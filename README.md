# Mental-Health-Survey
# 🧠 Mental Health in Tech Survey Analysis

## 📌 Project Overview

This project analyzes the **Mental Health in Tech Survey** dataset to understand patterns related to mental-health treatment, workplace environment, employee demographics, and access to mental-health support.

The project includes:

* Data cleaning and preprocessing using Python
* Exploratory Data Analysis (EDA)
* Univariate, bivariate, and multivariate analysis
* Analysis of demographic and workplace factors
* Mental-health treatment analysis
* Interactive visualizations
* Streamlit dashboard development
* Business insights and recommendations

---

## 🎯 Project Objective

The primary objective of this project is to analyze workplace mental-health data and identify patterns associated with employees' mental-health treatment and workplace experiences.

The analysis focuses on factors such as:

* Age
* Gender
* Family history
* Remote work
* Technology company employment
* Company size
* Mental-health benefits
* Mental-health care options
* Workplace anonymity
* Work interference
* Perceived workplace consequences

---

## 📂 Dataset

**Dataset:** Mental Health in Tech Survey

The dataset contains information collected from employees regarding their experiences and perceptions related to mental health in the workplace.

### Key Dataset Features

| Feature                     | Description                                                             |
| --------------------------- | ----------------------------------------------------------------------- |
| `Age`                       | Age of the respondent                                                   |
| `Gender`                    | Gender of the respondent                                                |
| `Country`                   | Country of the respondent                                               |
| `family_history`            | Whether the respondent has a family history of mental-health conditions |
| `treatment`                 | Whether the respondent has received mental-health treatment             |
| `remote_work`               | Whether the respondent works remotely                                   |
| `tech_company`              | Whether the respondent works in a technology company                    |
| `no_employees`              | Company size                                                            |
| `benefits`                  | Availability of mental-health benefits                                  |
| `care_options`              | Availability/awareness of mental-health care options                    |
| `anonymity`                 | Perception of anonymity when seeking support                            |
| `work_interfere`            | Extent to which mental health interferes with work                      |
| `mental_health_consequence` | Perceived workplace consequences related to mental health               |

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Plotly**
* **Streamlit**
* **Jupyter Notebook / Google Colab**

---

## 🧹 Data Cleaning

The following preprocessing steps were performed:

1. Loaded the survey dataset using Pandas.
2. Checked the dataset dimensions and data types.
3. Identified missing values.
4. Checked and removed duplicate records.
5. Removed the `comments` column because of high missingness.
6. Filled missing values in relevant categorical columns with `"Unknown"`.
7. Converted `timestamp` into datetime format.
8. Converted `age` into numeric format.
9. Identified invalid age values and handled them appropriately.
10. Standardized gender categories into consistent groups.
11. Removed unnecessary whitespace and standardized text values.
12. Verified the cleaned dataset.

### Cleaned Dataset

The cleaned dataset was saved as:

```text
mental_health_tech_survey_cleaned.csv
```

---

# 📊 Exploratory Data Analysis

The project contains extensive EDA using univariate, bivariate, and multivariate visualizations.

## 1. Univariate Analysis

The following variables were analyzed individually:

* Age Distribution
* Gender Distribution
* Mental Health Treatment
* Family History
* Remote Work
* Technology Company
* Company Size
* Work Interference
* Mental Health Benefits
* Mental Health Care Options
* Perception of Anonymity
* Mental Health Consequences

---

## 2. Bivariate Analysis

Relationships between variables were analyzed using grouped charts and percentage-based comparisons.

### Key analyses include:

* Treatment by Gender
* Treatment by Family History
* Treatment by Remote Work
* Treatment by Technology Company
* Treatment by Company Size
* Family History by Gender
* Work Interference by Gender
* Mental Health Benefits vs Treatment
* Care Options vs Treatment
* Anonymity vs Treatment
* Mental Health Consequences vs Treatment

---

## 3. Multivariate Analysis

Multivariate analysis was performed to understand relationships involving multiple demographic and workplace variables.

Examples include:

* Age + Gender + Treatment
* Gender + Family History
* Gender + Work Interference
* Company Size + Treatment
* Remote Work + Treatment
* Technology Company + Treatment
* Correlation analysis of numerical variables

---

# 📈 Key Visualizations

The project includes visualizations such as:

### Demographic Analysis

* Age Distribution
* Gender Distribution
* Country Distribution
* Age by Gender

### Workplace Analysis

* Remote Work Distribution
* Technology Company Distribution
* Company Size Distribution
* Work Interference by Gender

### Mental Health Analysis

* Treatment Distribution
* Family History Distribution
* Mental Health Benefits
* Mental Health Care Options
* Perception of Anonymity
* Mental Health Consequences

### Treatment Analysis

* Treatment Rate by Gender
* Treatment Rate by Family History
* Treatment Rate by Remote Work
* Treatment Rate by Company Size
* Treatment by Technology Company

---

# 💡 Key Insights

The analysis provides several useful observations:

### 👥 Demographics

The dataset contains respondents from different age and gender groups, allowing mental-health patterns to be examined across demographic segments.

### 🏢 Company Size

Mental-health treatment responses vary across company-size categories. Percentage-based analysis provides a better comparison when group sizes differ.

