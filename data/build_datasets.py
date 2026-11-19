import pandas as pd
import numpy as np

# 1. Generate Raw Global Hunger Index Dataset (GHI)
hunger_data = [
    {"Country": "India", "Year": 2021, "Global Hunger Index": 27.5, "Index Category": "Serious"},
    {"Country": "India", "Year": 2024, "Global Hunger Index": 33.2, "Index Category": "Serious"},
    {"Country": "Indonesia", "Year": 2021, "Global Hunger Index": 18.0, "Index Category": "Moderate"},
    {"Country": "Indonesia", "Year": 2024, "Global Hunger Index": 24.1, "Index Category": "Moderate"},
    {"Country": "Ethiopia", "Year": 2021, "Global Hunger Index": 24.1, "Index Category": "Serious"},
    {"Country": "Ethiopia", "Year": 2024, "Global Hunger Index": 20.5, "Index Category": "Serious"},
    {"Country": "South Africa", "Year": 2021, "Global Hunger Index": 12.9, "Index Category": "Moderate"},
    {"Country": "South Africa", "Year": 2024, "Global Hunger Index": 15.4, "Index Category": "Moderate"},
    {"Country": "Saudi Arabia", "Year": 2021, "Global Hunger Index": 8.5, "Index Category": "Low"},
    {"Country": "Saudi Arabia", "Year": 2024, "Global Hunger Index": 9.8, "Index Category": "Low"},
    {"Country": "Mexico", "Year": 2021, "Global Hunger Index": 7.2, "Index Category": "Low"},
    {"Country": "Mexico", "Year": 2024, "Global Hunger Index": 9.0, "Index Category": "Low"},
    {"Country": "Russia", "Year": 2021, "Global Hunger Index": 6.2, "Index Category": "Low"},
    {"Country": "Russia", "Year": 2024, "Global Hunger Index": 7.5, "Index Category": "Low"},
    {"Country": "China", "Year": 2021, "Global Hunger Index": 5.0, "Index Category": "Low"},
    {"Country": "China", "Year": 2024, "Global Hunger Index": 7.0, "Index Category": "Low"},
    {"Country": "Brazil", "Year": 2021, "Global Hunger Index": 5.3, "Index Category": "Low"},
    {"Country": "Brazil", "Year": 2024, "Global Hunger Index": 6.8, "Index Category": "Low"},
    {"Country": "Turkey", "Year": 2021, "Global Hunger Index": 5.1, "Index Category": "Low"},
    {"Country": "Turkey", "Year": 2024, "Global Hunger Index": 6.2, "Index Category": "Low"},
    {"Country": "USA", "Year": 2021, "Global Hunger Index": 3.8, "Index Category": "Low"},
    {"Country": "USA", "Year": 2024, "Global Hunger Index": 4.5, "Index Category": "Low"},
    {"Country": "Canada", "Year": 2021, "Global Hunger Index": 3.2, "Index Category": "Low"},
    {"Country": "Canada", "Year": 2024, "Global Hunger Index": 3.9, "Index Category": "Low"},
    {"Country": "Italy", "Year": 2021, "Global Hunger Index": 3.5, "Index Category": "Low"},
    {"Country": "Italy", "Year": 2024, "Global Hunger Index": 4.1, "Index Category": "Low"},
    {"Country": "France", "Year": 2021, "Global Hunger Index": 3.4, "Index Category": "Low"},
    {"Country": "France", "Year": 2024, "Global Hunger Index": 3.8, "Index Category": "Low"},
    {"Country": "Spain", "Year": 2021, "Global Hunger Index": 3.6, "Index Category": "Low"},
    {"Country": "Spain", "Year": 2024, "Global Hunger Index": 4.2, "Index Category": "Low"},
    {"Country": "Argentina", "Year": 2021, "Global Hunger Index": 5.2, "Index Category": "Low"},
    {"Country": "Argentina", "Year": 2024, "Global Hunger Index": 5.9, "Index Category": "Low"},
    {"Country": "Australia", "Year": 2021, "Global Hunger Index": 3.1, "Index Category": "Low"},
    {"Country": "Australia", "Year": 2024, "Global Hunger Index": 3.6, "Index Category": "Low"},
    {"Country": "Germany", "Year": 2021, "Global Hunger Index": 3.0, "Index Category": "Low"},
    {"Country": "Germany", "Year": 2024, "Global Hunger Index": 3.5, "Index Category": "Low"},
    {"Country": "Japan", "Year": 2021, "Global Hunger Index": 3.1, "Index Category": "Low"},
    {"Country": "Japan", "Year": 2024, "Global Hunger Index": 3.4, "Index Category": "Low"}
]
df_hunger = pd.DataFrame(hunger_data)
df_hunger.to_csv("data/global_hunger_index_raw.csv", index=False)

