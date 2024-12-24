import yfinance as yf
import streamlit as st
import datetime
import plotly.graph_objects as go

st.set_page_config(page_title="Universal Finance Tracker", layout="wide", page_icon="📈")

st.markdown(
    """
    <style>
    /* Overall page styling */
    .main {
        background: #F4F7FA;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #2E3A59;
        line-height: 1.6;
        padding: 20px;
    }

    /* Header Styling */
    h1 {
        font-size: 3.5rem;
        color: #ffffff;
        background: linear-gradient(45deg, #0066FF, #4C6EF5);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
        text-align: center;
        letter-spacing: 1px;
    }

    h2 {
        font-size: 2.5rem;
        color: #0066FF;
        margin-top: 20px;
        text-align: center;
    }

    h3 {
        font-size: 1.8rem;
        color: #444;
        margin-top: 20px;
        font-weight: 500;
    }

    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: #003366;
        color: #ffffff;
        border-radius: 16px;
        box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.1);
        padding: 15px;
        margin-right: 20px;
        max-width: 300px;
    }

    .sidebar .sidebar-content h1, .sidebar .sidebar-content h2 {
        color: #ffffff;
        text-transform: uppercase;
    }

    /* Sidebar input styling */
    .sidebar .sidebar-content .stTextInput input {
        background-color: #ffffff;
        color: #333;
        padding: 12px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        width: 100%;
        box-sizing: border-box;
        font-size: 1rem;
        box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.05);
        transition: border-color 0.3s ease;
    }

    .sidebar .sidebar-content .stTextInput input:focus {
        border-color: #0066FF;
    }

    /* Button styling */
    .sidebar .sidebar-content .stButton button {
        background-color: #0066FF;
        color: white;
        padding: 12px;
        border-radius: 10px;
        border: none;
        font-size: 1.2rem;
        font-weight: bold;
        width: 100%;
        cursor: pointer;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease, transform 0.2s ease;
    }

    .sidebar .sidebar-content .stButton button:hover {
        background-color: #0052cc;
        transform: translateY(-2px);
    }

    .sidebar .sidebar-content .stButton button:active {
        background-color: #0041a8;
        transform: translateY(1px);
    }

    /* Content Area Styling */
    .stTable, .stLineChart {
        border-radius: 12px;
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.1);
        padding: 20px;
        background-color: #ffffff;
        margin-top: 20px;
        overflow: hidden;
        box-sizing: border-box;
    }

    .stTable {
        border-collapse: collapse;
        width: 100%;
    }

    .stTable th, .stTable td {
        padding: 12px;
        text-align: left;
        border-bottom: 1px solid #e0e0e0;
    }

    .stTable th {
        background-color: #F4F7FA;
        color: #0066FF;
    }

    .stTable tr:hover {
        background-color: #F1F5FF;
    }

    .stLineChart {
        background-color: #fafafa;
        padding: 25px;
        box-sizing: border-box;
    }

    /* Alerts (Error, Warning) */
    .stError {
        background-color: #F8D7DA;
        color: #842029;
        border: 1px solid #F5C6CB;
        border-radius: 10px;
        padding: 12px;
        box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.05);
        font-size: 1rem;
    }

    .stWarning {
        background-color: #FFF3CD;
        color: #856404;
        border: 1px solid #FFEBAA;
        border-radius: 10px;
        padding: 12px;
        box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.05);
        font-size: 1rem;
    }

    /* Footer (Optional) */
    .footer {
        text-align: center;
        font-size: 1rem;
        color: #888;
        margin-top: 40px;
    }

    /* Transitions for smoother interactivity */
    * {
        transition: all 0.3s ease;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Universal Finance Tracker")

st.markdown(
    """
    Welcome to the **Universal Finance Tracker**! Here, you can explore the **historical performance**, including **closing prices** and **trading volumes**, for any stock or asset over your chosen time period.
    """
)

@st.cache_data
def get_data(symbol, start, end):
    data = yf.Ticker(symbol)
    try:
        return data.history(period='1d', start=start, end=end)
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

def display_stock_info(symbol, start, end):
    data = get_data(symbol, start, end)
    if data is not None and not data.empty:
        st.subheader("Closing Price")
        st.line_chart(data.Close, use_container_width=True)

        st.subheader("Volume")
        st.line_chart(data.Volume, use_container_width=True)

        st.subheader("Candlestick Chart")
        fig = go.Figure(data=[go.Candlestick(x=data.index,
                                            open=data['Open'],
                                            high=data['High'],
                                            low=data['Low'],
                                            close=data['Close'])])
        fig.update_layout(title=f"{symbol} Candlestick Chart", xaxis_title="Date", yaxis_title="Price")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data available for the selected symbol and date range.")

today = datetime.date.today()
ninety_days_ago = today - datetime.timedelta(days=90)

with st.sidebar:
    st.header("ENTER STOCK DETAILS:")
    symbol = st.text_input("Enter Stock Ticker", "GOOGL").upper()
    start_date = st.date_input("Start Date", ninety_days_ago)
    end_date = st.date_input("End Date", today)

    if start_date >= end_date:
        st.sidebar.error("End date must be after start date.")

if start_date < end_date:
    if symbol:
        display_stock_info(symbol, start_date, end_date)
    else:
        st.error("Please enter a valid stock ticker symbol.")
else:
    st.error("Please select a valid date range.")
