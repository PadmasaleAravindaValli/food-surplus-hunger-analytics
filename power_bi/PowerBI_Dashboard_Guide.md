# Power BI Implementation Guide: Food Wastage vs Hunger Index

**Department of Computer Science & Engineering (Data Science)**  
**Dayananda Sagar University, 2025–26**

---

## 1. Data Import and Power Query Setup
1. Open **Power BI Desktop**.
2. Click **Get Data** -> **Text/CSV** -> Select `data/cleaned_merged_food_hunger_dataset.csv`.
3. Click **Transform Data** to open the **Power Query Editor**.
4. Check that data types are verified:
   - `Country`: Text
   - `Total Waste (Tons)`: Decimal / Whole Number
   - `Waste Per Capita (Kg)`: Decimal Number
   - `Economic Loss (Million $)`: Decimal Number
   - `Global Hunger Index`: Decimal Number
   - `Index Category`: Text
   - `Hunger-to-Waste Ratio`: Decimal Number
   - `Waste in Millions (Tons)`: Decimal Number
5. Click **Close & Apply**.
6. Import the custom theme: Go to **View** -> **Themes** -> **Browse for themes** -> Select `power_bi/PowerBI_Theme_Exact.json`.

---

## 2. Page 1: Hunger vs Economic Loss & Waste Distribution
- **Background**:
  - Insert Canvas Background / Image or soft rounded card layout with warm beige/purple tones.
- **Visual 1 (Top Left): Top 10 Countries By Hunger Index (Clustered Column Chart)**:
  - **X-axis**: `Country`
  - **Y-axis**: `Avg Hunger Index` (or `Global Hunger Index`, Aggregation: Average)
  - **Filter**: Filter top 10 by `Avg Hunger Index` descending.
  - **Data Color**: Hex `#543884` (Deep Purple).
  - **Title**: *Top 10 Countries By Hunger Index* (Centered, Bold, Underlined).
  - **Values**: India (33.2), Indonesia (24.1), Ethiopia (20.5), South Africa (15.4), Saudi Arabia (9.8), Mexico (9.0), Russia (7.5), China (7.0), Brazil (6.8), Turkey (6.2).
- **Visual 2 (Top Right): Card**:
  - **Field**: `[Selected Economic Loss ($M)]` -> Shows **1.37M**
  - **Title**: *Total Economic Loss(Million $)* (Underlined)
  - **Callout Value**: 32pt, Bold, Color `#543884`
- **Visual 3 (Bottom Left): Card**:
  - **Field**: `[Total Economic Loss ($M)]` -> Shows **17.80M**
  - **Title**: *Total Economic Loss(Million $)* (Underlined)
  - **Callout Value**: 36pt, Bold, Color `#543884`
- **Visual 4 (Bottom Right): Donut Chart**:
  - **Legend**: `Country`
  - **Values**: `Total Waste (Tons)` or `Economic Loss (Million $)`
  - **Detail Labels**: Category + Data value + Percent of total (e.g. `Italy 1.34M (7.61%)`, `Canada 1.21M (6.84%)`, `Spain 1.1M (6.22%)`, etc.)
  - **Title**: *Total Waste by Country* (Centered, Bold, Underlined).

---

## 3. Page 2: Map Visualization over Countries
- **Canvas Background**: Dark / Satellite Map Style.
- **Visual**: **Map (Bing Maps or Azure Map)**
  - **Location**: `Country`
  - **Bubble Size**: `Total Waste (Tons)`
  - **Bubble Color**: Hex `#0078D4` / Semi-transparent bright blue (`#38BDF8`).
  - **Tooltips**:
    - `Country`
    - `Total Waste (Tons)`
    - `Global Hunger Index`
    - `Economic Loss (Million $)`
  - **Title**: *Map Visualization over Countries* (Centered, Bold, Underlined).
  - **Map Theme**: Aerial / Satellite with labels.

---

## 4. Page 3: FOOD WASTAGE Vs HUNGER INDEX (Trends & Correlation)
- **Top Header**:
  - Shape: Rounded Rectangle, Color `#2B3A67` / Navy Indigo.
  - Text: **FOOD WASTAGE Vs HUNGER INDEX** (White, Bold, 20pt, Centered).
- **Visual 1 (Top Left): Trend Line Over Years (Line Chart with Secondary Y-Axis)**:
  - **X-axis**: `Year` (from `yearly_trends_food_hunger.csv`)
  - **Y-axis (Primary)**: `Total Food Waste (Million Tons)` (Red Line `#E63946`)
  - **Secondary Y-axis**: `Avg Hunger Index` (Navy Blue Line `#1E3A8A`)
  - **Title**: *Trend Line Over Years*
- **Visual 2 (Top Right): Top 10 Countries By Food Waste (Clustered Column Chart)**:
  - **X-axis**: `Country`
  - **Y-axis**: `Total Waste (Tons)` or `Sum of Sum of Total Was...`
  - **Filter**: Top 10 by waste descending.
  - **Bar Color**: Royal Slate Blue (`#4361EE` / `#3B82F6`).
  - **Countries**: Italy (1.34M), Canada (1.21M), Spain (1.10M), France (1.07M), Argentina (1.04M), Mexico (1.04M), South Africa (0.97M), USA (0.95M), Australia (0.90M), Russia (0.83M).
- **Visual 3 (Bottom): Food Waste Vs Hunger (Scatter Chart)**:
  - **X-axis**: `Weighted Avg Waste per Capita (Kg)`
  - **Y-axis**: `Avg Hunger Index`
  - **Details**: `Country`
  - **Marker Color**: Crimson Red (`#E63946`) with soft glow/halo.
  - **Title**: *Food Waste Vs Hunger*
  - **Observation**: Shows clearly that high waste per capita countries cluster with low hunger index (< 10), while high hunger countries have lower or moderate waste per capita.
