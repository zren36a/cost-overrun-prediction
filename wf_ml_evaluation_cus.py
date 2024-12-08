# --------------------------------------
# Machine Learning, additionally, with customized normalization method
# --------------------------------------

import pandas as pd
from sklearn.model_selection import train_test_split
from wf_ml_training import train_original_knn, train_optimized_knn, train_logistic_regression, train_random_forest
from wf_ml_prediction import predict
from sklearn.metrics import accuracy_score, recall_score
import os

# Ensure necessary directories exist
os.makedirs("data_processed", exist_ok=True)
os.makedirs("evaluation", exist_ok=True)

# Proposed Encoding Normalization
def normalize_features(X):
    """
    Normalize features using predefined mapping directly in the code.
    Args:
        X (pd.DataFrame): Input features dataframe.
    Returns:
        pd.DataFrame: Normalized dataframe.
    """
    # Normalization mappings
    normalization_mapping = {
        "Project Phase Name": {
            "CM": 1.2,
            "Scope": 1.0,
            "Design": 0.8,
            "CM,F&E": 0.6,
            "Construction": 0.4,
            "CM,Art,F&E": 0.2,
        },
        "Project Type": {
            "SCA Emergency Lighting": 1.2,
            "SCA CIP": 1.0,
            "SCA CIP RESOA": 0.8,
            "SCA Lease Site Improvement": 0.6,
            "3K": 0.4,
            "SCA Capacity": 0.2,
        },
    }

    # Apply custom normalization for categorical features
    for feature, mapping in normalization_mapping.items():
        if feature in X.columns:
            X = X.copy()  # Fix for SettingWithCopyWarning
            X[feature] = X[feature].map(mapping)
            # Handle unmapped values by assigning a default value (e.g., -1)
            X[feature] = X[feature].fillna(-1)  # Replace with an appropriate default value

    # Normalize "Project Budget Amount" by binning
    if "Project Budget Amount" in X.columns:
        X = X.copy()  # Fix for SettingWithCopyWarning
        bin_edges = [0, 100000, 200000, 500000, 1000000, 5000000, 10000000, float("inf")]  # Budget ranges
        bin_labels = [1.4, 1.2, 1.0, 0.8, 0.6, 0.4, 0.2]  # Normalization values for bins
        X["Project Budget Amount"] = pd.cut(
            X["Project Budget Amount"], bins=bin_edges, labels=bin_labels, right=False
        )
        X["Project Budget Amount"] = X["Project Budget Amount"].astype(float).fillna(-1)  # Ensure numeric type

    return X

def split_data(data_path):
    """
    Split the dataset into training and testing sets.
    Args:
        data_path (str): Path to the dataset.
    Returns:
        None
    """
    # Load the dataset
    data = pd.read_csv(data_path)

    # Filter valid rows
    data_valid = data[data["Cost Overrun"].notnull()]
    print(f"Total rows: {len(data)}, Valid rows: {len(data_valid)}")

    # Select features and target
    X = data_valid[["Project Type", "Project Phase Name", "Project Budget Amount"]].copy()  # Fix for SettingWithCopyWarning
    y = data_valid["Cost Overrun"]

    # Normalize features based on the normalization mapping
    X = normalize_features(X)

    # Split into training and testing datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    # Save to data_processed folder
    X_train.to_csv("data_processed/training_data.csv", index=False)
    X_test.to_csv("data_processed/testing_data.csv", index=False)
    y_train.to_csv("data_processed/training_labels.csv", index=False)
    y_test.to_csv("data_processed/testing_labels.csv", index=False)
    print("Training and testing datasets created and saved.")

def evaluate_models():
    """
    Train models, perform predictions, and evaluate metrics.
    """
    # Load datasets
    X_train = pd.read_csv("data_processed/training_data.csv")
    y_train = pd.read_csv("data_processed/training_labels.csv")["Cost Overrun"]
    X_test = pd.read_csv("data_processed/testing_data.csv")
    y_test = pd.read_csv("data_processed/testing_labels.csv")["Cost Overrun"]

    # Train models and save them
    train_original_knn(X_train, y_train)
    train_optimized_knn(X_train, y_train)
    train_logistic_regression(X_train, y_train)
    train_random_forest(X_train, y_train)

    # Models and their paths
    models = {
        "Original KNN": "models/original_knn_model.pkl",
        "Optimized KNN": "models/optimized_knn_model.pkl",
        "Logistic Regression": "models/optimized_logistic_regression.pkl",
        "Random Forest": "models/optimized_rf_model.pkl",
    }

    # Evaluate each model
    results = []
    for model_name, model_path in models.items():
        # Perform prediction
        predictions = predict(model_path, X_test)

        # Compute metrics
        accuracy = accuracy_score(y_test, predictions)
        recall = recall_score(y_test, predictions)

        # Append results
        results.append(f"{model_name}: Accuracy={accuracy:.4f}, Recall={recall:.4f}")
        print(f"{model_name} - Accuracy: {accuracy:.4f}, Recall: {recall:.4f}")

    # Save results to evaluation/summary.txt
    with open("evaluation/summary_cus.txt", "w") as file:
        file.write("\n".join(results))
    print("Evaluation results saved to 'evaluation/_cus.txt'.")

if __name__ == "__main__":
    # Split data
    split_data("data_processed/Processed_Capital_Project_Schedules_and_Budgets.csv")

    # Train models and evaluate
    evaluate_models()
