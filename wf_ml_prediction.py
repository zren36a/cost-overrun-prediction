import pickle
import pandas as pd


def load_model(model_path):
    """
    Load the trained model from the given path.

    Args:
        model_path (str): Path to the saved model file.

    Returns:
        model: The loaded model.
    """
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model


def predict(model_path, input_data):
    """
    Predict outputs based on the input data using the specified model.

    Args:
        model_path (str): Path to the saved model file.
        input_data (pd.DataFrame): Input data for prediction.

    Returns:
        pd.Series: Predicted outputs.
    """
    # Load the model
    model = load_model(model_path)

    # Predict the output
    predictions = model.predict(input_data)
    return pd.Series(predictions, name="Predictions")


if __name__ == "__main__":
    # Example usage
    # Load testing data
    test_data_path = "data_processed/testing_data.csv"
    X_test = pd.read_csv(test_data_path)

    # Specify the model path
    model_path = "models/knn_model.pkl"  # Replace with the desired model

    # Perform prediction
    predictions = predict(model_path, X_test)

    # Save predictions to a file
    predictions.to_csv("data_processed/test_predictions.csv", index=False)
    print(f"Predictions saved to 'data_processed/test_predictions.csv'.")