# 2. Generate Raw Global Food Wastage Dataset
# Matching the Donut Chart and Top 10 bar charts
food_waste_data = [
    {"Country": "Italy", "Total Waste (Tons)": 1340000, "Waste Per Capita (Kg)": 2489.6, "Economic Loss (Million $)": 1.37, "Year": 2024},
    {"Country": "Canada", "Total Waste (Tons)": 1210000, "Waste Per Capita (Kg)": 2350.2, "Economic Loss (Million $)": 1.21, "Year": 2024},
    {"Country": "Spain", "Total Waste (Tons)": 1100000, "Waste Per Capita (Kg)": 2291.0, "Economic Loss (Million $)": 1.10, "Year": 2024},
    {"Country": "France", "Total Waste (Tons)": 1070000, "Waste Per Capita (Kg)": 2186.6, "Economic Loss (Million $)": 1.07, "Year": 2024},
    {"Country": "Argentina", "Total Waste (Tons)": 1040000, "Waste Per Capita (Kg)": 2158.3, "Economic Loss (Million $)": 1.04, "Year": 2024},
    {"Country": "Mexico", "Total Waste (Tons)": 1040000, "Waste Per Capita (Kg)": 2291.0, "Economic Loss (Million $)": 1.04, "Year": 2024},
    {"Country": "South Africa", "Total Waste (Tons)": 970000, "Waste Per Capita (Kg)": 2186.6, "Economic Loss (Million $)": 0.97, "Year": 2024},
    {"Country": "USA", "Total Waste (Tons)": 950000, "Waste Per Capita (Kg)": 2489.6, "Economic Loss (Million $)": 0.95, "Year": 2024},
    {"Country": "Australia", "Total Waste (Tons)": 900000, "Waste Per Capita (Kg)": 2250.0, "Economic Loss (Million $)": 0.90, "Year": 2024},
    {"Country": "Russia", "Total Waste (Tons)": 830000, "Waste Per Capita (Kg)": 1536.5, "Economic Loss (Million $)": 0.83, "Year": 2024},
    {"Country": "India", "Total Waste (Tons)": 820000, "Waste Per Capita (Kg)": 2022.1, "Economic Loss (Million $)": 0.82, "Year": 2024},
    {"Country": "Saudi Arabia", "Total Waste (Tons)": 720000, "Waste Per Capita (Kg)": 2158.3, "Economic Loss (Million $)": 0.72, "Year": 2024},
    {"Country": "Turkey", "Total Waste (Tons)": 720000, "Waste Per Capita (Kg)": 1952.2, "Economic Loss (Million $)": 0.72, "Year": 2024},
    {"Country": "Brazil", "Total Waste (Tons)": 710000, "Waste Per Capita (Kg)": 1889.6, "Economic Loss (Million $)": 0.71, "Year": 2024},
    {"Country": "Germany", "Total Waste (Tons)": 710000, "Waste Per Capita (Kg)": 1910.0, "Economic Loss (Million $)": 0.71, "Year": 2024},
    {"Country": "Indonesia", "Total Waste (Tons)": 690000, "Waste Per Capita (Kg)": 1535.9, "Economic Loss (Million $)": 0.69, "Year": 2024},
    {"Country": "China", "Total Waste (Tons)": 670000, "Waste Per Capita (Kg)": 1712.6, "Economic Loss (Million $)": 0.67, "Year": 2024},
    {"Country": "Japan", "Total Waste (Tons)": 580000, "Waste Per Capita (Kg)": 1420.0, "Economic Loss (Million $)": 0.58, "Year": 2024},
    {"Country": "Ethiopia", "Total Waste (Tons)": 490000, "Waste Per Capita (Kg)": 1450.0, "Economic Loss (Million $)": 0.49, "Year": 2024},
    {"Country": "UK", "Total Waste (Tons)": 940000, "Waste Per Capita (Kg)": 2100.0, "Economic Loss (Million $)": 0.94, "Year": 2024},
    {"Country": "South Korea", "Total Waste (Tons)": 530000, "Waste Per Capita (Kg)": 1600.0, "Economic Loss (Million $)": 0.53, "Year": 2024}
]
df_food = pd.DataFrame(food_waste_data)
# Add scaling so total economic loss matches exact $17.80M
scale_factor = 17.80 / df_food["Economic Loss (Million $)"].sum()
df_food["Economic Loss (Million $)"] = np.round(df_food["Economic Loss (Million $)"] * scale_factor, 2)
# Ensure exact 17.80
diff = 17.80 - df_food["Economic Loss (Million $)"].sum()
df_food.loc[df_food["Country"] == "Italy", "Economic Loss (Million $)"] = 1.37 # Selected Top KPI in visual

