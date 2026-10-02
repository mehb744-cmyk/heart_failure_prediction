## Project Background

This project is a rebuilt and extended version of an earlier heart-failure prediction project. The original project included the machine-learning model, visualisations, and Flask dashboard.

This version reconstructs the workflow with a cleaner project structure, documented analysis, reusable Python modules, version control, testing, and improved documentation.

# Heart Failure Prediction
https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction

Cardiovascular diseases (CVDs) are among the leading causes of death globally, accounting for an estimated 31% of deaths worldwide. Heart failure is one of the common conditions caused by CVDs. Therefore, early prediction and diagnosis of heart failure can significantly improve patient outcomes and reduce the burden on healthcare systems. This project aims to develop a machine learning model for predicting heart failure using clinical data. The dataset used in this project, Heart Failure Prediction Dataset, was obtained from Kaggle and contains clinical information related to patients with heart failure, which will be used to train and evaluate the machine learning model.


## Project Status
Machine Learning models 
Among the baseline models evaluated on the test set, Logistic Regression achieved the highest accuracy (89.13%) and F1-score (90.29%), while SVM achieved the highest ROC-AUC (94.00%) and KNN achieved the highest recall (93.14%).

Cross-Validation
The five baseline models demonstrated different performance characteristics across the evaluation metrics. SVM achieved the highest mean accuracy, recall, and F1-score, while Logistic Regression achieved the highest mean precision. Random Forest achieved the highest mean ROC-AUC

Hyperparameter Tuning
After hyperparameter tuning using 5-fold stratified cross-validation, the Random Forest achieved a mean ROC-AUC of 0.9331, compared with 0.9227 for Logistic Regression and 0.9225 for SVM

The tuned Random Forest achieved a cross-validation ROC-AUC of 0.9331. On the independent test set, Logistic Regression and Random Forest achieved approximately 0.933 ROC-AUC, while SVM achieved approximately 0.929