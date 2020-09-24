I am exploring using Streamlit to create a simple yet powerful dashboard to visualize COVID-19 cases and deaths for US states and counties.

I fetch the data from URL provided by the New York Times in their GitHub repository. This is time series data updated every day by some kind souls from the NY Times. You can read more about the data at:
https://github.com/nytimes/covid-19-data

I join this data to a csv file which has latitude, longitude information for US counties. I wanted to visualize COVID cases and deaths on a US map and this data will help me achieve that objective. The csv file is called, 2019_Gaz_counties_national.csv and was downloaded from, https://www.census.gov/geographies/reference-files/time-series/geo/gazetteer-files.html

I deployed the app on Heroku. You can see it at:
https://streamlit-covid-app.herokuapp.com/

To help me deploy the app, I followed this great Youtube tutorial:
https://www.youtube.com/watch?v=mQ7rGcE766k

My favorite part about this project is the data visualization. I use a bubble plot to show Covid-19 hotspots in different counties in the US.
I should mention that in order to make this plot, I selected the latest date which has reported Covid19-cases for each US county since that date corresponds to the cumulative number of cases reported from the day data collection began in Jan/Feb 2020. The map below shows cumulative cases reported for September 22, 2020.

![image](https://user-images.githubusercontent.com/31268268/94161325-69836b00-fe3a-11ea-8ba0-1db3232b5f76.png)

