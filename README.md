# 📊 **FinanceTracker** 📈

Welcome to the **Universal Finance Tracker**! This project allows you to explore the **historical performance** of stocks or assets, including **closing prices**, **trading volumes**, and **candlestick charts** over a customizable date range. 🚀

Built with **Streamlit** for interactive web-based interfaces, **Plotly** for rich visualizations, and **Yahoo Finance API** (`yfinance`) to fetch stock data, this tool provides an easy way to track financial trends and make informed decisions. 💡

🔗 **Live Demo:** [Finance Tracker](https://finance-track.streamlit.app/)

---

## 🛠️ Features

### 🔍 **Interactive User Interface**
- 🏷️ Enter a stock ticker symbol (e.g., `GOOGL`, `AAPL`) and get a historical performance view.
- 📅 Choose a custom date range to analyze stock data.

### 📊 **Visualizations**
- 📉 **Closing Prices** and **Trading Volumes** line charts.
- 📈 **Interactive Candlestick Chart** for price movements.

### 📡 **Data Source**
- 🌐 Utilizes **Yahoo Finance** to fetch real-time and historical stock data.

### 🎛️ **Streamlit Sidebar**
- 🔧 Input options for stock ticker and date range.
- ⚠️ Error handling and warnings for invalid inputs.

---

## 📥 Prerequisites

Before you start, ensure you have the following installed:

### 📌 **Required Software**
- 🐍 Python 3.x
- Required libraries:
  - `yfinance` 📊
  - `streamlit` 🌐
  - `plotly` 📉

### 📦 **Installation**
You can install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

Or install them individually:

```bash
pip install yfinance streamlit plotly
```

---

## 🚀 How to Run the Application (Locally)

### 📂 **Clone the Repository**

```bash
git clone https://github.com/eric157/FinanceTracker.git
cd FinanceTracker
```

### ▶️ **Run the Streamlit App**

```bash
streamlit run financeTracker.py
```

### 🌍 **Access the App**

Open the provided URL (typically `http://localhost:8501`) in your browser to start using FinanceTracker.

---

## 🔎 Usage Guide

### 1️⃣ **Enter Stock Details**
- On the left sidebar, input the stock ticker (e.g., `GOOGL` for Google, `AAPL` for Apple).
- 🗓️ Select a start and end date to define the period of historical data you want to view.

### 2️⃣ **View Data**
The app will display:
- 📉 A **line chart** showing closing prices for the selected date range.
- 📊 A **line chart** of trading volumes over the same period.
- 📈 A **candlestick chart** showing the open, high, low, and close prices for each day in the range.

### 3️⃣ **Error Handling**
- ❌ If an invalid stock ticker or date range is provided, appropriate error messages will be displayed.
- 🚫 If no data is available for the selected stock or period, a warning will appear.

---

## 🛠️ Customization

You can enhance or modify the app by adjusting the following:

- 🎨 **Styling:** The app uses custom CSS for a more appealing UI.
- 📅 **Date Ranges:** Modify the default 90-day range or tweak the data-fetching logic.
- 📊 **Additional Features:** Add technical indicators, moving averages, or financial reports to improve decision-making.

---

## 🎯 Example Walkthrough

Start by entering a stock symbol (e.g., `GOOGL`), selecting a start date (e.g., 90 days ago), and an end date (e.g., today). The app will generate the following charts:

✅ **Closing Price Chart**
✅ **Trading Volume Chart**
✅ **Candlestick Chart**

---

## 🙏 Acknowledgements

- 🚀 **Streamlit**: For providing a powerful tool for interactive apps.
- 💡 **Yahoo Finance API**: For reliable financial data.
- 🎨 **Plotly**: For rendering interactive and visually appealing charts.

Enjoy using **FinanceTracker** to monitor your investments and make data-driven financial decisions! 📊💼