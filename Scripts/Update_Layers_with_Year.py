import arcpy
import re

# Set the workspace to your File Geodatabase
arcpy.env.workspace = r"C:\Users\KevinMazur\Documents\GISNerd\Seagrass_Change_SWFWMD\ArcGIS\SWFWMD_Seagrass_Change\SWFWMD_Seagrass_Change.gdb"

# List all feature classes in the workspace
feature_classes = arcpy.ListFeatureClasses()

# Regular expression pattern to find a four-digit year in the feature class name
year_pattern = re.compile(r"(\d{4})")

# Loop through each feature class
for fc in feature_classes:
    print(f"Processing feature class: {fc}")
    
    # Search for the year in the feature class name
    match = year_pattern.search(fc)
    if match:
        year_str = match.group(1)
        print(f"Found year: {year_str}")
        
        # List existing fields in the feature class
        fields = [field.name for field in arcpy.ListFields(fc)]
        
        # If the "Year" field doesn't exist, add it. Using SHORT because years fit within an integer.
        if "Year" not in fields:
            print(f"Adding 'Year' field to {fc}")
            arcpy.AddField_management(fc, "Year", "SHORT")
        else:
            print(f"'Year' field already exists in {fc}")
        
        # Use an UpdateCursor to populate the 'Year' field for all records in the feature class
        with arcpy.da.UpdateCursor(fc, ["Year"]) as cursor:
            for row in cursor:
                row[0] = int(year_str)
                cursor.updateRow(row)
        print(f"Updated 'Year' field for {fc}\n")
    else:
        print(f"No four-digit year found in the name of {fc}. Skipping...\n")
