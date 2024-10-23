import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the processed dataset
data = pd.read_csv('data_processed/Capital_Project_Schedules_and_Budgets_cleaned.csv')


# Generate summary statistics and visualizations
def visualize_data(data):
    # Clean column names to remove extra spaces
    data.columns = data.columns.str.strip()

    # Convert numeric columns to appropriate data types
    numeric_cols = ['Project Budget Amount', 'Final Estimate of Actual Costs Through End of Phase Amount',
                    'Total Phase Actual Spending Amount']
    for col in numeric_cols:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors='coerce')

    # Drop rows with non-numeric values in numeric columns
    data.dropna(subset=numeric_cols, inplace=True)

    # Filter out zero values
    if all(col in data.columns for col in numeric_cols):
        data = data[(data['Project Budget Amount'] > 0) &
                    (data['Final Estimate of Actual Costs Through End of Phase Amount'] > 0) &
                    (data['Total Phase Actual Spending Amount'] > 0)]
    else:
        print("Error: One or more required columns not found in the dataset.")
        return

    # Remove extreme outliers using IQR
    for col in numeric_cols:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        data = data[(data[col] >= (Q1 - 1.5 * IQR)) & (data[col] <= (Q3 + 1.5 * IQR))]

    # Summary statistics for quantitative features
    summary_quantitative = data[numeric_cols].agg(['min', 'max', 'median'])

    # Summary statistics for qualitative features
    qualitative_cols = ['Project Geographic District', 'Project Phase Name']
    summary_qualitative = {}
    for col in qualitative_cols:
        if col in data.columns:
            unique_values = data[col].value_counts()
            summary_qualitative[col] = {
                'Number of Categories': len(unique_values),
                'Most Frequent': unique_values.idxmax(),
                'Least Frequent': unique_values.idxmin()
            }

    # Write summary statistics to summary.txt
    with open('data_processed/summary.txt', 'w') as f:
        f.write("Summary Statistics for Quantitative Features:\n")
        f.write(summary_quantitative.to_string())
        f.write("\n\nSummary Statistics for Qualitative Features:\n")
        for col, stats in summary_qualitative.items():
            f.write(f"{col}:\n")
            f.write(f"  Number of Categories: {stats['Number of Categories']}\n")
            f.write(f"  Most Frequent: {stats['Most Frequent']}\n")
            f.write(f"  Least Frequent: {stats['Least Frequent']}\n\n")

    # Correlation matrix
    correlation_matrix = data[numeric_cols].corr()
    with open('data_processed/correlations.txt', 'w') as f:
        f.write(correlation_matrix.to_string())

    # Histogram for Project Budget
    plt.figure(figsize=(8, 6))
    data['Project Budget Amount'].plot(kind='hist', bins=30, edgecolor='black')
    plt.xlabel('Project Budget Amount')
    plt.title('Budget Distribution')
    plt.tight_layout()
    plt.savefig('visuals/budget_distribution.png')
    plt.show()

    # Scatter plot for Spending vs. Budget
    if 'Total Phase Actual Spending Amount' in data.columns:
        plt.figure(figsize=(8, 6))
        plt.scatter(data['Project Budget Amount'], data['Total Phase Actual Spending Amount'], alpha=0.6)
        plt.xlabel('Project Budget Amount')
        plt.ylabel('Total Phase Spending')
        plt.title('Budget vs. Spending')
        plt.tight_layout()
        plt.savefig('visuals/budget_vs_spending.png')
        plt.show()

    # Scatter plots for all pairs of quantitative features
    pairs = [(numeric_cols[i], numeric_cols[j]) for i in range(len(numeric_cols)) for j in
             range(i + 1, len(numeric_cols))]
    for col_x, col_y in pairs:
        plt.figure(figsize=(8, 6))
        plt.scatter(data[col_x], data[col_y], alpha=0.6)
        plt.xlabel(col_x)
        plt.ylabel(col_y)
        plt.title(f'{col_x} vs. {col_y}')
        plt.tight_layout()
        plt.savefig(f'visuals/{col_x}_vs_{col_y}.png')
        plt.show()

    # Histogram for qualitative features
    for col in qualitative_cols:
        if col in data.columns:
            plt.figure(figsize=(10, 6))
            data[col].value_counts().plot(kind='bar', edgecolor='black')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.title(f'{col} Distribution')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(f'visuals/{col}_distribution.png')
            plt.show()


if __name__ == "__main__":
    visualize_data(data)
