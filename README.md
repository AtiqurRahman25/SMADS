<div align="center">
  <h1>SMADS: Student Mathematics Anxiety and Digital Learning Modalities Survey</h1>
  <h3>Dataset for Predictive Modeling (<i>N</i> = 1,953)</h3>

  <p>
    <strong>Authors:</strong> Md. Atiqur Rahman Sifat, Most Rimi Moni, Muhammad Imtiaz Ahmed, Fahmida Fardousi, Tahmina Islam<br>
    <strong>Version & Date:</strong> Version 1.0 (November 2026)<br>
    <strong>License:</strong> <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International (CC BY 4.0)</a>
  </p>
</div>

<hr>

<h2>1. Dataset Overview</h2>
<p>
  <strong>SMADS</strong> is a cross-disciplinary survey dataset comprising 1,953 valid student responses. 
  It captures demographic profiles, study habits, mathematics anxiety, test stress, perceived teacher adaptability, and academic exam performance across Traditional, AI-Based, and Hybrid teaching modalities. All missing values, empty trailing rows, and personally identifiable information (PII) have been removed.
</p>

<h2>2. File Structure</h2>
<ul>
  <li><code>StudentsResponses.csv</code> : Preprocessed dataset (1,953 rows, 16 columns)</li>
  <li><code>StudentsResponses.xlsx</code> : Preprocessed dataset (1,953 rows, 16 columns)</li>
  <li><code>README.txt</code> : Dataset documentation and data dictionary</li>
</ul>

<h2>3. Data Dictionary (Column Descriptions)</h2>

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #f2f2f2; text-align: left;">
      <th>Column Name & Type</th>
      <th>Description</th>
      <th>Allowed / Range Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>socio_economic_background</code><br><em>(Categorical)</em></td>
      <td>Student household income bracket.</td>
      <td><code>'Low Income'</code>, <code>'Middle Income'</code>, <code>'High Income'</code></td>
    </tr>
    <tr>
      <td><code>preferred_learning_platform</code><br><em>(Categorical)</em></td>
      <td>Primary preferred platform for learning.</td>
      <td>
        <code>'Blended Learning (Online + Offline mix)'</code>,<br>
        <code>'Online Learning (E-learning)'</code>,<br>
        <code>'Classroom Learning'</code>,<br>
        <code>'Self-Study (Books, Notes, Materials)'</code>,<br>
        <code>'Tutoring / Coaching'</code>,<br>
        <code>'Group Study'</code>
      </td>
    </tr>
    <tr>
      <td><code>education_level</code><br><em>(Categorical)</em></td>
      <td>Current academic education tier.</td>
      <td>
        <code>'Secondary'</code>, <code>'Higher Secondary'</code>,<br>
        <code>'Undergraduate (Bachelor)'</code>, <code>'Graduate (Master)'</code>,<br>
        <code>'Postgraduate / PhD'</code>
      </td>
    </tr>
    <tr>
      <td><code>age</code><br><em>(Numeric / Integer)</em></td>
      <td>Age of the respondent in years.</td>
      <td>Range: <strong>13 to 37</strong></td>
    </tr>
    <tr>
      <td><code>homework_completion_rate</code><br><em>(Ordinal / Categorical)</em></td>
      <td>Percentage bracket of assigned mathematics homework completed.</td>
      <td>
        <code>'Very Low (0–20%)'</code>, <code>'Low (21–40%)'</code>,<br>
        <code>'Moderate (41–60%)'</code>, <code>'High (61–80%)'</code>,<br>
        <code>'Very High (81–100%)'</code>
      </td>
    </tr>
    <tr>
      <td><code>time_spent_math_learning</code><br><em>(Ordinal / Categorical)</em></td>
      <td>Overall time dedicated to mathematics learning.</td>
      <td>
        <code>'Less than 1 hour'</code>, <code>'1–2 hours'</code>,<br>
        <code>'2–3 hours'</code>, <code>'3–4 hours'</code>,<br>
        <code>'More than 4 hours'</code>
      </td>
    </tr>
    <tr>
      <td><code>recent_teaching_method</code><br><em>(Categorical)</em></td>
      <td>Primary teaching modality experienced in recent mathematics coursework.</td>
      <td>
        <code>'Traditional (classroom, textbook, lectures)'</code>,<br>
        <code>'AI-based (intelligent tutoring system, adaptive app, online AI tool)'</code>,<br>
        <code>'Hybrid (Traditional + AI Based)'</code>
      </td>
    </tr>
    <tr>
      <td><code>avoids_math_tasks</code><br><em>(Binary / Categorical)</em></td>
      <td>Indicates whether the student avoids math-related tasks whenever possible.</td>
      <td><code>'Yes'</code>, <code>'No'</code></td>
    </tr>
    <tr>
      <td><code>classroom_math_enjoyment</code><br><em>(Numeric / Ordinal)</em></td>
      <td>Self-reported enjoyment rating of learning math in a traditional classroom.</td>
      <td>Scale: <strong>1</strong> (Lowest enjoyment) to <strong>5</strong> (Highest enjoyment)</td>
    </tr>
    <tr>
      <td><code>memorization_level</code><br><em>(Ordinal / Categorical)</em></td>
      <td>Retention level of mathematical techniques taught in traditional classrooms.</td>
      <td><code>'Short Term'</code>, <code>'Moderate'</code>, <code>'Long Term'</code></td>
    </tr>
    <tr>
      <td><code>problem_solving_nervousness</code><br><em>(Ordinal / Categorical)</em></td>
      <td>Self-reported anxiety/nervousness level while solving math problems.</td>
      <td><code>'No'</code>, <code>'Low'</code>, <code>'Moderate'</code>, <code>'High'</code>, <code>'Extreme'</code></td>
    </tr>
    <tr>
      <td><code>test_stress_level</code><br><em>(Ordinal / Categorical)</em></td>
      <td>Self-reported stress level prior to mathematics exams/tests.</td>
      <td><code>'Very Low'</code>, <code>'Low'</code>, <code>'Moderate'</code>, <code>'High'</code>, <code>'Very High'</code></td>
    </tr>
    <tr>
      <td><code>teacher_flexibility</code><br><em>(Ordinal / Categorical)</em></td>
      <td>Perceived flexibility of the instructor in adapting to student learning needs.</td>
      <td>
        <code>'Not Flexible at All'</code>, <code>'Less Flexible'</code>,<br>
        <code>'Moderately Flexible'</code>, <code>'Flexible'</code>,<br>
        <code>'Highly Flexible'</code>
      </td>
    </tr>
    <tr>
      <td><code>academic_background</code><br><em>(Categorical)</em></td>
      <td>Student's primary field of study / academic track.</td>
      <td>
        <code>'Science (e.g., Engineering, MBBS)'</code>,<br>
        <code>'Commerce (e.g., Business, Management)'</code>,<br>
        <code>'Social Science / Humanities & Arts (e.g., Political Science, Psychology)'</code>
      </td>
    </tr>
    <tr>
      <td><code>current_math_score</code><br><em>(Numeric / Continuous)</em></td>
      <td>Last recorded mathematics exam score normalized on a 10-point scale.</td>
      <td>Range: <strong>1.0 to 10.0</strong></td>
    </tr>
    <tr>
      <td><code>gender</code><br><em>(Categorical)</em></td>
      <td>Gender of the respondent.</td>
      <td><code>'Male'</code>, <code>'Female'</code></td>
    </tr>
  </tbody>
</table>