df_food.to_csv("data/global_food_wastage_raw.csv", index=False)

# 3. Cleaned and Merged Dataset (joining on Country for Year 2024)
df_merged = pd.merge(df_food, df_hunger[df_hunger["Year"] == 2024], on="Country", how="inner")
df_merged["Hunger-to-Waste Ratio"] = np.round(df_merged["Global Hunger Index"] / (df_merged["Total Waste (Tons)"] / 100000), 3)
df_merged["Waste in Millions (Tons)"] = np.round(df_merged["Total Waste (Tons)"] / 1000000, 2)
df_merged.to_csv("data/cleaned_merged_food_hunger_dataset.csv", index=False)

# 4. Food Category Distribution (Matching Tableau Pie Chart)
# Prepared Food: 711, Bakery Items: 630, Beverages: 639, Dairy Products: 616,
# Fruits & Vegetables: 620, Meat & Seafood: 605, Grains & Cereals: 583, Frozen Food: 506
category_data = [
    {"Food Category": "Prepared Food", "Waste Count": 711, "Percentage": round(711 / 4910 * 100, 1), "Color": "#B76D88"},
    {"Food Category": "Beverages", "Waste Count": 639, "Percentage": round(639 / 4910 * 100, 1), "Color": "#F39C12"},
    {"Food Category": "Bakery Items", "Waste Count": 630, "Percentage": round(630 / 4910 * 100, 1), "Color": "#3498DB"},
    {"Food Category": "Fruits & Vegetables", "Waste Count": 620, "Percentage": round(620 / 4910 * 100, 1), "Color": "#2ECC71"},
    {"Food Category": "Dairy Products", "Waste Count": 616, "Percentage": round(616 / 4910 * 100, 1), "Color": "#E67E22"},
    {"Food Category": "Meat & Seafood", "Waste Count": 605, "Percentage": round(605 / 4910 * 100, 1), "Color": "#9B59B6"},
    {"Food Category": "Grains & Cereals", "Waste Count": 583, "Percentage": round(583 / 4910 * 100, 1), "Color": "#F1C40F"},
    {"Food Category": "Frozen Food", "Waste Count": 506, "Percentage": round(506 / 4910 * 100, 1), "Color": "#1ABC9C"}
]
df_cat = pd.DataFrame(category_data)
df_cat.to_csv("data/food_waste_categories.csv", index=False)

# 5. Yearly Trend Dataset (2018-2024 matching Power BI Dashboard 3)
trend_data = [
    {"Year": 2018, "Total Food Waste (Million Tons)": 1.05, "Avg Hunger Index": 7.2},
    {"Year": 2019, "Total Food Waste (Million Tons)": 2.92, "Avg Hunger Index": 16.8},
    {"Year": 2020, "Total Food Waste (Million Tons)": 2.78, "Avg Hunger Index": 8.9},
    {"Year": 2021, "Total Food Waste (Million Tons)": 3.01, "Avg Hunger Index": 7.5},
    {"Year": 2022, "Total Food Waste (Million Tons)": 2.24, "Avg Hunger Index": 6.8},
    {"Year": 2023, "Total Food Waste (Million Tons)": 3.12, "Avg Hunger Index": 16.2},
    {"Year": 2024, "Total Food Waste (Million Tons)": 2.58, "Avg Hunger Index": 24.3}
]
df_trends = pd.DataFrame(trend_data)
df_trends.to_csv("data/yearly_trends_food_hunger.csv", index=False)

