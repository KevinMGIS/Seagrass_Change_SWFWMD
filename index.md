[View the Interactive Map & Dashboard](map.html)

**Notice: This project is for display purposes only and is a coding exercise.**

# Seagrass Coverage Dashboard

This project is an interactive web application designed to visualize and analyze seagrass coverage over time along selected coastal areas. It combines spatial data and temporal statistics to provide insights into the changes in seagrass extent by year.

## Project Overview

The project utilizes individual GeoJSON files for the years 2004, 2006, 2008, 2010, 2012, 2014, 2016, and 2018. Each file contains polygon data representing seagrass coverage along with important attributes, such as total area (in acres). A separate JSON file, containing precomputed change statistics, is used to generate a Plotly chart that dynamically displays the trends in seagrass coverage and percentage changes over time.

## Interactive Features

- **Map Display:**  
  An interactive map built using the ArcGIS API for JavaScript displays the seagrass polygons. Each year’s data is loaded as a separate layer with a unique color. By default, only the 2018 layer is visible, and users can toggle each year on or off using the legend in the top right.

- **Basemap Selector:**  
  A basemap selector is provided in the top left, allowing users to switch between different basemaps (with Oceans set as the default) to adjust the visual context of the map.

- **Pop-up Information:**  
  Clicking on any seagrass polygon brings up a popup displaying details such as the year and the total area in acres.

- **Dashboard Chart:**  
  A Plotly chart positioned in the bottom left displays both bar and line charts that illustrate the overall seagrass area and percentage changes over the years.

## Data Processing and Technical Stack

- **Data Processing:**  
  The spatial analysis was performed using Python and ArcPy to compute year-over-year change statistics, which were then exported to static JSON files used by the web application.

- **Front-end Tools:**  
  - **ArcGIS API for JavaScript:** Used for rendering the interactive map and managing GeoJSON layers.
  - **Plotly:** Used for generating the dynamic chart that visualizes temporal trends.
  - **HTML/CSS/JavaScript:** These technologies are used to create the overall structure and interactivity of the project.

- **Hosting:**  
  The project is hosted on GitHub Pages, making it a fully code-based, static solution that demonstrates how spatial data visualization can be achieved with a simple yet effective workflow.

## Conclusion

This interactive dashboard serves as a proof-of-concept for integrating spatial data, statistical analysis, and web mapping into a cohesive, user-friendly platform. While the data is static and the project is primarily a coding exercise, the techniques demonstrated here can be further extended to support dynamic, real-time applications in environmental monitoring and resource management.

Feel free to explore the interactive map and dashboard by clicking the link above!
