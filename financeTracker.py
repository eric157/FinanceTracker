import yfinance as yf
import streamlit as st
import datetime

st.set_page_config(page_title="Universal Finance Tracker", layout="wide", page_icon="📈")

st.markdown(
    """
    <style>
    .main {
        background-color: #f7f7f7;
        font-family: 'Arial', sans-serif;
    }
    h1, h2 {
        color: #2E86C1;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Universal Finance Tracker")

st.markdown(
    """
    Shown below are the **historical closing prices** and **trading volumes** for the selected asset.
    """
)

def get_data(symbol, start, end):
    data = yf.Ticker(symbol)
    return data.history(period='1d', start=start, end=end)

def display_stock_info(symbol, start, end):
    data = get_data(symbol, start, end)
    st.subheader("Closing Price")
    st.line_chart(data.Close, use_container_width=True)
    st.subheader("Volume")
    st.line_chart(data.Volume, use_container_width=True)

with st.sidebar:
    st.header("ENTER:")
    symbol = st.text_input("Enter Stock Ticker", "GOOGL").upper()
    start_date = st.date_input("Start Date", datetime.date(2014, 12, 24))
    end_date = st.date_input("End Date", datetime.date.today())

if start_date < end_date:
    display_stock_info(symbol, start_date, end_date)
else:
    st.error("End date must be after start date.")
