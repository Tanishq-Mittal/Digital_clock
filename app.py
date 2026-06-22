import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

st.title("🕒 Digital Clock")

india_time = datetime.now(ZoneInfo("Asia/Kolkata"))

st.write("Current Time:")
st.code(india_time.strftime("%H:%M:%S %p"))

st.write("Current Date:")
st.code(india_time.strftime("%d/%m/%Y"))