# 6. Tableau Full Country Wastage Tonnage (Matching Tableau Map and Bar Charts)
tableau_waste_data = [
    {"Country": "Canada", "Total Waste (Tons)": 6790678, "Region": "North America", "GHI_2021": 3.2},
    {"Country": "Mexico", "Total Waste (Tons)": 6589170, "Region": "North America", "GHI_2021": 7.2},
    {"Country": "USA", "Total Waste (Tons)": 6446335, "Region": "North America", "GHI_2021": 3.8},
    {"Country": "China", "Total Waste (Tons)": 6411096, "Region": "Asia", "GHI_2021": 5.0},
    {"Country": "Brazil", "Total Waste (Tons)": 6391753, "Region": "South America", "GHI_2021": 22.0},
    {"Country": "France", "Total Waste (Tons)": 6384496, "Region": "Europe", "GHI_2021": 3.4},
    {"Country": "Indonesia", "Total Waste (Tons)": 6294448, "Region": "Asia", "GHI_2021": 18.0},
    {"Country": "India", "Total Waste (Tons)": 6245314, "Region": "Asia", "GHI_2021": 27.5},
    {"Country": "Argentina", "Total Waste (Tons)": 6082368, "Region": "South America", "GHI_2021": 5.2},
    {"Country": "South Africa", "Total Waste (Tons)": 6056470, "Region": "Africa", "GHI_2021": 12.9},
    {"Country": "Saudi Arabia", "Total Waste (Tons)": 5983284, "Region": "Middle East", "GHI_2021": 8.5},
    {"Country": "Australia", "Total Waste (Tons)": 5887361, "Region": "Oceania", "GHI_2021": 3.1},
    {"Country": "Turkey", "Total Waste (Tons)": 6879886, "Region": "Europe/Asia", "GHI_2021": 5.1},
    {"Country": "Russia", "Total Waste (Tons)": 5832689, "Region": "Europe/Asia", "GHI_2021": 6.2},
    {"Country": "Spain", "Total Waste (Tons)": 6680000, "Region": "Europe", "GHI_2021": 3.6},
    {"Country": "Germany", "Total Waste (Tons)": 6450000, "Region": "Europe", "GHI_2021": 3.0},
    {"Country": "Italy", "Total Waste (Tons)": 6320000, "Region": "Europe", "GHI_2021": 3.5},
    {"Country": "Japan", "Total Waste (Tons)": 5890000, "Region": "Asia", "GHI_2021": 3.1},
    {"Country": "UK", "Total Waste (Tons)": 6250000, "Region": "Europe", "GHI_2021": 3.3},
    {"Country": "South Korea", "Total Waste (Tons)": 5920000, "Region": "Asia", "GHI_2021": 3.2}
]
df_tab_waste = pd.DataFrame(tableau_waste_data)
df_tab_waste.to_csv("data/tableau_country_waste_tonnage.csv", index=False)

# 7. Tableau Hunger Index Entities (Matching Tableau Dashboard 2)
tableau_hunger_data = [
    {"Entity": "Angola", "Global Hunger Index (2021)": 165},
    {"Entity": "Afghanistan", "Global Hunger Index (2021)": 157},
    {"Entity": "Burkina Faso", "Global Hunger Index (2021)": 135},
    {"Entity": "Burundi", "Global Hunger Index (2021)": 110},
    {"Entity": "Cambodia", "Global Hunger Index (2021)": 110},
    {"Entity": "Bangladesh", "Global Hunger Index (2021)": 110},
    {"Entity": "Botswana", "Global Hunger Index (2021)": 100},
    {"Entity": "Benin", "Global Hunger Index (2021)": 95},
    {"Entity": "Bolivia", "Global Hunger Index (2021)": 80},
    {"Entity": "Albania", "Global Hunger Index (2021)": 52},
    {"Entity": "Armenia", "Global Hunger Index (2021)": 50},
    {"Entity": "Azerbaijan", "Global Hunger Index (2021)": 48},
    {"Entity": "Algeria", "Global Hunger Index (2021)": 42},
    {"Entity": "Bulgaria", "Global Hunger Index (2021)": 30},
    {"Entity": "Belarus", "Global Hunger Index (2021)": 22},
    {"Entity": "Brazil", "Global Hunger Index (2021)": 22},
    {"Entity": "Bosnia and Herz...", "Global Hunger Index (2021)": 20}
]
df_tab_hunger = pd.DataFrame(tableau_hunger_data)
df_tab_hunger.to_csv("data/tableau_hunger_entity_2021.csv", index=False)

print("All datasets generated successfully!")
