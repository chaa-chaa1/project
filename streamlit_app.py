import streamlit as st
import pandas as pd
import pydeck as pdk

# 소화기 아이콘 정의
ICON_URL = "https://i.postimg.cc/2jc0dcDK/fire-extinguisher-icon-cursor-32x32.png"

# 데이터 정의 (진주 비상 소화 장치)
data = pd.DataFrame({
    'lat': [35.186973, 35.193525, 35.193956, 35.194058, 35.193629, 35.194087, 35.194413, 35.194561, 35.194345, 35.194707, 35.194976, 35.195263, 35.19485, 35.193816, 35.198762, 35.194143, 35.196067, 35.181216, 35.18379, 35.185007, 35.27549, 35.17059, 35.145915, 35.192003, 35.235063, 35.26434, 35.263328, 35.261892, 35.226602, 35.283471, 35.305003, 35.289305, 35.340751, 35.116731],
    'lon': [128.11661, 128.085195, 128.085071, 128.085805, 128.085644, 128.084908, 128.084785, 128.085414, 128.085532, 128.084664, 128.084567, 128.085322, 128.085498, 128.083967, 128.089517, 128.087345, 128.084445, 128.079159, 128.08881, 128.088449, 128.03109, 128.167451, 128.353869, 128.263979, 128.254845, 128.168969, 128.169231, 128.168459, 128.121389, 128.12142, 128.136347, 128.056208, 128.142771, 128.189791],
    'place': [f"연번 {i+1}" for i in range(34)]
})

# 아이콘 정보 열 추가
data["icon_data"] = None
for i in data.index:
    data.at[i, "icon_data"] = {
        "url": ICON_URL,
        "width": 32,
        "height": 32,
        "anchorY": 32
    }

# pydeck 지도 표시 (기본 스타일)
st.pydeck_chart(pdk.Deck(
    map_style=None,  # Mapbox 스타일 대신 기본 스타일 사용
    initial_view_state=pdk.ViewState(
        latitude=35.226602,
        longitude=128.121389,
        zoom=10
    ),
    layers=[
        pdk.Layer(
            type="IconLayer",
            data=data,
            get_icon="icon_data",
            get_position='[lon, lat]',
            get_size=4,
            size_scale=15,
            pickable=True
        )
    ],
    tooltip={"text": "{place}"}
))