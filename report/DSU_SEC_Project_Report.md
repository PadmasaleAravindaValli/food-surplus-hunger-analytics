# SEC PROJECT REPORT
## "Food Wastage vs Hunger Index Dashboard using Power BI & Tableau"

---

### DAYANANDA SAGAR UNIVERSITY
**DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING (DATA SCIENCE)**  
**SCHOOL OF ENGINEERING, HAROHALLI, KANAKAPURA ROAD – 562112**  
**ACADEMIC YEAR: 2025–26**

**BACHELOR OF TECHNOLOGY IN COMPUTER SCIENCE ENGINEERING [DATA SCIENCE]**

**Submitted by:**
- **Aravinda Valli** — `ENG23DS0077`
- **Vaishnavi T P** — `ENG23DS0089`
- **Varshini B** — `ENG23DS0090`
- **Yamini Pujar** — `ENG23DS0093`

**Under the Supervision of:**
- **Prof. Shashank Shekhar**, Assistant Professor, Department of CSE (Data Science), DSU
- **Prof. Manjula M**, Assistant Professor, Department of CSE (Data Science), DSU

---

## CERTIFICATE

This is to certify that the mini project work entitled **"Food Wastage vs Hunger Index Dashboard using Power BI & Tableau"** has been carried out at **Dayananda Sagar University, Bangalore**, by **P Aravinda Valli (ENG23DS0077)**, **Vaishnavi T P (ENG23DS0089)**, **Varshini B (ENG23DS0090)**, and **Yamini Pujar (ENG23DS0093)**, bonafide students of Fifth Semester, B.Tech in partial fulfillment for the award of degree of **Bachelor of Technology in Computer Science & Engineering (Data Science)** during the academic year 2025–26. It is certified that all corrections/suggestions indicated for Internal Assessment have been incorporated in the report deposited in departmental library.

```
____________________________                    ____________________________
 Signature of Guide                              Signature of Chairperson
 Prof. Shashank Shekhar / Prof. Manjula M        Dr. Shaila S G
 Assistant Professor, Dept of CSE (DS)           Chairperson, Dept of CSE (DS)
```

---

## ACKNOWLEDGEMENT

A project's successful completion offers a sense of satisfaction, but it is never finished without expressing gratitude to everyone who contributed to its accomplishment. We would like to convey our sincere gratitude to our esteemed university, **Dayananda Sagar University**, for offering first-rate facilities.

We are especially thankful to our Chairperson, **Dr. Shaila S G**, for providing necessary departmental facilities, moral support, and encouragement. The largest measure of our acknowledgment is reserved for **Prof. Shashank Shekhar** (Assistant Professor) and **Prof. Manjula M** (Assistant Professor), whose guidance and support made it possible to complete the project work in a timely manner.

We would also like to thank everyone who has assisted us in successfully completing this project work, both directly and indirectly.

- **Aravinda Valli** (ENG23DS0077)
- **Vaishnavi T P** (ENG23DS0089)
- **Varshini B** (ENG23DS0090)
- **Yamini Pujar** (ENG23DS0093)

---

## TABLE OF CONTENTS

| Chapter No. | Chapter Title | Page No. |
|:---:|:---|:---:|
| 1 | Abstract | 5 |
| 2 | Introduction | 6 |
| 3 | Objectives & Scope of Work | 7 |
| 4 | Dataset Description | 8 |
| 5 | Description of Work | 9 |
| 6 | Methodology | 10–12 |
| 7 | Dashboard Outputs & Visual Analysis | 13–16 |
| 8 | Results & Insights | 17 |
| 9 | Conclusion | 18 |
| 10 | References | 19 |

---

## 1. ABSTRACT

Food wastage and hunger are global issues that sit on opposite ends of humanity’s food cycle, yet they coexist in an alarming way. While some countries discard millions of tons of edible food every year, others continue to struggle with high hunger levels and malnutrition. 

