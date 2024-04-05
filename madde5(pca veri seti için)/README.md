# Naive Bayes Classifier Evaluation on Diabetes Dataset

This project involves training a Naive Bayes classifier on a diabetes dataset and evaluating its performance using various metrics such as accuracy, precision, recall, and F1 score. It includes loading the dataset, splitting it into training and testing sets, training the Naive Bayes classifier, making predictions on the test data, calculating performance metrics, and saving the results to CSV files.

## Usage

1. Ensure that you have pandas and scikit-learn installed. You can install them using the following commands:

2. Place the dataset file named `diabetesSet.csv` in the project directory. This file should contain the features and outcomes of diabetes patients.

3. Run the `naive_bayes_evaluation.py` script. This script will load the dataset, split it into training and testing sets, train a Naive Bayes classifier, evaluate its performance, and save the results to CSV files.

## Description

- `naive_bayes_evaluation.py`: This is the main script file. It loads the dataset, splits it into training and testing sets, trains a Naive Bayes classifier, evaluates its performance, and saves the results to CSV files.

- `diabetesSet.csv`: The dataset file containing the features and outcomes of diabetes patients.

- `naive_bayes_results.csv`: The CSV file containing performance metrics such as accuracy, precision, recall, and F1 score.

- `confusion_matrix.csv`: The CSV file containing the confusion matrix.

## Results

- Performance Metrics: Accuracy, precision, recall, and F1 score of the Naive Bayes classifier are saved to a CSV file (`naive_bayes_results.csv`).

- Confusion Matrix: The confusion matrix is saved to a CSV file (`confusion_matrix.csv`).

## License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.
