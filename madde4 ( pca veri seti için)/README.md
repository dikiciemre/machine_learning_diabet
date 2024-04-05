# Decision Tree Classifier with PCA on Diabetes Dataset

This project involves training a decision tree classifier using PCA-transformed features on a diabetes dataset. It includes loading the dataset, applying PCA to reduce the dimensionality, splitting the data into training and testing sets, training the decision tree classifier, evaluating its performance, visualizing the decision tree structure, and saving the performance metrics to a CSV file.

## Usage

1. Ensure that you have pandas, scikit-learn, and matplotlib installed. You can install them using the following commands:

2. Place the PCA results file named `pca_sonucları.csv` and the original dataset file named `diyabetSet.csv` in the project directory. The original dataset file should contain the features and outcomes of diabetes patients.

3. Run the `decision_tree_pca.py` script. This script will load the PCA results and the original dataset, apply PCA to reduce dimensionality, split the data into training and testing sets, train a decision tree classifier, evaluate its performance, visualize the decision tree structure, and save the performance metrics to a CSV file.

## Description

- `decision_tree_pca.py`: This is the main script file. It loads the PCA results and the original dataset, applies PCA to reduce dimensionality, splits the data into training and testing sets, trains a decision tree classifier, evaluates its performance, visualizes the decision tree structure, and saves the performance metrics to a CSV file.

- `pca_sonucları.csv`: The PCA results file containing the PCA-transformed features.

- `diyabetSet.csv`: The original dataset file containing the features and outcomes of diabetes patients.

- `decision_tree_structure_pca.png`: The image file containing the visualized decision tree structure.

- `model_performance_decision_tree_pca.csv`: The CSV file containing the performance metrics, such as accuracy, of the decision tree classifier.

## Results

- Decision Tree Accuracy (Test): The accuracy of the decision tree classifier on the test dataset is calculated and printed to the console.

- Decision Tree Structure Visualization: The decision tree structure is visualized and saved as an image file (`decision_tree_structure_pca.png`).

- Performance Metrics: The accuracy of the decision tree classifier is saved to a CSV file (`model_performance_decision_tree_pca.csv`).

## License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.
