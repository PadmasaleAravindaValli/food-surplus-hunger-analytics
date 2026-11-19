# Tableau Workbook Specification: Food Wastage vs Hunger Index

**Dayananda Sagar University (DSU) - 2025–26**  
**Bachelor of Technology in CSE (Data Science)**

---

## Data Sources
1. **Source 1: `tableau_country_waste_tonnage.csv`**
   - Fields: `Country`, `Total Waste (Tons)`, `Region`, `GHI_2021`
2. **Source 2: `food_waste_categories.csv`**
   - Fields: `Food Category`, `Waste Count`, `Percentage`, `Color`
3. **Source 3: `tableau_hunger_entity_2021.csv`**
   - Fields: `Entity`, `Global Hunger Index (2021)`
4. **Source 4: `yearly_trends_food_hunger.csv`**
   - Fields: `Year`, `Total Food Waste (Million Tons)`, `Avg Hunger Index`

---

## Tableau Dashboard 1: Food Waste Breakdown & Bullet Graph
### 1. Top Left: "Top 10 Countries by Total Food Waste (Tons)"
- **Columns**: `Country`
- **Rows**: `SUM([Total Waste (Tons)])`
- **Color**: Distinct categorical colors per country (`Country` on Color shelf).
- **Y-Axis Range**: 0M to 7M Tons.

### 2. Top Right: "Bar Graph"
- **Columns**: `SUM([Total Waste (Tons)])`
- **Rows**: `Country` (Sorted Alphabetically or by Value)
- **Color**: Single Rose Pink `#D85A87` / `#C2185B`.
- **Value Range**: 0K to 7000K.

### 3. Bottom Left: "Pie chart of food waste"
- **Marks**: Pie
- **Angle**: `SUM([Waste Count])`
- **Color**: `[Food Category]`
- **Labels**: `[Food Category]` & `SUM([Waste Count])`
  - Prepared Food: 711
  - Beverages: 639
  - Bakery Items: 630
  - Fruits & Vegetables: 620
  - Dairy Products: 616
  - Meat & Seafood: 605
  - Grains & Cereals: 583
  - Frozen Food: 506
  - **Total**: 4,910 items

### 4. Bottom Right: "Bullet Graph"
- **Columns**: `SUM([Total Waste (Tons)])`
- **Rows**: `Country`, `Year` (2025)
- **Marks**: Reference lines / Distribution bands (60%, 80% of target, bullet whiskers).

---

## Tableau Dashboard 2: Global Hunger Index Patterns
### 1. Top: "Bar Chart"
- **Columns**: `SUM([Global Hunger Index (2021)])`
- **Rows**: `[Entity]`
- **Color**: Sequential Blue Gradient (`#BEE3F8` to `#1E3A8A`) based on `SUM([Global Hunger Index (2021)])`.
- **Key Entities**:
  - Angola: 165
  - Afghanistan: 157
  - Burkina Faso: 135
  - Burundi: 110
  - Cambodia: 110
  - Bangladesh: 110
  - Botswana: 100
  - Benin: 95
  - Bolivia: 80
  - Albania: 52
  - Armenia: 50
  - Azerbaijan: 48
  - Algeria: 42
  - Bulgaria: 30
  - Belarus: 22
  - Brazil: 22
  - Bosnia and Herzegovina: 20

### 2. Bottom: "Line Graph"
- **Columns**: `Year`
- **Rows**: `SUM([Global Hunger Index])`
- **Marks**: Continuous Line with Data Point Tooltips.
- **Tooltip**: `Year: 2021`, `Global Hunger Index (2021): 2,149`.

---

## Tableau Dashboard 3: World Food Waste Choropleth Map
### Visual: "Map"
- **Marks**: Map (Filled Map / Choropleth)
- **Detail**: `Country`
- **Color**: `SUM([Total Waste (Tons)])`
- **Color Palette**: Red-Gold / Salmon Sequential Gradient (`6M` to `7M`)
- **Key Country Values on Hover**:
  - Canada: 6,790,678
  - Mexico: 6,589,170
  - USA: 6,446,335
  - China: 6,411,096
  - Brazil: 6,391,753
  - France: 6,384,496
  - Indonesia: 6,294,448
  - India: 6,245,314
  - Argentina: 6,082,368
  - South Africa: 6,056,470
  - Saudi Arabia: 5,983,284
  - Australia: 5,887,361
  - Russia: 5,832,689
  - Turkey: 6,879,886
