import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import numpy as np


def train_original_knn(X_train, y_train):
    """Train the original KNN model."""
    knn_model = KNeighborsClassifier(n_neighbors=5)
    knn_model.fit(X_train, y_train)
    with open("models/original_knn_model.pkl", "wb") as file:
        pickle.dump(knn_model, file)
    print("Original KNN model trained and saved to 'models/original_knn_model.pkl'.")


def train_optimized_knn(X_train, y_train):
    """Train the optimized KNN model using GridSearchCV."""
    param_grid = {
        'n_neighbors': np.arange(1, 21),
        'weights': ['uniform', 'distance'],
        'metric': ['euclidean', 'manhattan', 'chebyshev']
    }
    grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5, scoring='recall', n_jobs=-1, verbose=1)
    grid_search.fit(X_train, y_train)
    best_knn_model = grid_search.best_estimator_
    with open("models/optimized_knn_model.pkl", "wb") as file:
        pickle.dump(best_knn_model, file)
    print(f"Optimized KNN model trained and saved to 'models/optimized_knn_model.pkl'. Best parameters: {grid_search.best_params_}")


def train_logistic_regression(X_train, y_train):
    """Train the Logistic Regression model using GridSearchCV."""
    param_grid = {'C': [0.01, 0.1, 1, 10, 100], 'penalty': ['l1', 'l2']}
    grid_search = GridSearchCV(
        LogisticRegression(max_iter=1000, solver='liblinear', random_state=42), param_grid, cv=5, scoring='recall', verbose=1
    )
    grid_search.fit(X_train, y_train)
    best_log_reg_model = grid_search.best_estimator_
    with open("models/optimized_logistic_regression.pkl", "wb") as file:
        pickle.dump(best_log_reg_model, file)
    print(f"Optimized Logistic Regression model trained and saved to 'models/optimized_logistic_regression.pkl'. Best parameters: {grid_search.best_params_}")


def train_random_forest(X_train, y_train):
    """Train the Random Forest model using GridSearchCV."""
    param_grid = {
        "n_estimators": [100, 200, 300],
        "max_depth": [None, 10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4]
    }
    grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, scoring="recall", verbose=2, n_jobs=-1)
    grid_search.fit(X_train, y_train)
    best_rf_model = grid_search.best_estimator_
    with open("models/optimized_rf_model.pkl", "wb") as file:
        pickle.dump(best_rf_model, file)
    print(f"Optimized Random Forest model trained and saved to 'models/optimized_rf_model.pkl'. Best parameters: {grid_search.best_params_}")


if __name__ == "__main__":
    # Load training data
    X_train = pd.read_csv("data_processed/training_data.csv")
    y_train = pd.read_csv("data_processed/training_labels.csv")["Cost Overrun"]

    # Train and save models
    train_original_knn(X_train, y_train)
    train_optimized_knn(X_train, y_train)
    train_logistic_regression(X_train, y_train)
    train_random_forest(X_train, y_train)
    print("All models have been trained and saved.")
