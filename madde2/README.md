# PCA (Principal Component Analysis) and LDA (Linear Discriminant Analysis) on Diabetes Dataset

This project utilizes PCA and LDA techniques to perform dimensionality reduction on a diabetes dataset. PCA and LDA are both widely used techniques in machine learning and data analysis to reduce the dimensionality of the dataset while preserving the most important information.

## Usage

1. Ensure that you have pandas and scikit-learn libraries installed. You can install them using the following commands:

2. Place the dataset file named `diabetesSet.csv` in the project directory. This dataset file should contain the features and outcomes of diabetes patients.

3. Run the `pca_lda_analysis.py` script. This script will load the dataset, perform PCA and LDA, save the results to CSV files (`pca_lda_results.csv`, `pca_components.csv`, and `lda_components.csv`), and print the feature weights for PCA and LDA.

## Description

- `pca_lda_analysis.py`: This is the main script file. It loads the dataset, applies PCA and LDA, saves the results to CSV files, and prints the feature weights for PCA and LDA.

- `diabetesSet.csv`: The dataset file containing the features and outcomes of diabetes patients.

- `pca_lda_results.csv`: The CSV file containing the results of PCA and LDA analysis.

- `pca_components.csv` and `lda_components.csv`: CSV files containing the feature weights for PCA and LDA.

## Results

- PCA Feature Weights: The feature weights for PCA analysis are printed to the console.
- LDA Feature Weights: The feature weights for LDA analysis are printed to the console.

## License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.
