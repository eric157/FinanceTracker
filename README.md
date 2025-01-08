# 📊 **FinanceTracker** 📈

Welcome to the **Universal Finance Tracker**! This project allows you to explore the **historical performance** of stocks or assets, including **closing prices**, **trading volumes**, and **candlestick charts** over a customizable date range. 🚀

Built with **Streamlit** for interactive web-based interfaces, **Plotly** for rich visualizations, and **Yahoo Finance API** (`yfinance`) to fetch stock data, this tool provides an easy way to track financial trends and make informed decisions. 💡
# FinanceTracker
A finance tracking app for stocks, indices, commodities, and more

---

## 🛠️ **Features**

- **Interactive User Interface**:
  - 🏷️ Enter a stock ticker symbol (e.g., `GOOGL`, `AAPL`) and get a historical performance view.
  - 📅 Choose a custom date range to analyze stock data.

- **Visualizations**:
  - 📉 Line charts for **Closing Prices** and **Trading Volumes**.
  - 📈 Interactive **Candlestick Chart** for price movements.

- **Data Source**:
  - 🌐 Utilizes **Yahoo Finance** to fetch real-time and historical stock data.
  
- **Streamlit Sidebar**:
  - 🔧 Input options for stock ticker and date range.
  - ⚠️ Error handling and warnings for invalid inputs.

---

## 📥 **Prerequisites**

Before you start, ensure you have the following installed:

- 🐍 Python 3.x
- Required libraries:
  - `yfinance` 📊
  - `streamlit` 🌐
  - `plotly` 📉

You can install the necessary dependencies by running:

```bash
pip install yfinance streamlit plotly
```

---

## 🚀 **How to Run the Application**

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/FinanceTracker.git
    cd FinanceTracker
    ```

2. Run the Streamlit app:

    ```bash
    streamlit run financeTracker.py
    ```

3. Open the provided URL (typically `http://localhost:8501`) in your browser to start using the finance tracker. 🌍

---

## 🔎 **Usage**

1. **Enter Stock Details**:
   - On the left sidebar, input the stock ticker (e.g., `GOOGL` for Google, `AAPL` for Apple).
   - 🗓️ Select a start and end date to define the period of historical data you want to view.

2. **View Data**:
   - The app will display:
     - 📉 A line chart showing the **closing prices** for the selected date range.
     - 📊 A line chart of **trading volumes** over the same period.
     - 📈 A **candlestick chart** showing the open, high, low, and close prices for each day in the range.

---

## ⚠️ **Error Handling**

- ❌ If an invalid stock ticker or date range is provided, appropriate error messages will be displayed.
- 🚫 If no data is available for the selected stock or period, a warning will appear.

---

## 🛠️ **Customization**

Feel free to adjust or enhance the app by modifying:

- 🎨 **Styling**: The app uses custom CSS for a more appealing user interface.
- 📅 **Date Ranges**: Change the default 90-day range or adjust the data-fetching logic.
- 📊 **Additional Features**: Add more technical indicators, moving averages, or financial reports to enhance the tool.

---

## 🎯 **Example**

You can start by entering a stock symbol (e.g., `GOOGL`), selecting a start date (e.g., 90 days ago), and an end date (e.g., today). The app will generate the following charts:

1. **📉 Closing Price Chart**
2. **📊 Trading Volume Chart**
3. **📈 Candlestick Chart**

---


## 🙏 **Acknowledgements**

- **Streamlit**: For creating a powerful tool for building interactive apps. 🚀
- **Yahoo Finance API**: For providing reliable financial data. 💡
- **Plotly**: For rendering interactive and visually appealing charts. 🎨

---

Enjoy using **Finance Tracker** to keep track of your investments and make informed decisions! 📊💼
