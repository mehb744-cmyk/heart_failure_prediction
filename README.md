# Project title
## Heart Failure Prediction

### Project Background

This project is a rebuilt and extended version of an earlier heart-failure prediction project. The original project included the machine-learning model, visualisations, and Flask dashboard.

This version reconstructs the workflow with a cleaner project structure, documented analysis, reusable code, version control, testing, and improved documentation.

### Dataset
Dataset: https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction<br>
Source: Kaggle<br>
Number of records: 918<br>
Features: 13 original clinical/demographic variables<br>
Target: Heart Disease<br>

The dataset is used to develop machine-learning models for predicting the HeartDisease target based on patient demographic and clinical characteristics.

### Introduction 
Cardiovascular diseases (CVDs) are among the leading causes of death globally, accounting for an estimated 31% of deaths worldwide. Heart failure is one of the common conditions caused by CVDs. Therefore, early prediction and diagnosis of heart failure can significantly improve patient outcomes and reduce the burden on healthcare systems. This project aims to develop a machine learning model for predicting heart failure using clinical data. The dataset used in this project, Heart Failure Prediction Dataset, was obtained from Kaggle and contains clinical information related to patients with heart failure, which will be used to train and evaluate the machine learning model.

### Machine Learning Models 
Several classification algorithms were evaluated:
- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

The data was preprocessed before model training. Categorical variables were one-hot encoded, and feature scaling was applied where appropriate.

### Cross-Validation
Five-fold stratified cross-validation was used to evaluate the baseline models while maintaining the class distribution across folds. The models demonstrated different performance characteristics across the evaluation metrics. The cross-validation results were used to assess model consistency and compare performance before hyperparameter tuning.

### Hyperparameter Tuning
Hyperparameter tuning was performed using GridSearchCV with five-fold stratified cross-validation.

- Logistic Regression achieved a best cross-validation ROC-AUC of 0.9227.
- Random Forest achieved a best cross-validation ROC-AUC of 0.9331.
- SVM achieved a best cross-validation ROC-AUC of 0.9225.

The tuned Random Forest therefore had the highest observed cross-validation ROC-AUC among these three tuned models.

### Final Test Evaluation
After hyperparameter tuning, the selected tuned models were evaluated on the independent test set.

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 89.67% | 89.52% | 92.16% | 90.82% | 0.9333 |
| Random Forest | 88.59% | 87.85% | 92.16% | 89.95% | 0.9334 |
| SVM | 86.41% | 85.98% | 90.20% | 88.04% | 0.9292 |

On the independent test set, Logistic Regression and Random Forest produced very similar ROC-AUC values (0.9333 and 0.9334 respectively), while SVM achieved 0.9292. Logistic Regression was used for the Flask application. The saved model includes the preprocessing pipeline required for prediction.

### Flask Application
The trained Logistic Regression pipeline was saved as a .pkl file and integrated into a Flask web application. The application allows a user to enter patient information through a web form. The input is converted into the feature representation expected by the trained model, after which the model generates a prediction and predicted probability. The Flask application is intended as a demonstration of machine-learning deployment and is not a medical diagnostic tool.
