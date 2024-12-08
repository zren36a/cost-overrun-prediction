#### SERX94: Machine Learning Evaluation
#### TODO (title) Predictive Analysis of Cost Overruns in Engineering and Construction Projects
#### TODO (author) Zhiguo Ren
#### TODO (date) Nov 25.2024

## Evaluation Metrics
### Metric 1
**Name:** Accuracy

**Choice Justification:** Accuracy measures the proportion of correctly classified instances over the total instances, which is crucial in understanding the overall effectiveness of the models for our data.

Interpretation:** The higher the accuracy, the better the model is at general classification.

### Metric 2
**Name:** Recall

**Choice Justification:** Recall measures the proportion of actual positives correctly identified by the model, which is critical for our use case to minimize false negatives in project cost overruns.

Interpretation:** A high recall indicates that the model effectively captures the majority of positive cases.

## Alternative Models
### Alternative 1:Optimized KNN
**Construction:** The KNN model was optimized by fine-tuning hyperparameters such as the number of neighbors (n_neighbors), distance metric (metric), and weight type (weights) using cross-validation.

**Evaluation:** 0.7404, Recall: 0.5018

### Alternative 2: Logistic Regression
**Construction:** Logistic Regression was optimized by fine-tuning hyperparameters such as the regularization strength (C) and penalty type (penalty) using cross-validation.

**Evaluation:** 0.7644, Recall: 0.5230

### Alternative 3: Random Forest
**Construction:** The Random Forest model was optimized by fine-tuning parameters such as the number of estimators (n_estimators), maximum tree depth (max_depth), minimum samples per leaf (min_samples_leaf), and minimum samples for a split (min_samples_split) using cross-validation.

**Evaluation:** 0.7519, Recall: 0.4700


## Best Model

**Model:** Logistic Regression
**Reason:** Compared to other models' performance, Logistic Regression achieves the best balance between accuracy (0.7644) and recall (0.5230), making it the most suitable model for our problem.

## Improved Metrics with Custom Normalization Methods 
To enhance model performance, a custom normalization method was explored. This method mapped categorical features to numeric values based on their correlation with cost overruns and binned numerical features into predefined ranges. By running the Python file of "wf_ml_evaluation_cus.py", which was coded with custom normalization method, we get: 

Original KNN - Accuracy: 0.7261, Recall: 0.6678
Optimized KNN - Accuracy: 0.7079, Recall: 0.5866
Logistic Regression - Accuracy: 0.7816, Recall: 0.4346
Random Forest - Accuracy: 0.7778, Recall: 0.5053

We can see that the Original KNN outperformed with improved recall (66.78%). The custom normalization approach proved effective in aligning features with the domain-specific context.
