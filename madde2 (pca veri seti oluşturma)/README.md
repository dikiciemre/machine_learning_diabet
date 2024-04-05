# Diabetes Dataset Analysis with PCA (Principal Component Analysis)

This project includes a Python script that performs dimensionality reduction using PCA (Principal Component Analysis) on a diabetes dataset. PCA is a technique used to understand the relationships between variables in a dataset and to reduce the dimensionality of the data.

## Usage

1. First, install the pandas and scikit-learn libraries if they are not already installed on your computer. You can use the following commands:

2. Ensure that there is a dataset file named `diabetesSet.csv` in the project's main directory. This file should contain the features and outcomes of diabetes patients.

3. Next, run the `diabetes_pca.py` script. This script will load the dataset, create the PCA model, save the results to a new CSV file named `pca_results.csv`, and print the path to the created file.

## Description

- `diabetes_pca.py`: This is the main script file. It loads the dataset, creates the PCA model, saves the results, and prints the file path.

- `diabetesSet.csv`: The dataset file to be used for analysis.

- `pca_results.csv`: The new CSV file where the PCA results are saved.

## PCA (Principal Component Analysis)

PCA is a dimensionality reduction technique used in multivariate datasets. It is used to understand relationships between variables and to reduce the dimensionality of the data. In this project, PCA is used to find the principal components of the diabetes dataset and reduce its dimensionality.

## License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.
