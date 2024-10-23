#### SERX94: Exploratory Data Munging and Visualization
#### title: Analysis of Capital Project Costs 
#### author: Zhiguo Ren
#### date: October 22,2024

## Basic Questions
**Dataset Author(s):** School Construction Authority (SCA), City of New York / NYC OpenData

**Dataset Construction Date:** August 22, 2013

**Dataset Record Count:** 14077

**Dataset Field Meanings:** 
Project Geographic District: District where building is located
Project Building Identifier: Building ID	
Project School Name: School name	
Project Type: Type of project based on funding 	
Project Description: Component(s) of work to be done	
Project Phase Name: Examples Scope , Design & Construction	
Project Status Name: Within the phase more detail, i.e. In-Progress, Hold	
Project Phase Actual Start Date:Date phase actually started date 
Project Phase Planned End Date: Date phase originally scheduled to be completed
Project Phase Actual End Date: Date phase actually completed 	
Project Budget Amount: Award base budget by phase
Final Estimate of Actual Costs Through End of Phase Amount: Current projected final estimate at completion of project by phase	
Total Phase Actual Spending Amount: Actual cumulative expenditures by phase	
DSF Number(s): Number used to identify project in Five Year Pan

**Dataset File Hash(es):** MD5 Hash of Original File: c20307ead7faaf04a5fcc422016111b2
**URL:** https://data.cityofnewyork.us/api/views/2xh6-psuq/rows.csv?accessType=DOWNLOAD

## Interpretable Records
### Record 1
**Raw Data:** 1	M034	P.S. 34 - MANHATTAN	SCA CIP	HEATING PLANT / FLOOD ELIMINATION / PARAPETS / EXTERIOR MASONRY / LOW VOLTAGE ELECTRICAL SYSTEM / CLIMATE CONTROL / ELECTRICAL SYSTEMS / WINDOWS / ROOFS	Construction	In-Progress	7/5/2022	12/20/2024		30857060	29055879	24667044	DSF0000992072, DSF0000897945, DSF0000897946, DSF0000897947, DSF0000943350, DSF0000960885, DSF0000960884, DSF0001008630, DSF0000992069

Interpretation:** This record represents a major renovation project at P.S. 34 in Manhattan, focusing on multiple aspects such as heating, flood elimination, electrical systems, climate control, windows, roofs, and masonry. The project is currently in the construction phase and is ongoing ("In-Progress"). It began on July 5, 2022, with an expected completion date of December 20, 2024. The project has a budget of $30,857,060, and the final estimated cost through the end of the phase is projected at $29,055,879. So far, $24,667,044 has been spent on the project. The record also includes multiple DSF numbers, which are identifiers for related construction tasks or components within the Capital Improvement Program.

### Record 2
**Raw Data:** 30	Q171	P.S. 171 - QUEENS	SCA CIP	EXTERIOR MASONRY / PARAPETS	Design	Complete	7/27/2021	12/29/2021	1/19/2022	175581	225260	215157	DSF0001023504, DSF0000997642

**Interpretation:** This record represents a project at P.S. 171 in Queens, focused on "Exterior Masonry" and "Parapets" under the Capital Improvement Program. The project phase was "Design," which has been marked as "Complete." The phase began on July 27, 2021, and was initially planned to be completed by December 29, 2021, but actually concluded on January 19, 2022. The original budget for this phase was $175,581, but the final estimated cost increased to $225,260. The actual spending for this phase came to $215,157. The DSF numbers listed (DSF0001023504, DSF0000997642) are unique identifiers for specific components or tasks related to the project.

## Background Domain Knowledge

The construction industry is critical to the global economy, but it is also complex and challenging to manage due to numerous factors affecting project success. One of the key challenges in construction project management is accurately estimating project costs, which significantly influences project performance. Effective cost estimation helps in planning, budgeting, and mitigating the risk of cost overruns, which are common issues in the industry due to uncertainties and the dynamic nature of construction projects.
Accurate cost estimation is crucial, especially during the early phases of construction projects. Research by Ali et al. highlights the importance of using artificial intelligence (AI) models to improve cost estimation. The study found that models like Random Forest (RF), Artificial Neural Networks (ANN), and Support Vector Machines (SVM) can significantly enhance prediction accuracy when combined with feature selection techniques like Extreme Gradient Boosting [1] .

In addition to AI's role in cost estimation, data science has broader applications in construction management. Bobriakov discusses several data science use cases, such as managing customer data and predictive analytics, which can be adapted for the construction sector to enhance project performance. Data science allows construction companies to analyze customer and project data, improving efficiency and helping managers make more informed decisions. For example, recommendation engines and real-time analytics can optimize resource allocation and project timelines, thus boosting overall project performance and customer satisfaction [2].

Moreover, a study on the economic implications of construction cost analysis emphasizes that accurate cost predictions are not only crucial for project success but also have a significant impact on broader economic outcomes. Cost overruns can lead to financial losses and disputes, which can harm not only individual projects but also the overall economy. Accurate estimation and effective cost management are therefore necessary for maintaining financial stability and ensuring the successful completion of construction projects [3].

