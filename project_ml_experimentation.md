#### SERX94: Experimentation
#### TODO (title) Predictive Analysis of Cost Overruns in Engineering and Construction Projects
#### TODO (author) Zhiguo Ren
#### TODO (date) Nov 25.2024


## Explainable Records
### Record 1
**Raw Data:** 1	M015	P.S. 15 - MANHATTAN	SCA CIP	PLANYC BOILER CONVERSION / PLANYC CLIMATE CONTROL	Scope	Complete	6/18/2019	11/19/2019	8/30/2019	76269	109497	109497	DSF0000798463, DSF0000912540

Prediction Explanation:** This project is in the "Scope" phase, which typically involves a high degree of uncertainty as it deals with defining project boundaries and initial requirements. Projects in this phase are prone to overruns due to evolving scopes and unclear expectations. Additionally, the project type, "SCA CIP," often involves infrastructure-related tasks that are complex and can encounter unexpected delays. Combined with a relatively modest budget allocation, this project’s characteristics suggest a higher likelihood of challenges that could lead to overruns.

### Record 2
**Raw Data:** 2	M011	P.S. 11 - MANHATTAN	SCA CIP	ACCESSIBILITY / EXTERIOR MASONRY / PARAPETS / ROOF REPLACEMENT	Construction	Complete	4/4/2019	4/2/2021	12/18/2023	34149645	39016607	30644621	DSF0000844750, DSF0000853806, DSF0000874870, DSF0000960578

Prediction Explanation:** This project is in the "Construction" phase, which is generally more predictable as it involves executing well-defined plans, reducing the likelihood of overruns. The "SCA CIP" project type, while complex, is mitigated here by the structured nature of this phase. Moreover, with substantial budget allocation, this project benefits from sufficient resources to address potential risks, making it less prone to overruns. The combination of these factors suggests better control and stability during execution.

## Interesting Features
### Feature A
**Feature:** Project Phase Name

**Justification:** The "Project Phase Name" is crucial because different project phases inherently involve varying levels of complexity, risk, and cost uncertainty. For example:

Phases like "scope" (initial stages of a construction project) are associated with high unpredictability, coordination challenges, and dependency risks, leading to higher overrun rates (e.g., over 50%). 
In contrast, phases like "Construction" tend to be more structured and better defined, resulting in lower overrun probabilities (e.g., less than 5%). This feature strongly influences the model as it encapsulates the domain knowledge that different project stages inherently involve different risk profiles, directly impacting the likelihood of cost overruns.

### Feature B
**Feature:** Project Budget Amount

**Justification:** The "Project Budget Amount" is critical because it reflects the scale and resources allocated to a project. From the data:
Smaller budgets (e.g., $0–100K) often lead to higher probabilities of overrun (~40%), as these projects may lack contingency resources or economies of scale.
Larger budgets (e.g., $1M–5M) are typically associated with lower overrun probabilities (~21%), as they allow for better resource allocation and risk management. This feature significantly impacts the model because it captures the relationship between project size and financial resilience.

## Experiments 
### Varying A - Project Phase Name
**Prediction Trend Seen:** "Project Phase Name" was varied while keeping other features constant. Phases like Scope, Design, and Construction were analyzed. Early phases such as Scope tend to have higher risks due to incomplete information and uncertainties, while later phases like Construction are typically more stable. The model's predictions align with the trend that earlier phases are more prone to overruns, confirming the significance of this feature in risk prediction.

### Varying B - Project Budget Amount
**Prediction Trend Seen:** "Project Budget Amount" was varied across ranges from small to large budgets. Smaller-budget projects generally show higher risks of overruns due to limited resources and uncertainties, while larger budgets tend to reflect better planning and control. The model predictions highlight a clear trend of decreasing overrun risks as project budgets increase, emphasizing the importance of this feature.

### Varying A and B together
**Prediction Trend Seen:** The interaction between "Project Phase Name" and "Project Budget Amount" was analyzed. Aligned scenarios, such as larger budgets during stable phases like Construction, indicate low overrun risks. Misaligned cases, such as small budgets in uncertain phases like Scope, lead to higher risks. These trends validate the combined importance of these features in predicting project overruns.