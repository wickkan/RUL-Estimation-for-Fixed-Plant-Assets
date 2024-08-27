# **Predictive Maintenance and Remaining Useful Life (RUL) Estimation for Fixed Plant Assets**

This project focuses on developing predictive maintenance models to estimate the remaining useful life (RUL) of fixed plant assets, such as machinery and equipment used in mining operations. The goal is to prevent unexpected failures, optimise maintenance schedules, and reduce downtime, ultimately improving operational efficiency and cost-effectiveness

## **Key Objectives**

1. **Data Collection and Preparation:**

   - **Data Sources:** Utilises historical operational data from sensors and logs associated with plant assets. This includes metrics such as temperature readings, vibration data, rotational speed, torque, and tool wear. Dataset: https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset
   - **Data Cleaning:** Handled missing values, outliers, and inconsistent data entries to ensure a high-quality dataset suitable for modeling.
   - **Feature Engineering:** Created new features from the raw data, including interaction terms and lag features, to improve the predictive power of the models.

2. **Exploratory Data Analysis (EDA):**

   - Performed exploratory analysis to understand the distribution and relationships within the data.
   - Visualised key variables and their interactions with the target variable to uncover patterns and insights.
   - Analysed failure modes and the conditions leading to different types of failures.

3. **Predictive Modelling:**

   - **Model Selection:** Trained and evaluated multiple machine learning models, including Logistic Regression, Random Forest, and Gradient Boosting techniques like XGBoost.
   - **Model Evaluation:** Used metrics such as F1-score, ROC-AUC, and confusion matrices to evaluate the models' performance, particularly focusing on handling imbalanced data.
   - **Hyperparameter Tuning:** Optimised model parameters to enhance performance and generalisability.

4. **Remaining Useful Life (RUL) Estimation:**

   - Extended the predictive models to estimate the remaining useful life of assets based on their current condition and historical performance data.
   - Implemented survival analysis techniques or regression-based models to predict the time-to-failure for each asset.
