import streamlit as st
from datetime import datetime

st.title("🕒 Digital Clock")

current_time = datetime.now().strftime("%H:%M:%S %p")
current_date = datetime.now().strftime("%d/%m/%Y")

st.markdown(f"## {current_time}")
st.markdown(f"### {current_date}")
