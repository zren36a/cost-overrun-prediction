import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from wf_ml_training import train_original_knn, train_optimized_knn, train_logistic_regression, train_random_forest
from wf_ml_prediction import predict
from sklearn.metrics import accuracy_score, recall_score
import os

# Ensure necessary directories exist
os.makedirs("data_processed", exist_ok=True)
os.makedirs("evaluation", exist_ok=True)


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
    X = data_valid[["Project Type", "Project Phase Name", "Project Budget Amount"]]
    y = data_valid["Cost Overrun"]

    # One-Hot Encode categorical features
    encoder = OneHotEncoder(handle_unknown="ignore")
    encoded_features = encoder.fit_transform(X[["Project Type", "Project Phase Name"]]).toarray()
    encoded_feature_names = encoder.get_feature_names_out(["Project Type", "Project Phase Name"])
    encoded_df = pd.DataFrame(encoded_features, columns=encoded_feature_names, index=X.index)

    # Normalize "Project Budget Amount"
    scaler = MinMaxScaler()
    X.loc[:, "Project Budget Amount"] = scaler.fit_transform(X[["Project Budget Amount"]])

    # Combine encoded and scaled features
    X = pd.concat([X.drop(["Project Type", "Project Phase Name"], axis=1), encoded_df], axis=1)

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
    with open("evaluation/summary.txt", "w") as file:
        file.write("\n".join(results))
    print("Evaluation results saved to 'evaluation/summary.txt'.")


if __name__ == "__main__":
    # Split data
    split_data("data_processed/Processed_Capital_Project_Schedules_and_Budgets.csv")

    # Train models and evaluate
    evaluate_models()
