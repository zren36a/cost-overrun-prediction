import pandas as pd
import hashlib

# Load the original dataset
file_path = 'data_original/Capital_Project_Schedules_and_Budgets.csv'
data = pd.read_csv(file_path)

# Save the original data and generate MD5 hash
def save_original_data():
    data.to_csv(file_path, index=False)
    with open(file_path, 'rb') as f:
        md5_hash = hashlib.md5(f.read()).hexdigest()
        print("MD5 Hash of Original File:", md5_hash)

if __name__ == "__main__":
    save_original_data()