import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk
import plotly.express as px
import plotly.graph_objects as go

st.write("# COVID-19 Cases and Deaths in US Counties")
DATA_URL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'

@st.cache(persist=True)
def load_data():
    """
    Returns DataFrame of covid-19 cases and deaths for US counties
    """
    location = pd.read_csv('2019_Gaz_counties_national.csv', encoding='ISO-8859-1')
    location.columns = location.columns.str.replace(' ', '')
    nyt_covid_file = pd.read_csv(DATA_URL)
    joined_csv = pd.merge(nyt_covid_file, location, how='inner', left_on=['fips'], 
                      right_on=['GEOID'])
    joined_csv.rename(columns={"INTPTLAT": "latitude", "INTPTLONG": "longitude"}, inplace=True)
    return joined_csv

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text('Loading data...done!')

if st.checkbox('Show covid data'):
    st.write(data)

fig = px.scatter(data, data['date'], data['cases'], 
                 color=data['state'], hover_data=['county'])
st.plotly_chart(fig)

########################################################################################
    #   WIDGETS
subset_data = data

### MULTISELECT
state_name_input = st.sidebar.multiselect(
'Select State',
data.groupby('state').size().reset_index()['state'].tolist(), default=['Arizona'])

# by state name
if len(state_name_input) > 0:
    subset_data = data[data['state'].isin(state_name_input)]

if st.checkbox('Show covid subset data'):
    st.write(subset_data)
  
########################################################################################
## scatterplots

st.subheader('Covid-19 Cases by All Counties in Selected State(s)')

fig_cases = px.scatter(subset_data, subset_data['date'], subset_data['cases'], 
                 color=subset_data['state'], hover_data=['county'])
st.plotly_chart(fig_cases)

st.subheader('Covid-19 Deaths by All Counties in Selected State(s)')

fig_deaths = px.scatter(subset_data, subset_data['date'], subset_data['deaths'], 
                 color=subset_data['state'], hover_data=['county'])
st.plotly_chart(fig_deaths)

########################################################################################
### experimenting with maps

latest_update = data.sort_values(['date'], ascending=False).reset_index(drop=True).iloc[:2]
latest_date = latest_update['date'].values[0]
current_data = data[data['date']==latest_date]

fig = go.Figure()

fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = current_data['longitude'],
        lat = current_data['latitude'],
        text = current_data['county'],
        marker = dict(
            size = current_data['cases']/5000
        )))
    
fig.update_layout(
        title_text = 'Bubble Map of Covid-19 Cases in Different US Counties<br>(Click legend to toggle)',
        showlegend = True,
        geo = dict(
            scope = 'usa',
            landcolor = 'rgb(217, 217, 217)',
        )
    )

st.plotly_chart(fig)