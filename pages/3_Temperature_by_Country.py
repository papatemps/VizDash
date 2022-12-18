import streamlit as st
import altair as alt
from Main_Page import dfcountry


st.title("Temperatures by Country")
st.sidebar.markdown("# Temperatures sorted by Country")
st.sidebar.markdown("The temperatures by country are plotted into line charts along with their 95th confidence interval underneath them, and the user is able to choose the year range with a slider, as well as choose which countries (and other regions/islands) they want to plot by using a multiselect field.")

year_range = st.slider('Select a year range', 1750, 2015, (1900, 2000))

dfcountry = dfcountry[(dfcountry['year'].astype(int) >= year_range[0]) & (
    dfcountry['year'].astype(int) <= int(year_range[1]))]

country_list = dfcountry['Country'].unique().tolist()
options = st.multiselect('Choose countries', country_list)
dfcountry = dfcountry[dfcountry['Country'].isin(options)]

chart = alt.Chart(dfcountry).mark_line().encode(
    x=alt.X('Date:T', axis=alt.Axis(format='%Y')),
    y=alt.Y('AverageTemperature:Q', axis=alt.Axis(
        title='Average Land Temperature')),
    color=alt.Color('Country:N', legend=alt.Legend(
        title="Country by colour"))
).properties(title="Monthly Average Temperature by Country")

chartpoints = alt.Chart(dfcountry).mark_circle(size=30).encode(
    x=alt.X('Date:T'),
    y=alt.Y('AverageTemperature:Q', axis=alt.Axis(
        title='Average Land Temperature')),
    color=alt.Color('Country:N', legend=alt.Legend(
        title="Country by colour"))
).properties(title="Monthly Average Temperature by Country")

yeartemp = dfcountry.groupby(['year', 'Country'], as_index=False)[
    'AverageTemperature'].mean()

meanchart = alt.Chart(yeartemp).mark_line().encode(
    x=alt.X('year:T', axis=alt.Axis(title="Year", format='%Y')),
    y=alt.Y('AverageTemperature:Q', axis=alt.Axis(
        title='Average Land Temperature')),
    color=alt.Color('Country:N', legend=alt.Legend(
        title="Country by colour"))
).properties(title="Annual Average Temperature by Country")

meanchart_points = alt.Chart(yeartemp).mark_circle(size=30).encode(
    x=alt.X('year:T'),
    y=alt.Y('AverageTemperature:Q', axis=alt.Axis(
        title='Average Land Temperature')),
    color=alt.Color('Country:N', legend=alt.Legend(
        title="Country by colour"))
).properties(title="Annual Average Temperature by Country")

unc_chart = alt.Chart(dfcountry).mark_line().encode(
    x=alt.X('Date:T', axis=alt.Axis(format='%Y')),
    y=alt.Y('AverageTemperatureUncertainty:Q', axis=alt.Axis(
        title='Average Temperature Uncertainty')),
    color=alt.Color('Country:N', legend=alt.Legend(
        title="Country by colour"))
).properties(title="95th CI in Temperatures")

tab1, tab2 = st.tabs(["Annual Mean", "Monthly Mean"])

with tab1:
    st.altair_chart((meanchart + meanchart_points).interactive(),
                    use_container_width=True)

with tab2:
    st.altair_chart((chart + chartpoints).interactive(), use_container_width=True)

st.altair_chart((unc_chart).interactive(), use_container_width=True)



# def get_chart(dfcountry):
#     chart = alt.Chart(dfcountry).mark_line().encode(
#         x=alt.X('Date:T', axis=alt.Axis(format='%Y')),
#         y=alt.Y('AverageTemperature:Q', axis=alt.Axis(
#             title='Average Land Temperature')),
#         color=alt.Color('Country:N', legend=alt.Legend(
#             title="Country by colour"))
#     ).properties(title="Average Temperature by Country")

#     hover = alt.selection_single(
#         fields=["Date"],
#         nearest=True,
#         on="mouseover",
#         empty="none"
#     )

#     points = chart.transform_filter(hover).mark_circle(size=65)

#     tooltips = (
#         alt.Chart(dfcountry).mark_rule().encode(
#             x="Date",
#             y="AverageTemperature",
#             opaCountry=alt.condition(hover, alt.value(0.3), alt.value(0)),
#             tooltip=[
#                 alt.Tooltip("Date", title="Date", format='%Y'),
#                 alt.Tooltip("AverageTemperature",
#                             title="Average Land Temperature"),
#             ],
#         ).add_selection(hover)
#     )
#     return (chart + points + tooltips).interactive()


# fullchart = get_chart(dfcountry)
# st.altair_chart(fullchart, use_container_width=True)
