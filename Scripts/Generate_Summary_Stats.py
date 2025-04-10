import arcpy
import json
import os

# -----------------------------------------------------------
# STEP 1: Define Workspace and Input Parameters
# -----------------------------------------------------------

# Set the workspace to your File Geodatabase containing the seagrass data.
# Replace the path below with the actual location of your geodatabase.
arcpy.env.workspace = r"C:\Users\KevinMazur\Documents\GISNerd\Seagrass_Change_SWFWMD\ArcGIS\SWFWMD_Seagrass_Change\SWFWMD_Seagrass_Change.gdb"

# Define the merged feature class name
input_feature_class = "Seagrass_Merge"

# Field names used in the analysis
year_field = "Year"           # Field that indicates the year.
calc_field = "Calc_Acres"     # Field that contains calculated seagrass area in acres.

# Define the name for the output summary table (temporary table)
output_summary_table = "Seagrass_Summary_Updated"

# Define the output JSON file (update the path as required)
output_json = r"C:\Users\KevinMazur\Documents\GISNerd\Seagrass_Change_SWFWMD\data\Seagrass_Change_Stats_Updated.json"

# -----------------------------------------------------------
# STEP 2: Calculate Summary Statistics for Each Year
# -----------------------------------------------------------

# We use arcpy.Statistics_analysis to group by the "Year" field and sum the "Calc_Acres" for each year.
stat_fields = [[calc_field, "SUM"]]

try:
    arcpy.Statistics_analysis(in_table=input_feature_class,
                                out_table=output_summary_table,
                                statistics_fields=stat_fields,
                                case_field=year_field)
    print(f"Summary table '{output_summary_table}' created successfully.")
except Exception as e:
    print(f"Error during Statistics_analysis: {e}")
    raise

# -----------------------------------------------------------
# STEP 3: Retrieve Summary Data and Compute Change Statistics
# -----------------------------------------------------------

# Create an empty dictionary to store total acres per year.
summary_data = {}

# The output field for the sum will be automatically named "SUM_<calc_field>"
sum_field = f"SUM_{calc_field}"

# Use a SearchCursor to iterate over the summary table and collect data.
try:
    with arcpy.da.SearchCursor(output_summary_table, [year_field, sum_field]) as cursor:
        for row in cursor:
            year = row[0]
            total_acres = row[1]
            summary_data[year] = total_acres
            print(f"Year {year}: Total Acres = {total_acres}")
except Exception as e:
    print(f"Error reading summary data: {e}")
    raise

# Sort the years in ascending order.
sorted_years = sorted(summary_data.keys())

# Create a list to hold the final change statistics data for export.
results = []

# Variable to keep track of the previous year's total for computing differences.
previous_total = None

# Loop through the sorted years to calculate the year-over-year difference and percentage change.
for year in sorted_years:
    current_total = summary_data[year]
    # Default values for change statistics.
    difference = None
    pct_change = None

    if previous_total is not None:
        difference = current_total - previous_total
        # Avoid division by zero.
        pct_change = (difference / previous_total) * 100 if previous_total != 0 else 0

    # Append the result as a dictionary.
    results.append({
        "Year": year,
        "Total_Acres": current_total,
        "Difference": difference,
        "Percentage_Change": pct_change
    })
    
    previous_total = current_total

# Optionally, print the change statistics.
print("\nYear-over-Year Change Statistics:")
for record in results:
    year = record["Year"]
    diff = record["Difference"]
    pct = record["Percentage_Change"]
    if diff is not None:
        print(f"From {year - 1} to {year}: Difference = {diff:.2f} acres, Percentage Change = {pct:.2f}%")
    else:
        print(f"{year}: No previous year data for change calculation.")

# -----------------------------------------------------------
# STEP 4: Export the Results to a JSON File
# -----------------------------------------------------------

# Write the results list to a JSON file.
try:
    # Ensure the directory for the output JSON exists.
    output_dir = os.path.dirname(output_json)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(output_json, 'w') as json_file:
        json.dump(results, json_file, indent=4)
    print(f"\nChange statistics successfully exported to '{output_json}'")
except Exception as e:
    print(f"Error writing JSON file: {e}")
    raise
