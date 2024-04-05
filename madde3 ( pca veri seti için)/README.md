# Logistic Regression with PCA on Diabetes Dataset

This project utilizes logistic regression to classify diabetes outcomes based on PCA-transformed features. It includes training a logistic regression model using PCA-transformed features and evaluating its performance using metrics such as confusion matrix, classification report, and performance metrics.

## Usage

1. Ensure that you have pandas, scikit-learn, and any other required dependencies installed. You can install them using the following commands:

2. Place the PCA results file named `pca_sonucları.csv` in the project directory. This file should contain the PCA-transformed features and outcomes.

3. Run the `logistic_regression_pca.py` script. This script will load the PCA results file, split the data into training and testing sets, train a logistic regression model, evaluate its performance, and save the evaluation results to CSV files (`confusion_matrix.csv`, `classification_report.csv`, and `performance_metrics.csv`).

## Description

- `logistic_regression_pca.py`: This is the main script file. It loads the PCA results file, trains a logistic regression model, evaluates its performance, and saves the evaluation results to CSV files.

- `pca_sonucları.csv`: The PCA results file containing the PCA-transformed features and outcomes.

- `confusion_matrix.csv`: The CSV file containing the confusion matrix.

- `classification_report.csv`: The CSV file containing the classification report.

- `performance_metrics.csv`: The CSV file containing performance metrics such as sensitivity, specificity, accuracy, and F1-score.

## Results

- Confusion Matrix: The confusion matrix is saved to the `confusion_matrix.csv` file.

- Classification Report: The classification report is saved to the `classification_report.csv` file.

- Performance Metrics: Sensitivity, specificity, accuracy, and F1-score are calculated and saved to the `performance_metrics.csv` file.

## License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.
