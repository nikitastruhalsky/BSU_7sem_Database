from sqlalchemy import create_engine
import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")
name = 'DS_lab2'
user = 'postgres'
password = '1234'
port = 9248
engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@localhost:{port}/{name}"
)

st.header("Стругальский Никита Борисович, 4 группа, 4 курс, 2023")

exchanges = pd.read_sql_query(f"SELECT * FROM exchanges", con=engine)
st.session_state["exchanges"] = exchanges