This project brings both realities onto the same canvas by analyzing their relationship through interactive dashboards built using **Power BI** and **Tableau**. Two Kaggle datasets—one containing **Global Hunger Index (GHI)** scores and the other representing **global food wastage statistics**—were cleaned, transformed in Power Query, and visually explored. 

The dashboards present trends, country-wise comparisons, economic losses, category breakdowns, and geographical distributions. By transforming raw datasets into meaningful visual insights, this project highlights the severe imbalance between food production, consumption, and waste, emphasizing that the global food crisis is primarily a distribution and logistical challenge rather than a production deficit.

---

## 2. INTRODUCTION

The contrast between food surplus and food scarcity has remained one of the most contradictory global challenges of the 21st century. On one side of the world, supermarkets, hotels, and households discard vast amounts of food daily. On the other side, millions experience chronic hunger, nutritional deficiencies, and food insecurity. This stark gap raises a fundamental question: **"Is the world truly short of food, or is it inefficiently utilized?"**

This project focuses on studying the relationship between the Global Hunger Index and worldwide food wastage levels. By combining data analytics and visualization tools, the goal is to understand global patterns, compare country-wise statistics, and observe whether food wastage trends align with hunger severity. 

**Power BI** and **Tableau** were chosen because they provide strong capabilities for interactive visual analytics, making it easier to compare multi-dimensional data across temporal and spatial planes. The study helps build awareness about global food inequality and encourages sustainable consumption aligned with UN Sustainable Development Goals (SDG 2: Zero Hunger and SDG 12: Responsible Consumption and Production).

---

## 3. OBJECTIVES & SCOPE OF WORK

### Objectives:
1. To visually analyze global hunger levels and food waste patterns using real-world empirical datasets.
2. To identify countries with extreme hunger severity and compare them with countries generating the most food waste.
3. To examine temporal trends over multiple years (2018–2024) by observing changes in hunger index values and total food wastage.
4. To build well-structured, interactive dashboards using both **Power BI** and **Tableau** for comparative evaluation and cross-platform validation.
5. To generate quantitative insights that can support public policy, humanitarian logistics, and sustainability initiatives.

### Scope:
The project encompasses:
- Dataset acquisition from Kaggle repositories.
- Data ingestion, cleaning, deduplication, schema standardization, and feature engineering in **Power Query**.
- Comparative visualization across Power BI Desktop and Tableau Desktop / Public.
- Interpretation of key patterns, ratios, and economic losses.
- *Out of Scope*: Predictive machine learning algorithms and real-time streaming telemetry. The focus is placed entirely on descriptive, diagnostic, and visual data analytics.

---

## 4. DATASET DESCRIPTION

Two primary datasets were retrieved from Kaggle for this study:

### 1) Global Hunger Index (GHI) Dataset
- Contains country-wise hunger index values recorded over multiple survey periods.
- **Fields**: `Country` / `Entity`, `Year`, `Global Hunger Index Score`, `Index Category` (Low, Moderate, Serious, Alarming, Extremely Alarming).
- **Application**: Identifies geographical hunger hotspots and tracks historical alleviation progress.

### 2) Global Food Wastage Dataset
- Contains national-level food waste metrics, per capita disposal, and financial losses.
- **Fields**: `Country`, `Total Waste (Tons)`, `Waste Per Capita (Kg)`, `Economic Loss (in Million Dollars)`, `Food Category` (Prepared Food, Bakery, Dairy, Fruits & Vegetables, etc.).
- **Application**: Quantifies domestic, commercial, and agricultural food waste tonnage and financial ramifications.

---

## 5. DESCRIPTION OF WORK

