import pandas as pd

# Load the dataset for processing
data = pd.read_csv('data_original/Capital_Project_Schedules_and_Budgets.csv')

# Data cleaning and processing
def data_pro_1(data):
    # Clean column names to remove extra spaces
    data.columns = data.columns.str.strip()

    # Check if 'Project Phase Name' column exists in the dataset
    if 'Project Phase Name' in data.columns:
        # Handle missing values
        data.ffill(inplace=True)  # Forward fill to handle missing data
        # Remove duplicates
        data.drop_duplicates(inplace=True)
        # Standardize categorical values
        data['Project Phase Name'] = data['Project Phase Name'].str.lower()
    else:
        print("Error: 'Project Phase Name' column not found in the dataset.")
    data.to_csv('data_processed/Processed_1_Capital_Project_Schedules_and_Budgets.csv', index=False)
    return data

def data_pro_2():

    # Load the dataset from a CSV file
    df = pd.read_csv(
        "data_original/Capital_Project_Schedules_and_Budgets.csv")  # Load the CSV file into a pandas DataFrame

    # Mark invalid rows
    # Convert relevant columns to numeric, marking non-numeric or invalid as NaN
    df["Project Budget Amount"] = pd.to_numeric(df["Project Budget Amount"], errors="coerce")
    df["Total Phase Actual Spending Amount"] = pd.to_numeric(df["Total Phase Actual Spending Amount"], errors="coerce")

    # Mark rows where date columns are invalid as NaN
    date_columns = ["Project Phase Actual Start Date", "Project Phase Planned End Date"]
    for col in date_columns:
        df[col] = pd.to_datetime(df[col],
                                 errors="coerce")  # Convert to datetime, invalid values will be NaT (Not a Time)

    # Create a new column to mark validity
    df["Valid Row"] = True  # Initialize all rows as valid

    # Identify invalid rows and mark them
    invalid_budget_or_spending = (df["Project Budget Amount"].isna() | (df["Project Budget Amount"] == 0)) | \
                                 (df["Total Phase Actual Spending Amount"].isna() | (
                                             df["Total Phase Actual Spending Amount"] == 0))
    invalid_dates = df[date_columns].isna().any(axis=1)  # Check if any of the date columns have invalid dates
    df.loc[invalid_budget_or_spending | invalid_dates, "Valid Row"] = False  # Mark rows as invalid

    # Proceed with valid rows for processing
    valid_data = df[df["Valid Row"]].copy()  # Filter for valid rows

    # Calculate overrun metrics for valid rows
    valid_data["Overrun Amount"] = valid_data["Total Phase Actual Spending Amount"] - valid_data[
        "Project Budget Amount"]
    valid_data["Overrun Percentage"] = (valid_data["Overrun Amount"] / valid_data["Project Budget Amount"]) * 100

    # Define the threshold and label rows
    threshold = 5  # Overrun percentage threshold
    valid_data["Cost Overrun"] = (valid_data["Overrun Percentage"] > threshold).astype(
        int)  # Label as 1 if overrun exceeds threshold

    # Retain the original dataset structure while including the new columns
    df["Overrun Amount"] = valid_data["Overrun Amount"]
    df["Overrun Percentage"] = valid_data["Overrun Percentage"]
    df["Cost Overrun"] = valid_data["Cost Overrun"]

    # Output the processed dataset with all columns
    processed_dataset = df.copy()  # Include all original columns plus new calculated columns

    # Save the processed dataset as a new CSV file
    processed_dataset.to_csv("data_processed/Processed_2_Capital_Project_Schedules_and_Budgets.csv",
                             index=False)  # Save to a new CSV file


if __name__ == "__main__":
    data_pro_1 = data_pro_1(data)
    data_pro_2()

