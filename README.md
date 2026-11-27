# Explainable AI for Predicting Mathematics Avoidance in Higher Education

Code for the paper "Explainable AI for Predicting Mathematics Avoidance in
Higher Education: A Control-Value Theory Guided Approach"

The project predicts mathematics avoidance among university students using a
stacking ensemble, and explains the predictions with SHAP.

## Method

- Dataset: survey responses from 1,750 university students after removing
  duplicates (16 variables)
- Encoding: ordinal encoding for Likert-type variables, label encoding for
  nominal variables
- Split: stratified 80/20 train/test (random seed 42), 5-fold cross-validation
- Base learners: Random Forest and SVM
- Meta-learner: Logistic Regression
- Baselines: Logistic Regression, SVM, Decision Tree, Random Forest
- Explainability: SHAP (summary and global importance plots)

## Results (N = 1,750)

| Model               | Acc (%) | AUC   |
| ------------------- | ------- | ----- |
| Logistic Regression | 73.43   | 0.818 |
| SVM                 | 84.29   | 0.931 |
| Decision Tree       | 92.86   | 0.932 |
| Random Forest       | 94.29   | 0.989 |
| Stacking (proposed) | 95.43   | 0.989 |

Exact numbers can vary slightly across library versions and environments.

## Data

The dataset is not included in this repository. It is available from the
corresponding author on reasonable request. To run the code, place it in this
folder as `StudentsResponses.csv`.

## How to run

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python replicate.py
```

## Outputs

`table_v_results.csv` and the figures `fig3_comparison.png`,
`fig4_confusion.png`, `fig5_roc.png`, `fig6_shap_beeswarm.png`,
`fig7_shap_bar.png`.