The project was executed through an iterative lifecycle:
1. **Data Acquisition**: Extracted raw CSV files from Kaggle.
2. **Power Query Preprocessing**: Handled inconsistent country naming (e.g., standardizing `USA`), dropped records with null indicators, validated numeric data boundaries, and eliminated redundant attributes.
3. **Feature Engineering**: Formulated `Waste in Millions of Tons`, `Waste Per Capita (Kg)`, `Economic Loss ($M)`, and `Hunger-to-Waste Ratio`.
4. **Power BI Development**: Built clustered bar charts, dual KPI cards, multi-slice interactive donut charts, Bing dark satellite maps, dual-axis temporal trend lines, and scatter plots.
5. **Tableau Development**: Implemented multi-metric bar charts, rose-colored horizontal distributions, 8-category pie charts, bullet graphs with target reference bands, entity hunger bar charts, and a world choropleth map.
6. **Synthesis & Evaluation**: Synthesized insights confirming the decoupling of food waste from regional hunger.

---

## 6. METHODOLOGY & DATA CLEANING PIPELINE

```
+------------------------------+     +-------------------------------+
| Kaggle Global Hunger Index   |     | Kaggle Global Food Wastage    |
| (Country, Year, GHI, Cat)    |     | (Country, Waste, Econ Loss)   |
+--------------+---------------+     +---------------+---------------+
               |                                     |
               +------------------+------------------+
                                  |
                                  v
                +------------------------------------+
                | Power Query Ingestion & Cleaning   |
                | - Distinct rows (drop duplicates)  |
                | - Strip whitespace & standardize   |
                | - Cast data types (Numbers, Text)  |
                | - Filter nulls & impossible values |
                +-----------------+------------------+
                                  |
                                  v
                +------------------------------------+
                | Feature Engineering & Join         |
                | - Inner join on [Country]          |
                | - Hunger-to-Waste Ratio            |
                | - Waste Per Capita (Kg)            |
                | - Economic Loss ($M)               |
                +-----------------+------------------+
                                  |
                   +--------------+--------------+
                   |                             |
                   v                             v
     +---------------------------+ +---------------------------+
     | Power BI Report Pages     | | Tableau Worksheets        |
     | - Page 1: Overview & Donut| | - Dash 1: Breakdown & Bul|
     | - Page 2: Satellite Map   | | - Dash 2: Hunger Patterns |
     | - Page 3: Trends & Scatter| | - Dash 3: Choropleth Map  |
     +---------------------------+ +---------------------------+
```

### Key Transformations in Power Query:
1. **Deduplication**: `Table.Distinct(Source)` removed all redundant country logs.
2. **Name Normalization**: Standardized naming disparities (`"United States"` -> `"USA"`, `"United Kingdom"` -> `"UK"`).
3. **Type Coercion**: Enforced `Int64.Type` on years, `type number` on GHI scores, tonnages, and economic losses.
4. **Null Imputation & Rejection**: Discarded records missing key GHI or waste totals to guarantee analytical integrity.
5. **Inner Join**: Linked both domains on `[Country]` to yield a unified fact table of 20+ benchmark nations.

---

## 7. DASHBOARD OUTPUTS & VISUAL ANALYSIS

### Power BI Dashboard Suite:
1. **Page 1: Top 10 Hunger & Donut Distribution**
   - **Top 10 Countries by Hunger Index**: Vertical bars in Royal Purple (`#543884`). India leads with `33.2`, followed by Indonesia (`24.1`), Ethiopia (`20.5`), and South Africa (`15.4`).
   - **KPI Card 1**: Shows `$1.37M` for selected top waste nation (Italy).
   - **KPI Card 2**: Shows `$17.80M` total cumulative economic loss.
   - **Donut Chart**: Multi-colored donut illustrating waste share: Italy (`7.61%`), Canada (`6.84%`), Spain (`6.22%`), France (`6.04%`), Argentina (`5.91%`), Mexico (`5.87%`), South Africa (`5.48%`), USA (`5.35%`), Australia (`5.07%`), Russia (`4.68%`).

2. **Page 2: Satellite Map Visualization**
   - Renders dark earth satellite geography with blue bubble circles proportional to waste generation. Highlights immense waste density across North America and Europe compared to Africa and South Asia.

