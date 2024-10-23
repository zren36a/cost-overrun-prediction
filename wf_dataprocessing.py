import pandas as pd

# Load the dataset for processing
data = pd.read_csv('data_original/Capital_Project_Schedules_and_Budgets.csv')

# Data cleaning and processing
def clean_data(data):
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
    return data

# Save the processed data
def save_processed_data(data):
    data.to_csv('data_processed/Capital_Project_Schedules_and_Budgets_cleaned.csv', index=False)

if __name__ == "__main__":
    cleaned_data = clean_data(data)
    save_processed_data(cleaned_data)
