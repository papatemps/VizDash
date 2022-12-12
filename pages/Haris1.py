import streamlit as st

st.markdown("# Haris 1 hehe")
st.sidebar.markdown("# Haris 1 hehe")

x = st.slider('x')
st.write(x, 'squared is', x * x)