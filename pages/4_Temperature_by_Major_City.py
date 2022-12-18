import streamlit as st
import altair as alt
import pandas as pd
from Main_Page import dfcity


st.title("Temperatures by City")
st.sidebar.markdown("# Average temperatures sorted by city")
st.sidebar.markdown("The user is able to see the temperatures by major city, where it is plotted into line charts along with their 95th confidence interval. The user is able to select which cities they desire to plot with a multiselect field and choose the range of years they want to plot.")

year_range = st.slider('Select a year range', 1750, 2015, (1900, 2000))

dfcity = dfcity[(dfcity['year'].astype(int) >= year_range[0]) & (
    dfcity['year'].astype(int) <= int(year_range[1]))]

city_list = dfcity['City'].unique().tolist()
options = st.multiselect('Choose cities', city_list)
dfcity = dfcity[dfcity['City'].isin(options)]

chart = alt.Chart(dfcity).mark_line().encode(
    x=alt.X('Date:T', axis=alt.Axis(format='%Y')),
    y=alt.Y('AverageTemperature:Q', axis=alt.Axis(
        title='Average Land Temperature')),
    color=alt.Color('City:N', legend=alt.Legend(
        title="City by colour")),
).properties(title="Monthly Average Temperature by City")

chartpoints = alt.Chart(dfcity).mark_circle(size=30).encode(
    x=alt.X('Date:T'),
    y=alt.Y('AverageTemperature:Q', axis=alt.Axis(
        title='Average Land Temperature')),
    color=alt.Color('City:N', legend=alt.Legend(
        title="City by colour"))
).properties(title="Monthly Average Temperature by City")

yeartemp = dfcity.groupby(['year', 'City'], as_index=False)[
    'AverageTemperature'].mean()


meanchart = alt.Chart(yeartemp).mark_line().encode(
    x=alt.X('year:T', axis=alt.Axis(title="Year", format='%Y')),
    y=alt.Y('AverageTemperature:Q', axis=alt.Axis(
        title='Average Land Temperature')),
    color=alt.Color('City:N', legend=alt.Legend(
        title="City by colour"))
).properties(title="Annual Average Temperature by City")

meanchart_points = alt.Chart(yeartemp).mark_circle(size=30).encode(
    x=alt.X('year:T'),
    y=alt.Y('AverageTemperature:Q', axis=alt.Axis(
        title='Average Land Temperature')),
    color=alt.Color('City:N', legend=alt.Legend(
        title="City by colour"))
).properties(title="Annual Average Temperature by City")

unc_chartline = alt.Chart(dfcity).mark_line().encode(
    x=alt.X('Date:T', axis=alt.Axis(format='%Y')),
    y=alt.Y('AverageTemperatureUncertainty:Q', axis=alt.Axis(
        title='Average Temperature Uncertainty')),
    color=alt.Color('City:N', legend=alt.Legend(
        title="City by colour"))
).properties(title="95th CI for Temperatures")

unc_chartarea = alt.Chart(dfcity).mark_area(opacity=0.5).encode(
    x=alt.X('Date:T', axis=alt.Axis(format='%Y')),
    y=alt.Y('AverageTemperatureUncertainty:Q', axis=alt.Axis(
        title='Average Temperature Uncertainty')),
    color=alt.Color('City:N', legend=alt.Legend(
        title="City by colour"))
).properties(title="95th CI for Temperatures")

tab1, tab2 = st.tabs(["Annual Mean", "Monthly Mean"])

with tab1:
    st.altair_chart((meanchart + meanchart_points).interactive(),
                    use_container_width=True)

with tab2:             
    st.altair_chart((chart + chartpoints).interactive(), use_container_width=True)

tab3, tab4 = st.tabs(["Line Chart", "Area Chart"])

with tab3:
    st.altair_chart((unc_chartline).interactive(), use_container_width=True)

with tab4:
    st.altair_chart((unc_chartarea).interactive(), use_container_width=True)