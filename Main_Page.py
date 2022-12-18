import streamlit as st
import numpy as np
import pandas as pd


def convert_df(df):
    return df.to_csv().encode('utf-8')


st.title("Raw Dataset Showcase")
st.sidebar.markdown("# Raw Dataset Showcase")
st.sidebar.markdown("This page shows the raw datasets used in the making of this dashboard and the graphs within it. We used datasets that gave us global average temperatures, temperature averages by country and also by major city.  Here the data can be explored and it is also possible to download the data as CSV files.")


dft = pd.read_csv('GlobalTemperatures.csv')
dft['year'] = pd.to_datetime(dft['dt']).dt.strftime("%Y")
dft.rename(columns={'dt': 'Date'}, inplace=True)

dfc = pd.read_csv('GlobalLandTemperaturesByCountry.csv')
dfc['year'] = pd.to_datetime(dfc['dt']).dt.strftime("%Y")
dfc.rename(columns={'dt': 'Date'}, inplace=True)

dfmc = pd.read_csv('GlobalLandTemperaturesByMajorCity.csv')
dfmc['year'] = pd.to_datetime(dfmc['dt']).dt.strftime("%Y")
dfmc.rename(columns={'dt': 'Date'}, inplace=True)

dftemp = dft
dfcountry = dfc
dfcity = dfmc

st.markdown("Global Temperatures")
st.dataframe(dftemp, use_container_width=True)
st.download_button(
    label='Download CSV',
    data=convert_df(dftemp),
    file_name='GlobalTemperature.csv',
    mime='text/csv')

st.markdown("Global Land Temperatures by Country")
st.dataframe(dfcountry, use_container_width=True)
st.download_button(
    label='Download CSV',
    data=convert_df(dfcountry),
    file_name='GlobalTemperatureByCountry.csv',
    mime='text/csv')

st.markdown("Global Land Temperatures by Major City")
st.dataframe(dfcity, use_container_width=True)
st.download_button(
    label='Download CSV',
    data=convert_df(dfcity),
    file_name='GlobalTemperatureByMajorCity.csv',
    mime='text/csv')
