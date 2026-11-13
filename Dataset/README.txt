================================================================================
DATASET TITLE:
SMADS: Student Mathematics Anxiety and Digital Learning Modalities Survey 
Dataset for Predictive Modeling (N = 1,953)

AUTHORS:
Md. Atiqur Rahman Sifat, Most Rimi Moni, Muhammad Imtiaz Ahmed, 
Fahmida Fardousi, Tahmina Islam

VERSION & DATE:
Version 1.0 (November 2026)

LICENSE:
Creative Commons Attribution 4.0 International (CC BY 4.0)
================================================================================

1. DATASET OVERVIEW
SMADS is a cross-disciplinary survey dataset comprising 1,953 valid student 
responses. It captures demographic profiles, study habits, mathematics 
anxiety, test stress, perceived teacher adaptability, and academic exam 
performance across Traditional, AI-Based, and Hybrid teaching modalities. 
All missing values, empty trailing rows, and personally identifiable 
information (PII) have been removed.

2. FILE STRUCTURE
- StudentsResponses.csv         : Preprocessed dataset (1,953 rows, 16 columns)
- StudentsResponses.xlsx        : Preprocessed dataset (1,953 rows, 16 columns)
- README.txt                    : Dataset documentation and data dictionary

3. DATA DICTIONARY (COLUMN DESCRIPTIONS)

- socio_economic_background (Categorical)
  Student household income bracket.
  Values: 'Low Income', 'Middle Income', 'High Income'

- preferred_learning_platform (Categorical)
  Primary preferred platform for learning.
  Values: 'Blended Learning (Online + Offline mix)', 'Online Learning (E-learning)', 
          'Classroom Learning', 'Self-Study (Books, Notes, Materials)', 
          'Tutoring / Coaching', 'Group Study'

- education_level (Categorical)
  Current academic education tier.
  Values: 'Secondary', 'Higher Secondary', 'Undergraduate (Bachelor)', 
          'Graduate (Master)', 'Postgraduate / PhD'

- age (Numeric / Integer)
  Age of the respondent in years (Range: 13 to 37).

- homework_completion_rate (Ordinal / Categorical)
  Percentage bracket of assigned mathematics homework completed.
  Values: 'Very Low (0–20%)', 'Low (21–40%)', 'Moderate (41–60%)', 
          'High (61–80%)', 'Very High (81–100%)'

- time_spent_math_learning (Ordinal / Categorical)
  Overall time dedicated to mathematics learning.
  Values: 'Less than 1 hour', '1–2 hours', '2–3 hours', 
          '3–4 hours', 'More than 4 hours'

- recent_teaching_method (Categorical)
  Primary teaching modality experienced in recent mathematics coursework.
  Values: 'Traditional (classroom, textbook, lectures)', 
          'AI-based (intelligent tutoring system, adaptive app, online AI tool)', 
          'Hybrid (Traditional + AI Based)'

- avoids_math_tasks (Binary / Categorical)
  Indicates whether the student avoids math-related tasks whenever possible.
  Values: 'Yes', 'No'

- classroom_math_enjoyment (Numeric / Ordinal)
  Self-reported enjoyment rating of learning math in a traditional classroom.
  Scale: 1 (Lowest enjoyment) to 5 (Highest enjoyment)

- memorization_level (Ordinal / Categorical)
  Retention level of mathematical techniques taught in traditional classrooms.
  Values: 'Short Term', 'Moderate', 'Long Term'

- problem_solving_nervousness (Ordinal / Categorical)
  Self-reported anxiety/nervousness level while solving math problems.
  Values: 'No', 'Low', 'Moderate', 'High', 'Extreme'

- test_stress_level (Ordinal / Categorical)
  Self-reported stress level prior to mathematics exams/tests.
  Values: 'Very Low', 'Low', 'Moderate', 'High', 'Very High'

- teacher_flexibility (Ordinal / Categorical)
  Perceived flexibility of the instructor in adapting to student learning needs.
  Values: 'Not Flexible at All', 'Less Flexible', 'Moderately Flexible', 
          'Flexible', 'Highly Flexible'

- academic_background (Categorical)
  Student's primary field of study / academic track.
  Values: 'Science (e.g., Engineering, MBBS)', 
          'Commerce (e.g., Business, Management)', 
          'Social Science / Humanities & Arts (e.g., Political Science, Psychology)'

- current_math_score (Numeric / Continuous)
  Last recorded mathematics exam score normalized on a 10-point scale 
  (Range: 1.0 to 10.0).

- gender (Categorical)
  Gender of the respondent.
  Values: 'Male', 'Female'
================================================================================