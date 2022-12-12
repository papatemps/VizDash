import streamlit as st
import numpy as np
import pandas as pd

st.markdown("# Main Page")
st.sidebar.markdown("# Main Page")

dftemp = pd.read_csv('GlobalTemperatures.csv')
st.dataframe(dftemp)