### 🏠 Remote Work

Treatment responses differ between remote and non-remote workers. The analysis indicates an association worth further investigation.

### 👨‍💻 Technology Companies

Respondents working in technology and non-technology companies show differences in treatment responses.

### 👨‍👩‍👧 Family History

Treatment rates vary based on reported family history, making family history an important variable for further analysis.

### 🧠 Workplace Support

The availability and awareness of mental-health benefits and care options vary among respondents.

### 🔒 Anonymity

Respondents have different perceptions about whether mental-health support can be accessed anonymously. Uncertainty about anonymity highlights the importance of clear workplace communication regarding confidentiality.

### ⚠️ Work Interference

Respondents report different levels of mental-health interference with their work, ranging from no interference to more frequent interference.

---

# 🚀 Streamlit Application

An interactive Streamlit dashboard was developed to make the analysis easier to explore.

## Dashboard Features

### 📌 Overview

* Dataset summary
* KPI cards
* Treatment distribution
* Gender distribution
* Remote work distribution
* Technology company distribution

### 👤 Demographics

* Age distribution
* Gender analysis
* Family history
* Treatment by gender
* Age and treatment analysis

### 🏢 Workplace

* Remote work
* Technology company
* Company size
* Work interference
* Workplace mental-health support

### 🧠 Mental Health

* Treatment distribution
* Family history
* Benefits
* Care options
* Anonymity
* Mental-health consequences

### 🔍 Data Explorer

* Interactive data filtering
* Dataset preview
* Cross-tabulation
* Filtered data download

---

# ▶️ How to Run the Streamlit Application

## Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

## Step 2: Navigate to the Project Folder

```bash
cd mental-health-tech-survey
```

## Step 3: Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn plotly streamlit
```

Or use:

```bash
pip install -r requirements.txt
```

## Step 4: Place the Dataset

Keep the cleaned CSV file in the same folder as the Streamlit application:

```text
project/
│
├── mental_health_streamlit_app.py
├── mental_health_tech_survey_cleaned.csv
├── requirements.txt
└── README.md
```

## Step 5: Run Streamlit

```bash
streamlit run mental_health_streamlit_app.py
```

The application will open in your browser.

---

# 📁 Project Structure

```text
Mental-Health-Tech-Survey/
│
├── data/
│   └── mental_health_tech_survey_cleaned.csv
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   └── EDA.ipynb
│
├── app/
│   └── mental_health_streamlit_app.py
│
├── requirements.txt
│
└── README.md
```

---

# 📋 Requirements

Example `requirements.txt`:

```text
pandas
numpy
matplotlib
seaborn
plotly
streamlit
```

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

# 🔄 Project Workflow

```text
Raw Dataset
     ↓
Data Loading
     ↓
Data Cleaning
     ↓
Missing Value Handling
     ↓
Duplicate Removal
     ↓
Data Transformation
     ↓
Exploratory Data Analysis
     ↓
Univariate Analysis
     ↓
Bivariate Analysis
     ↓
Multivariate Analysis
     ↓
Insights & Recommendations
     ↓
Streamlit Dashboard
```

---

# 🎯 Business Recommendations

Based on the analysis, organizations can consider:

1. **Improve awareness of mental-health benefits**
   Clearly communicate available mental-health benefits and support programs.

2. **Improve access to care options**
   Employees should be able to easily identify and access available mental-health resources.

3. **Communicate confidentiality policies**
   Clear information about anonymity and confidentiality can reduce uncertainty around seeking support.

4. **Create a supportive workplace environment**
   Organizations can encourage open and non-stigmatizing conversations about mental health.

5. **Monitor work interference**
   Organizations can pay attention to workplace factors that may make it difficult for employees to manage mental-health challenges.

6. **Use data-driven employee support**
   Demographic and workplace patterns can be analyzed to understand where additional awareness or support may be useful.

---

# ⚠️ Limitations

* The analysis is based on survey responses and may contain self-reported bias.
* The dataset does not establish causal relationships.
* Some variables contain missing or unknown responses.
* Differences between groups should be interpreted alongside their sample sizes.
* The analysis represents the available survey data and may not generalize to every workplace or population.

---

# 🔮 Future Improvements

Future versions of the project could include:

* Machine-learning models to predict treatment responses
* Statistical significance testing
* Feature importance analysis
* Employee segmentation
* Advanced interactive dashboards
* Deployment using Streamlit Cloud
* Automated data updates
* Additional survey datasets for comparison

---

# 👩‍💻 Author

**Ekta**

Aspiring Data Analyst | Python | SQL | Power BI | Excel | Streamlit

---

## ⭐ Project Highlights

**Skills demonstrated:**

`Python` • `Pandas` • `NumPy` • `EDA` • `Data Cleaning` • `Data Visualization` • `Seaborn` • `Plotly` • `Streamlit` • `Business Insights`

---

## 📌 Conclusion

This project demonstrates an end-to-end **data analytics workflow**, starting from raw survey data and progressing through data cleaning, exploratory analysis, visualization, insight generation, and interactive dashboard development.

The project provides a structured approach to understanding workplace mental-health patterns while highlighting the importance of data-driven analysis, employee support, and clear communication of available mental-health resources.
