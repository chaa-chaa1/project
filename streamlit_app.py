import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("진주시 비상소화장치", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    df = df.rename(columns={
        '위도': 'lat',
        '경도': 'lon'
    })

    st.map(df)

    st.dataframe(df)