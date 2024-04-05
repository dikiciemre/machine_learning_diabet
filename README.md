# Diabetes Dataset Analysis and Machine Learning Models

This project involves the analysis of the diabetes dataset and the application of various machine learning models for prediction. Below are the details of each model and how to use them:

## 1. Dataset

- `diabetesSet.csv`: The diabetes dataset is a CSV file containing features and outcomes of diabetes patients.

## 2. Data Analysis and Preprocessing

- `data_analysis_preprocessing.py`: This script loads the diabetes dataset, performs data analysis, and conducts necessary preprocessing steps. Preprocessing steps include handling missing data, encoding categorical variables, and data standardization.

## 3. Model 1: Decision Tree Classifier with PCA

- `decision_tree_pca.py`: This script builds and trains a decision tree classifier model using PCA components. It evaluates the model's performance and visualizes the decision tree structure.

## 4. Model 2: Decision Tree Classifier Performance Evaluation

- `decision_tree_evaluation.py`: This script trains a decision tree classifier model and evaluates its performance. Performance metrics such as accuracy, precision, recall, F1 score, and confusion matrix are used to measure the model's performance.

## 5. Model 3: Naive Bayes Classifier Evaluation

- `naive_bayes_evaluation.py`: This script trains a Naive Bayes classifier model and evaluates its performance. Performance metrics such as accuracy, precision, recall, F1 score, and confusion matrix are used to measure the model's performance.

## Installation

1. Install Anaconda or a similar Python distribution.
2. Install the required Python libraries using the `requirements.txt` file:
3. Add the dataset to the root directory of the project (`diabetesSet.csv`).
4. Run the respective model script (e.g., `python decision_tree_pca.py`).

## License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.
