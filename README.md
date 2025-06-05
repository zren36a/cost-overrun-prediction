# Cost Overrun Prediction in Construction Projects

This project applies predictive analytics and machine learning to forecast cost overruns in engineering and construction projects, with a focus on public school construction data from New York City (2024). The goal is to help project managers identify risk factors and improve cost control strategies.

## 📌 Project Highlights

- **Data Source**: NYC OpenData – School Construction Authority (14,000+ records)
- **Key Techniques**:
  - Exploratory Data Analysis (EDA)
  - Feature engineering: budget bins, project phase classification
  - Normalization (traditional vs. custom)
- **Models Used**:
  - Logistic Regression
  - Random Forest
  - K-Nearest Neighbors (KNN)
- **Best Performance**: Logistic Regression (Accuracy: 76.44%, Recall: 52.30%)

## 🔍 Key Insights

- **Higher risk of cost overruns** in early project phases (e.g., "Scope", "Design") and small-budget projects (< $200K)
- **Custom normalization methods** improved KNN recall to **66.78%**
- Project budget and phase were found to be the **most significant predictors**

## 📊 Visualizations Included

- Overrun probability vs. project budget
- Overrun rate across project phases
- Overrun risk by project type

## 💡 Motivation

Cost overruns are a persistent problem in the construction industry. This project demonstrates how machine learning can provide actionable insights for budget forecasting and risk mitigation in public infrastructure development.

## ⚙️ Tech Stack

- Python (Pandas, scikit-learn, Matplotlib)
- Jupyter Notebook
- Data preprocessing and EDA
- Model training and performance evaluation
