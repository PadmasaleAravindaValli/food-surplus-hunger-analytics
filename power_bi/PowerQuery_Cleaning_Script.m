// ==============================================================================
// Power Query M Script: Food Wastage vs Hunger Index Pipeline
// Dayananda Sagar University - SEC Project (2025-26)
// ==============================================================================

// STEP 1: Load and Clean Raw Global Hunger Index (GHI) Data
let
    // Source: Point this to your local path or relative folder
    Source_Hunger = Csv.Document(File.Contents("data/global_hunger_index_raw.csv"), [Delimiter=",", Columns=4, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    Promote_Hunger_Headers = Table.PromoteHeaders(Source_Hunger, [PromoteAllScalars=true]),
    
    // 1. Remove duplicate rows
    Distinct_Hunger = Table.Distinct(Promote_Hunger_Headers),
    
    // 2. Standardize Country names
    Standardize_Hunger_Country = Table.TransformColumns(Distinct_Hunger, {
        {"Country", each Text.Trim(_), type text},
        {"Country", each if _ = "United States" or _ = "United States of America" then "USA" 
                        else if _ = "Great Britain" or _ = "United Kingdom" then "UK" 
                        else _, type text}
    }),
    
    // 3. Fix data types
    Type_Hunger = Table.TransformColumnTypes(Standardize_Hunger_Country, {
        {"Country", type text},
        {"Year", Int64.Type},
        {"Global Hunger Index", type number},
        {"Index Category", type text}
    }),
    
    // 4. Handle Missing / Null Values
    Filter_Hunger_Nulls = Table.SelectRows(Type_Hunger, each [Global Hunger Index] <> null and [Country] <> null and [Country] <> "")
in
    Filter_Hunger_Nulls


// STEP 2: Load and Clean Raw Food Wastage Data
let
    Source_Food = Csv.Document(File.Contents("data/global_food_wastage_raw.csv"), [Delimiter=",", Columns=5, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    Promote_Food_Headers = Table.PromoteHeaders(Source_Food, [PromoteAllScalars=true]),
    
    // 1. Remove duplicates
    Distinct_Food = Table.Distinct(Promote_Food_Headers),
    
    // 2. Standardize country names
    Standardize_Food_Country = Table.TransformColumns(Distinct_Food, {
        {"Country", each Text.Trim(_), type text},
        {"Country", each if _ = "United States" or _ = "United States of America" then "USA" 
                        else if _ = "Great Britain" or _ = "United Kingdom" then "UK" 
                        else _, type text}
    }),
    
    // 3. Correct data types
    Type_Food = Table.TransformColumnTypes(Standardize_Food_Country, {
        {"Country", type text},
        {"Total Waste (Tons)", type number},
        {"Waste Per Capita (Kg)", type number},
        {"Economic Loss (Million $)", type number},
        {"Year", Int64.Type}
    }),
    
    // 4. Handle Missing / Null Values and Outliers
    Filter_Food_Nulls = Table.SelectRows(Type_Food, each [#"Total Waste (Tons)"] <> null and [#"Economic Loss (Million $)"] <> null and [Country] <> "")
in
    Filter_Food_Nulls


// STEP 3: Merged Final Dataset (Power Query Inner Join on Country)
let
    // Perform Merge on Country
    Merged_Queries = Table.NestedJoin(Food_Wastage_Cleaned, {"Country"}, Hunger_Index_Cleaned, {"Country"}, "Hunger_Data", JoinKind.Inner),
    
    // Expand Hunger Index fields
    Expanded_Hunger = Table.ExpandTableColumn(Merged_Queries, "Hunger_Data", {"Global Hunger Index", "Index Category"}, {"Global Hunger Index", "Index Category"}),
    
    // 5. Add Custom Calculated Columns
    // A. Waste in Millions of Tons
    Add_Waste_Million = Table.AddColumn(Expanded_Hunger, "Waste in Millions (Tons)", each [#"Total Waste (Tons)"] / 1000000, type number),
    
    // B. Hunger-to-Waste Ratio
    Add_HW_Ratio = Table.AddColumn(Add_Waste_Million, "Hunger-to-Waste Ratio", each [Global Hunger Index] / ([#"Total Waste (Tons)"] / 100000), type number),
    
    // 6. Final Data Integrity Validation
    Validated_Output = Table.SelectRows(Add_HW_Ratio, each [Global Hunger Index] >= 0 and [#"Total Waste (Tons)"] > 0)
in
    Validated_Output
