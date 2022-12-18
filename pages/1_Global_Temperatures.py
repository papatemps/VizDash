import streamlit as st
import altair as alt
from Main_Page import dftemp

st.title("Global Temperatures")
st.sidebar.markdown("# Temperatures globally")
st.sidebar.markdown("This page contains different global temperatures, herein the annual and monthly means for land temperatures and temperatures for land and ocean combined. Furthermore, it is also possible to view the 95th confidence interval for both land and land/ocean. All the charts are line charts. The user can choose the range of years that they wish to plot.")

# SLIDERS
year_range = st.slider('Select a year range', 1750, 2015, (1900, 2000))
dftemp = dftemp[(dftemp['year'].astype(int) >= year_range[0])
                & (dftemp['year'].astype(int) <= int(year_range[1]))]

yearland = dftemp.groupby(['year'], as_index=False)[
    'LandAverageTemperature'].mean()

yearocean = dftemp.groupby(['year'], as_index=False)[
    'LandAndOceanAverageTemperature'].mean()

# TABS WITH LAND AND LAND/OCEAN TEMPERATURES
tab1, tab2, tab3, tab4 = st.tabs(["Annual Land Only", "Annual Land and Ocean", "Monthly Land Only", "Monthly Land and Ocean"])

with tab1:
    st.header("Annual Mean for Land Temperatures")
    st.line_chart(yearland, x='year', y='LandAverageTemperature')

    st.header("95th CI for Land Temperatures")
    st.line_chart(dftemp, x='Date', y='LandAverageTemperatureUncertainty')

with tab2:
    st.header("Annual Mean for Land and Ocean Temperatures")
    st.line_chart(yearocean, x='year', y='LandAndOceanAverageTemperature')

    st.header("95th CI for Land & Ocean Temperatures")
    st.line_chart(dftemp, x='Date',
                  y='LandAndOceanAverageTemperatureUncertainty')

with tab3:
    st.header("Monthly Mean for Land Temperatures")
    st.line_chart(dftemp, x='Date', y='LandAverageTemperature')

    st.header("95th CI for Land Temperatures")
    st.line_chart(dftemp, x='Date', y='LandAverageTemperatureUncertainty')

with tab4:
    st.header("Monthly Mean for Land & Ocean Temperatures")
    st.line_chart(dftemp, x='Date', y='LandAndOceanAverageTemperature')

    st.header("95th CI for Land & Ocean Temperatures")
    st.line_chart(dftemp, x='Date',
                  y='LandAndOceanAverageTemperatureUncertainty')