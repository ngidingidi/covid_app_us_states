I am exploring using Streamlit to create a simple yet powerful dashboard to visualize COVID-19 cases and deaths for US states and counties.

I fetch the data from URL provided by the New York Times in their GitHub repository:
https://github.com/nytimes/covid-19-data

I join this data to a csv file which has latitude, longitude information for US counties. I wanted to visualize COVID cases and deaths on a US map and this data will help me achieve that objective. The csv file is called, 2019_Gaz_counties_national.csv and was downloaded from, https://www.census.gov/geographies/reference-files/time-series/geo/gazetteer-files.html

Ultimately I plan to deploy the app on Heroku
