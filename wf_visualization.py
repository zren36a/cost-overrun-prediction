import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the processed dataset
data = pd.read_csv('data_processed/Processed_1_Capital_Project_Schedules_and_Budgets.csv')

# Generate summary statistics and visualizations # 1
def visualize_data_1(data):
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

#visualizations # 2
def visualize_data_2():


    # Define file paths
    processed_file_path = "data_processed/Processed_2_Capital_Project_Schedules_and_Budgets.csv"
    visuals_dir = "visuals/"
    output_dir = "data_processed/"

    # Load the processed CSV file
    df = pd.read_csv(processed_file_path)
    df.columns = df.columns.str.strip()

    # Filter for valid rows
    valid_data = df[df["Valid Row"] == True].copy()

    # --------------------------------------
    # 1. Plot for Project Phase Name Analysis
    # --------------------------------------
    phase_analysis = valid_data.groupby("Project Phase Name").agg(
        Total_Frequency=("Project Phase Name", "size"),
        Overrun_Frequency=("Cost Overrun", "sum")
    ).reset_index()

    phase_analysis["Overrun Rate (%)"] = (
                phase_analysis["Overrun_Frequency"] / phase_analysis["Total_Frequency"] * 100).round(2)
    phase_analysis = phase_analysis.sort_values(by="Overrun Rate (%)", ascending=False).reset_index(drop=True)

    # Save to Excel
    #phase_output_file = output_dir + "Phase_Name_Overrun_Analysis.xlsx"
    #phase_analysis.to_excel(phase_output_file, index=False)

    # Plot
    plt.figure(figsize=(10, 6))
    bars = plt.bar(phase_analysis["Project Phase Name"], phase_analysis["Overrun Rate (%)"], color='skyblue')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, f'{yval:.2f}%', ha='center', va='bottom')
    plt.title("Trend of Overrun Rate vs. Project Phase")
    plt.xlabel("Project Phase Name")
    plt.ylabel("Overrun Rate (%)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig(visuals_dir + "Phase_Name_Overrun_Bar_Chart.png")
    plt.show()

    # --------------------------------------
    # 2. Plot for Project Type Analysis
    # --------------------------------------
    type_analysis = valid_data.groupby("Project Type").agg(
        Total_Frequency=("Project Type", "size"),
        Overrun_Frequency=("Cost Overrun", "sum")
    ).reset_index()

    type_analysis["Overrun Rate (%)"] = (
                type_analysis["Overrun_Frequency"] / type_analysis["Total_Frequency"] * 100).round(2)
    type_analysis = type_analysis.sort_values(by="Overrun Rate (%)", ascending=False).reset_index(drop=True)

    # Save to Excel
    #type_output_file = output_dir + "Project_Type_Overrun_Analysis.xlsx"
    #type_analysis.to_excel(type_output_file, index=False)

    # Plot
    plt.figure(figsize=(10, 6))
    bars = plt.bar(type_analysis["Project Type"], type_analysis["Overrun Rate (%)"], color='skyblue')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, f'{yval:.2f}%', ha='center', va='bottom')
    plt.title("Overrun Rate by Project Type")
    plt.xlabel("Project Type")
    plt.ylabel("Overrun Rate (%)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig(visuals_dir + "Project_Type_Overrun_Bar_Chart.png")
    plt.show()

    # --------------------------------------
    # 3. Plot for Budget Overrun Analysis
    # --------------------------------------
    valid_data["Project Budget Amount"] = pd.to_numeric(valid_data["Project Budget Amount"], errors="coerce")

    bin_edges = [0, 100000, 200000, 500000, 1000000, 5000000, 10000000, float("inf")]
    bin_labels = ["0-100K", "100K-200K", "200K-500K", "500K-1M", "1M-5M", "5M-10M", "10M+"]
    valid_data["Budget Bin"] = pd.cut(valid_data["Project Budget Amount"], bins=bin_edges, labels=bin_labels,
                                      right=False)

    trend_analysis = valid_data.groupby("Budget Bin", observed=False).agg(
        Total_Projects=("Budget Bin", "size"),
        Overrun_Projects=("Cost Overrun", "sum")
    ).reset_index()

    trend_analysis["Probability of Overrun(%)"] = (
                trend_analysis["Overrun_Projects"] / trend_analysis["Total_Projects"] * 100).round(2)

    # Save to Excel
    #budget_output_file = output_dir + "Budget_Overrun_Analysis.xlsx"
    #trend_analysis.to_excel(budget_output_file, index=False)

    # Plot
    plt.figure(figsize=(10, 6))
    bars = plt.bar(trend_analysis["Budget Bin"], trend_analysis["Probability of Overrun(%)"], color='skyblue')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 1, f'{yval:.2f}%', ha='center', va='bottom')
    plt.title("Trend of Probability of Overrun vs. Project Budget Amount")
    plt.xlabel("Project Budget Amount (Binned)")
    plt.ylabel("Probability of Overrun (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig(visuals_dir + "Budget_Overrun_Bar_Chart.png")
    plt.show()

    # Code logic from plot.py goes here (omitted for brevity; include the full logic for plots)


if __name__ == "__main__":
    visualize_data_1(data)
    visualize_data_2()

