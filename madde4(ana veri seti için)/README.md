# Decision Tree Classifier Performance Evaluation on Diabetes Dataset

This project involves training a decision tree classifier on a diabetes dataset and evaluating its performance using various metrics such as accuracy, precision, recall, F1 score, and confusion matrix. It includes loading the dataset, splitting it into training and testing sets, training the decision tree classifier, making predictions on the test data, calculating performance metrics, visualizing the decision tree structure, and saving the performance metrics, confusion matrix, and decision tree structure to CSV and PNG files.

## Usage

1. Ensure that you have pandas, scikit-learn, and matplotlib installed. You can install them using the following commands:

2. Place the dataset file named `diabetesSet.csv` in the project directory. This file should contain the features and outcomes of diabetes patients.

3. Run the `decision_tree_performance_evaluation.py` script. This script will load the dataset, split it into training and testing sets, train a decision tree classifier, evaluate its performance, visualize the decision tree structure, and save the performance metrics, confusion matrix, and decision tree structure to CSV and PNG files.

## Description

- `decision_tree_performance_evaluation.py`: This is the main script file. It loads the dataset, splits it into training and testing sets, trains a decision tree classifier, evaluates its performance, visualizes the decision tree structure, and saves the performance metrics, confusion matrix, and decision tree structure to CSV and PNG files.

- `diabetesSet.csv`: The dataset file containing the features and outcomes of diabetes patients.

- `performance_metrics_decision_tree.csv`: The CSV file containing performance metrics such as accuracy, precision, recall, and F1 score.

- `confusion_matrix_decision_tree.csv`: The CSV file containing the confusion matrix.

- `decision_tree_structure.png`: The PNG image file containing the visualized decision tree structure.

## Results

- Performance Metrics: Accuracy, precision, recall, and F1 score of the decision tree classifier are saved to a CSV file (`performance_metrics_decision_tree.csv`).

- Confusion Matrix: The confusion matrix is saved to a CSV file (`confusion_matrix_decision_tree.csv`).

- Decision Tree Structure Visualization: The decision tree structure is visualized and saved as a PNG image file (`decision_tree_structure.png`).

## License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.
