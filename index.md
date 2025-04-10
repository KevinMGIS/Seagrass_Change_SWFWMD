[View the Interactive Map & Dashboard](https://kevinmgis.github.io/Seagrass_Change_SWFWMD/map.html)

**Notice: This project is for display purposes only and is a coding exercise.**

# Seagrass Coverage Dashboard

This project is an interactive web mapping application designed to visualize seagrass coverage along select coastal areas over time. The spatial data is hosted on ArcGIS Online as a Feature Service, which allows each year’s data to be accessed as a separate feature layer. This approach improves data management and leverages ArcGIS Online's optimized serving of geospatial information.

## Project Overview

The application displays seagrass data from multiple years (2004, 2006, 2008, 2010, 2012, 2014, 2016, and 2018) through separate layers hosted on ArcGIS Online.  
- **Interactive Map:**  
  A web map built with the ArcGIS API for JavaScript loads each year's seagrass data as an individual layer from a hosted Feature Service. By default, only the 2018 layer is visible; users can toggle other layers on and off using a legend with color-coded checkboxes.
- **Basemap Selector:**  
  A basemap selector (defaulting to the Oceans basemap) lets users choose from different background maps to enhance the visualization context.
- **Dynamic Chart:**  
  A Plotly chart displays precomputed statistics such as total seagrass area and percentage change over time. This chart updates alongside map interactions, providing a temporal perspective on seagrass trends.

## Data and Technical Stack

- **Data Hosting on ArcGIS Online:**  
  The seagrass data is hosted as a Feature Service on ArcGIS Online. Each year’s data is stored in its own layer within the service, making it easy to manage and toggle within the interactive map.
- **Front-end Technologies:**  
  - **ArcGIS API for JavaScript:** Powers the interactive map, handling the loading and filtering of feature layers directly from ArcGIS Online.
  - **Plotly:** Used for creating a dynamic, interactive chart that visualizes change statistics.
  - **HTML, CSS, and JavaScript:** Provide the overall structure and interactivity of the web application.

## How It Works

1. **Data Layers:**  
   The map loads individual layers corresponding to each year from the ArcGIS Online Feature Service. Unique colors are assigned to each layer, and a legend enables users to toggle visibility by year.
2. **Basemap Selection:**  
   A dropdown control allows users to switch between different basemaps, with the Oceans basemap as the default for coastal detail.
3. **Interactive Chart:**  
   Precomputed seagrass change statistics are loaded from a JSON file and rendered via Plotly, offering a visual summary of trends over the years.
4. **Optimized Performance:**  
   Although the underlying geospatial data is large, hosting it on ArcGIS Online ensures optimized delivery, while the application includes a loading indicator to improve the user experience during data retrieval.

## Conclusion

This coding exercise demonstrates an end-to-end workflow for building an interactive geospatial dashboard—from processing and hosting data on ArcGIS Online to integrating advanced web mapping and dynamic charting. While the application is static and designed for demonstration purposes, the techniques and technologies used here can be extended to support more complex, real-time environmental analyses.

Feel free to explore the interactive map and dashboard by clicking the link above!
