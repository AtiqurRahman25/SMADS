"""Replication of: Explainable AI for Predicting Mathematics Avoidance (stacking RF + SVM -> LogReg, SHAP)."""
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier, StackingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score,
                             roc_auc_score, roc_curve, confusion_matrix)

warnings.filterwarnings("ignore")
SEED = 42
DATA = "StudentsResponses.csv"
TARGET = "avoids_math_tasks"

# ---------- 1. Load & clean (paper: 1,953 -> 1,750; drop Timestamp -> 16 variables) ----------
df = pd.read_csv(DATA)
df = df[[c for c in df.columns if not c.startswith("Unnamed")]]   # stray empty columns in the CSV
df = df.drop(columns=["Timestamp"]).drop_duplicates().reset_index(drop=True)
print("Shape after cleaning:", df.shape)                           # expect (1750, 16)

# ---------- 2. Encoding (Eq. 1: ordinal 0..K-1 for Likert-type, label codes for nominal) ----------
ordered = {
    "homework_completion_rate": ["Very Low (0–20%)", "Low (21–40%)", "Moderate (41–60%)", "High (61–80%)", "Very High (81–100%)"],
    "time_spent_math_learning": ["Less than 1 hour", "1–2 hours", "2–3 hours", "3–4 hours", "More than 4 hours"],
    "memorization_level": ["Short Term", "Moderate", "Long Term"],
    "problem_solving_nervousness": ["No", "Low", "Moderate", "High", "Extreme"],
    "test_stress_level": ["Very Low", "Low", "Moderate", "High", "Very High"],
    "teacher_flexibility": ["Not Flexible at All", "Less Flexible", "Moderately Flexible", "Flexible", "Highly Flexible"],
    "socio_economic_background": ["Low Income", "Middle Income", "High Income"],
    "education_level": ["Secondary", "Higher Secondary", "Undergraduate (Bachelor)", "Graduate (Master)", "Postgraduate / PhD"],
}
nominal = ["preferred_learning_platform", "recent_teaching_method", "academic_background", "gender"]

X = df.drop(columns=[TARGET]).copy()
y = (df[TARGET] == "Yes").astype(int)
for col, order in ordered.items():
    X[col] = X[col].map({v: i for i, v in enumerate(order)})
X[nominal] = OrdinalEncoder().fit_transform(X[nominal])
assert X.isna().sum().sum() == 0, "unmapped category found"

# ---------- 3. Stratified 80/20 split ----------
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.20, stratify=y, random_state=SEED)

# ---------- 4. Models (Table IV hyperparameters) ----------
rf  = RandomForestClassifier(n_estimators=100, max_depth=None, criterion="gini", random_state=SEED)
svm = make_pipeline(StandardScaler(), SVC(kernel="rbf", C=1.0, gamma="scale", probability=True, random_state=SEED))
lr  = LogisticRegression(penalty="l2", solver="lbfgs", max_iter=1000)
cv  = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
stack = StackingClassifier(estimators=[("rf", rf), ("svm", svm)],
                           final_estimator=LogisticRegression(penalty="l2", solver="lbfgs", max_iter=1000),
                           stack_method="predict_proba", cv=cv)
models = {
    "Logistic Regression": make_pipeline(StandardScaler(), lr),
    "SVM": svm,
    "Decision Tree": DecisionTreeClassifier(random_state=SEED),
    "Random Forest": rf,
    "Stacking (Proposed)": stack,
}

# ---------- 5. Train / evaluate (Table V) ----------
rows, probs = [], {}
for name, m in models.items():
    m.fit(X_tr, y_tr)
    pred, p = m.predict(X_te), m.predict_proba(X_te)[:, 1]
    probs[name] = p
    rows.append([name, accuracy_score(y_te, pred) * 100, precision_score(y_te, pred),
                 recall_score(y_te, pred), f1_score(y_te, pred), roc_auc_score(y_te, p)])
res = pd.DataFrame(rows, columns=["Model", "Acc (%)", "Prec", "Rec", "F1", "AUC"]).round(3)
print(res.to_string(index=False))
res.to_csv("table_v_results.csv", index=False)

# 5-fold CV mean/std (Eq. 8-9) on the training set
sc = cross_val_score(stack, X_tr, y_tr, cv=cv, scoring="accuracy")
print(f"Stacking 5-fold CV accuracy: mean={sc.mean():.4f}, std={sc.std():.4f}")

# ---------- 6. Figures 3, 4, 5 ----------
res.melt(id_vars="Model", value_vars=["Prec", "F1"]).pipe(
    lambda d: sns.barplot(data=d, x="variable", y="value", hue="Model"))
plt.title("Model performance comparison"); plt.savefig("fig3_comparison.png", dpi=200, bbox_inches="tight"); plt.close()

cm = confusion_matrix(y_te, stack.predict(X_te))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["No", "Yes"], yticklabels=["No", "Yes"])
plt.xlabel("Predicted Label"); plt.ylabel("True Label"); plt.title("Confusion Matrix for Stacking Ensemble")
plt.savefig("fig4_confusion.png", dpi=200, bbox_inches="tight"); plt.close()

for name, p in probs.items():
    fpr, tpr, _ = roc_curve(y_te, p)
    plt.plot(fpr, tpr, label=f"{name} (AUC = {roc_auc_score(y_te, p):.2f})")
plt.plot([0, 1], [0, 1], "k--", label="Random"); plt.legend(); plt.xlabel("False Positive Rate"); plt.ylabel("True Positive Rate")
plt.title("ROC Curves"); plt.savefig("fig5_roc.png", dpi=200, bbox_inches="tight"); plt.close()

# ---------- 7. SHAP (Fig. 6 & 7) ----------
try:
    import shap
    bg = shap.sample(X_tr, 100, random_state=SEED)
    f = lambda d: stack.predict_proba(pd.DataFrame(d, columns=X.columns))[:, 1]
    explainer = shap.KernelExplainer(f, bg)
    X_ex = X_te.sample(100, random_state=SEED)           # KernelExplainer is slow; use a subset (raise it if you have time)
    sv = explainer.shap_values(X_ex, nsamples=200)
    shap.summary_plot(sv, X_ex, show=False); plt.savefig("fig6_shap_beeswarm.png", dpi=200, bbox_inches="tight"); plt.close()
    shap.summary_plot(sv, X_ex, plot_type="bar", show=False); plt.savefig("fig7_shap_bar.png", dpi=200, bbox_inches="tight"); plt.close()
except ImportError:
    print("shap not installed -> skipping Fig. 6/7 (pip install shap)")
