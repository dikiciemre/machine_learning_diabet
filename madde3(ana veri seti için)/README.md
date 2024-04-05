# Classification Models Evaluation on Diabetes Dataset

This project involves training and evaluating two classification models, namely Linear Regression and Logistic Regression, on a diabetes dataset. It includes splitting the dataset into training and testing sets, training the models, evaluating their performance using various metrics such as mean squared error (for Linear Regression) and accuracy, confusion matrix, precision, recall, and F1-score (for Logistic Regression).

## Usage

1. Ensure that you have pandas, scikit-learn, and any other required dependencies installed. You can install them using the following commands:

2. Place the dataset file named `diabetesSet.csv` in the project directory. This file should contain the features and outcomes of diabetes patients.

3. Run the `classification_evaluation.py` script. This script will load the dataset, split it into training and testing sets, train Linear Regression and Logistic Regression models, evaluate their performance, and save the evaluation results to a CSV file (`classification_results.csv`).

## Description

- `classification_evaluation.py`: This is the main script file. It loads the dataset, splits it into training and testing sets, trains two classification models, evaluates their performance, and saves the evaluation results to a CSV file.

- `diabetesSet.csv`: The dataset file containing the features and outcomes of diabetes patients.

- `classification_results.csv`: The CSV file containing the evaluation results including mean squared error, accuracy, confusion matrix, precision, recall, and F1-score.

## Results

- Mean Squared Error (for Linear Regression): The mean squared error is calculated for Linear Regression and saved in the `classification_results.csv` file.

- Accuracy, Confusion Matrix, Precision, Recall, and F1-score (for Logistic Regression): These metrics are calculated for Logistic Regression and saved in the `classification_results.csv` file.

## License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.