[1] Ali, Z. H., Burhan, A. M., Kassim, M., & Al-Khafaji, Z. (2022). Developing an Integrative Data Intelligence Model for Construction Cost Estimation. Complexity, 2022, 1–18. https://doi.org/10.1155/2022/4285328
[2] Igor Bobriakov. (2019, October 18). Top 8 Data Science Use Cases in Support - ActiveWizards — AI & ML for startups - Medium. Medium; ActiveWizards — AI & ML for startups. https://medium.com/activewizards-machine-learning-company/top-8-data-science-use-cases-in-support-616da5500e85
[3] Stasiak-Betlejewska, R., & Potkány, M. (2015). Construction Costs Analysis and its Importance to the Economy. Procedia Economics and Finance, 34, 35–42. https://doi.org/10.1016/s2212-5671(15)01598-1

## Dataset Generality

The dataset used in this project is highly representative of real-world budget & cost in public infrastructure projects, particularly in school construction. It captures key cost-related features such as budget allocations, final estimates, and actual spending, providing a complete view of the financial aspects of each project. This variety of cost-related data enables a comprehensive analysis of budgeting accuracy, cost overruns, and spending efficiency—common challenges in real-world construction projects.

By including data across various project types, phases, and geographic locations, the dataset offers a generalized understanding of cost dynamics in school construction projects. The ability to analyze cost differences across different districts and phases allows for valuable insights into how financial planning and management impact the success of public projects. Moreover, patterns in budget versus actual spending provide a realistic representation of typical issues in public infrastructure, such as cost overruns or savings.

The broad coverage of project budgets and spending data, along with observed financial trends, ensures that the dataset is suitable for analyzing cost efficiency, understanding budget deviations, and identifying common factors leading to cost overruns. This generality makes the dataset a valuable resource for deriving data-driven insights to improve cost management in public construction projects.


## Data Transformations
### Transformation

**Description:** 
1.Data Cleaning: Missing values were forward filled, and rows with non-numeric or erroneous values were removed.
**Soundness Justification:** 
Forward fill maintained data continuity, and removing erroneous rows ensured data integrity.

**Description:** 
2. Standardization: Numeric columns were converted to a consistent numeric type.
**Soundness Justification:** 
Ensures compatibility and prevents errors during analysis, keeping data structure uniform.

**Description:** 
3. Removing Zeros: Rows with zero values in key columns were filtered out.
**Soundness Justification:** 
Zeros in budget or spending columns were unrealistic, so filtering improved accuracy.

**Description:** 
4. Column Name Cleaning: Extra spaces were removed from column names.
**Soundness Justification:** 
Prevents manipulation issues and improves reliability without affecting semantics.

**Description:** 
5. Qualitative Data Standardization: "Project Phase Name" values were standardized to lowercase.
**Soundness Justification:** 
Avoids duplication from case sensitivity, simplifying analysis.

## Visualizations

### Visual 1. Final Estimate of Actual Costs Through End of Phase Amount_vs_Total Phase Actual Spending Amount
**Analysis:** The scatter plot shows the relationship between "Final Estimate of Actual Costs Through End of Phase Amount" and "Total Phase Actual Spending Amount." The points align in a diagonal pattern, indicating a strong positive correlation between estimated and actual costs. This suggests that higher estimated costs generally result in higher actual spending. A few outliers above the main trend suggest deviations where spending significantly exceeded estimates, indicating potential cost overruns.

### Visual 2. Project Budget Amount_vs_Final Estimate of Actual Costs Through End of Phase Amount
**Analysis:** The scatter plot depicts the relationship between "Project Budget Amount" and "Final Estimate of Actual Costs Through End of Phase Amount." There is a noticeable upward trend, indicating a strong positive correlation between the budget and the final estimated costs. The closer alignment of points along the diagonal suggests that projects generally stick close to their budgeted amounts. However, there are some scattered points, especially for higher budget values, indicating variability in the estimation process or inconsistencies in spending, implying potential budgeting inaccuracies or unexpected cost fluctuations.

### Visual 3. Project Budget Amount_vs_Total Phase Actual Spending Amount
**Analysis:** The scatter plot shows the relationship between "Project Budget Amount" and "Total Phase Actual Spending Amount." The data points are widely spread, indicating that the actual spending varies significantly, even for projects with similar budget amounts. Unlike the previous plot that showed a strong alignment, this one suggests that actual spending is less consistently tied to the budget, with many points clustered in lower spending values regardless of budget size. This indicates potential underspending or high variation in project execution, highlighting the need for improved financial monitoring and control mechanisms to ensure budgets are effectively managed.

### Visual 4. Project Geographic District_distribution
**Analysis:** The histogram represents the distribution of projects across different geographic districts. District 31 has the highest number of projects, with over 250 occurrences, followed closely by Districts 2 and 27. There is a noticeable decline in frequency across the remaining districts, with Districts like 1 and 32 having relatively fewer projects. This uneven distribution may indicate varying investment or project demands across different regions, which could reflect regional priorities or the specific infrastructure needs of each district. Understanding this distribution can help in assessing resource allocation and identifying areas that may need additional support.

### Visual 5. Project Phase Name_distribution
**Analysis:** The histogram illustrates the distribution of project phases across different categories. The phases "design," "cm, f&e," and "scope" have the highest frequency, with each exceeding 1,200 occurrences. These phases are fundamental in the early stages of project planning, reflecting significant emphasis on design, construction management, and scoping activities. The "construction" phase has a lower frequency compared to the planning stages, suggesting that fewer projects have reached or are actively in the construction stage. Phases like "f&e," "cm," and "cm, art & f&e" have the least representation, indicating they are less common in the dataset, possibly representing niche or specialized tasks. The trend suggests that more effort is focused on the preparatory stages of the project lifecycle compared to execution and specialized phases.