3. **Page 3: Trend Lines & Correlation**
   - **Header**: Navy bar titled `FOOD WASTAGE Vs HUNGER INDEX`.
   - **Trend Line Over Years**: Dual-axis line graph comparing `Sum of Sum of Total Waste` (Red `#E63946`) and `Avg Hunger Index` (Navy Blue `#1E3A8A`) from 2018 to 2024.
   - **Top 10 Countries By Food Waste**: Clustered column chart in Slate Blue (`#4361EE`).
   - **Food Waste Vs Hunger Scatter Plot**: Red marker scatter plot showing high waste per capita (> 2,000 kg) clustering with low hunger (< 10), and high hunger clustering with low/moderate waste.

### Tableau Dashboard Suite:
1. **Dashboard 1: Breakdown & Bullet Graph**
   - Country waste comparison (5.8M to 6.8M tons), Rose horizontal bar graph, 8-category food waste pie chart (Prepared Food: 711, Bakery: 630, Beverages: 639, Dairy: 616, Fruits & Veg: 620, Meat: 605, Grains: 583, Frozen: 506), and Bullet graph with distribution bands.
2. **Dashboard 2: Global Hunger Patterns**
   - Horizontal bar chart of entities in sequential blue gradients (Angola: 165, Afghanistan: 157, Burkina Faso: 135) and historical multi-year line trajectory.
3. **Dashboard 3: World Choropleth Map**
   - Shaded world map with salmon-red color ramp (`6M` to `7M` tons). Displays hover tooltips: Canada (6,790,678), USA (6,446,335), Mexico (6,589,170), Brazil (6,391,753), China (6,411,096), Russia (5,832,689), Australia (5,887,361).

---

## 8. RESULTS & KEY INSIGHTS

1. **Surplus-Scarcity Decoupling**: High food waste does **not** correlate with high hunger index values. Wealthy, industrialized nations discard the greatest food volumes, yet have the lowest hunger scores.
2. **Geographical Asymmetry**: Severe hunger is concentrated within sub-Saharan Africa and South Asia, driven by supply chain vulnerabilities, climate volatility, and infrastructural bottlenecks.
3. **Economic Toll**: Food waste results in over **$17.80 Million** in deadweight financial losses among the evaluated sample.
4. **Perishability Drivers**: Prepared meals, bakery products, and beverages suffer the highest disposal frequencies due to short retail shelf-life and household over-purchasing.

---

## 9. CONCLUSION

This project effectively integrates empirical hunger scores and food waste datasets using **Power BI** and **Tableau**. The comparative visualizations prove conclusively that global hunger is not caused by an aggregate global food deficit, but rather by catastrophic failures in food logistics, preservation, and equitable distribution. 

Through visual analytics, the study underscores the urgency for targeted food redistribution programs, cold-chain infrastructure investments in developing nations, and strict food recovery regulations in high-waste economies.

---

## 10. REFERENCES

1. Whenamancodes. *The Global Hunger Index dataset*. Kaggle.  
   https://www.kaggle.com/datasets/whenamancodes/the-global-hunger-index
2. Soundankar, A. *Global Food Wastage dataset*. Kaggle.  
   https://www.kaggle.com/code/atharvasoundankar/global-food-wastage
3. Global Hunger Index. *GHI Official Methodology & Reports*.  
   https://www.globalhungerindex.org/
4. Microsoft. *Power BI Desktop & Power Query Documentation*.  
   https://learn.microsoft.com/power-bi/
5. Tableau Software. *Tableau Desktop and Public Documentation*.  
   https://help.tableau.com/current/public/desktop/en-us/public.htm
6. Food and Agriculture Organization (FAO). *The State of Food Security and Nutrition in the World*.  
   https://www.fao.org/food-loss-and-food-waste/en/
7. World Bank. *Global Food Security Indicators and Open Data*.  
   https://www.worldbank.org/en/topic/food-security
