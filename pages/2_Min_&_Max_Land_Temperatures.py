import streamlit as st
import altair as alt
from Main_Page import dftemp

st.title("Minimum and Maximum Land Temperatures")
st.sidebar.markdown("# Minimum and Maximum Land Temperatures")
st.sidebar.markdown("This page shows the extremes of the land temperature averages, so both the maximum and minimum land temperatures. Once more they are split into different graphs, where the annual maximum and minimum has been put into a bar chart. The monthly maximums and minimums have been put into their own charts that are simple line charts. Underneath it is possible to view the 95th confidence interval of both the maximum and minimum in their own area charts. The user has a slider where they can choose the year range they want to inspect.")

# SLIDERS
year_range = st.slider('Select a year range', 1750, 2015, (1900, 2000))
dftemp = dftemp[(dftemp['year'].astype(int) >= year_range[0])
                & (dftemp['year'].astype(int) <= int(year_range[1]))]


# GROUPING RELEVANT DATA AND CALCULATING MEAN
yeartempmax = dftemp.groupby(['year'], as_index=False)[
    'LandMaxTemperature'].mean()
yeartempmin = dftemp.groupby(['year'], as_index=False)[
    'LandMinTemperature'].mean()

# MAX TEMPERATURE CHARTS
maxchart = alt.Chart(dftemp).mark_line().encode(
    x=alt.X('Date:T', axis=alt.Axis(format='%Y', title='Year')),
    y=alt.Y('LandMaxTemperature:Q', axis=alt.Axis(
        title='Land Temperature')),
    color=alt.value('orange')
).properties(title="Monthly Maximum Average Land Temperature")

maxchartpoints = alt.Chart(dftemp).mark_circle(size=30).encode(
    x=alt.X('Date:T'),
    y=alt.Y('LandMaxTemperature:Q', axis=alt.Axis(
        title='Land Temperature')),
    color=alt.value('orange')
).properties(title="Monthly Maximum Average Land Temperature")

maxchart_mean = alt.Chart(yeartempmax).mark_bar().encode(
    x=alt.X('year:T', axis=alt.Axis(title='Year')),
    y=alt.Y('LandMaxTemperature:Q', axis=alt.Axis(
        title='Land Temperature')),
    color=alt.value('orange')
).properties(title="Annual Min & Max Average Land Temperature")

maxchartpoints_mean = alt.Chart(yeartempmax).mark_circle(size=30).encode(
    x=alt.X('year:T', axis=alt.Axis(title='Year')),
    y=alt.Y('LandMaxTemperature:Q', axis=alt.Axis(
        title='Land Temperature')),
    color=alt.value('orange')
).properties(title="Annual Min & Max Average Land Temperature")

# MIN TEMPERATURE CHARTS
minchart = alt.Chart(dftemp).mark_line().encode(
    x=alt.X('Date:T', axis=alt.Axis(format='%Y', title='Year')),
    y=alt.Y('LandMinTemperature:Q', axis=alt.Axis(
        title='Land Temperature')),
    color=alt.value('cyan')
).properties(title="Monthly Minimum Average Land Temperature")

minchartpoints = alt.Chart(dftemp).mark_circle(size=30).encode(
    x=alt.X('Date:T'),
    y=alt.Y('LandMinTemperature:Q', axis=alt.Axis(
        title='Land Temperature')),
    color=alt.value('cyan')
).properties(title="Monthly Minimum Average Land Temperature")

minchart_mean = alt.Chart(yeartempmin).mark_bar().encode(
    x=alt.X('year:T', axis=alt.Axis(title='Year')),
    y=alt.Y('LandMinTemperature:Q', axis=alt.Axis(
        title='Land Temperature')),
    color=alt.value('cyan')
).properties(title="Annual Min & Max Average Land Temperature")

minchartpoints_mean = alt.Chart(yeartempmin).mark_circle(size=30).encode(
    x=alt.X('year:T', axis=alt.Axis(title='Year')),
    y=alt.Y('LandMinTemperature:Q', axis=alt.Axis(
        title='Land Temperature')),
    color=alt.value('cyan')
).properties(title="Annual Min & Max Average Land Temperature")

unc_chartmax = alt.Chart(dftemp).mark_area(opacity=0.5).encode(
    x=alt.X('Date:T', axis=alt.Axis(format='%Y')),
    y=alt.Y('LandMaxTemperatureUncertainty:Q', axis=alt.Axis(
        title='Average Temperature Uncertainty'), stack=None),
    color=alt.value('orange')
).properties(title="95th CI for Temperatures")

unc_chartmin = alt.Chart(dftemp).mark_area(opacity=0.5).encode(
    x=alt.X('Date:T', axis=alt.Axis(format='%Y')),
    y=alt.Y('LandMinTemperatureUncertainty:Q', axis=alt.Axis(
        title='Average Temperature Uncertainty'), stack=None),
    color=alt.value('cyan')
).properties(title="95th CI for Temperatures")

# TABS WITH MONTHLY MIN AND MAX TEMPERATURES
tab1, tab2, tab3 = st.tabs(["Annual Maximum & Minimum", "Monthly Maximum", "Monthly Minimum"])

with tab1:
    st.altair_chart(
        (maxchart_mean + minchart_mean).interactive(), use_container_width=True)
    

with tab2:
    st.altair_chart((maxchart + maxchartpoints).interactive(),
                    use_container_width=True)
    

with tab3:
    st.altair_chart((minchart + minchartpoints).interactive(),
                    use_container_width=True)

tab4, tab5 = st.tabs(["95th CI Max", "95th CI Min"])

with tab4:
    st.altair_chart((unc_chartmax).interactive(),
                    use_container_width=True)

with tab5:
    st.altair_chart((unc_chartmin).interactive(),
                    use_container_width=True)
