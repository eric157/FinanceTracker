# 📊 **FinanceTracker** 📈

Welcome to the **Universal Finance Tracker**! This project allows you to explore the **historical performance** of stocks or assets, including **closing prices**, **trading volumes**, and **candlestick charts** over a customizable date range. 🚀

Built with **Streamlit** for interactive web-based interfaces, **Plotly** for rich visualizations, and **Yahoo Finance API** (`yfinance`) to fetch stock data, this tool provides an easy way to track financial trends and make informed decisions. 💡

**Live Demo:** [https://finance-track.streamlit.app/](https://finance-track.streamlit.app/)

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
pip install -r requirements.txt
content_copy
download
Use code with caution.
Markdown

Note: You can also install the dependencies individually by running

pip install yfinance streamlit plotly
content_copy
download
Use code with caution.
🚀 How to Run the Application (Locally)

Clone this repository to your local machine:

git clone https://github.com/eric157/FinanceTracker.git
cd FinanceTracker
content_copy
download
Use code with caution.
Bash

Run the Streamlit app:

streamlit run financeTracker.py
content_copy
download
Use code with caution.
Bash

Open the provided URL (typically http://localhost:8501) in your browser to start using the finance tracker. 🌍

🔎 Usage

Enter Stock Details:

On the left sidebar, input the stock ticker (e.g., GOOGL for Google, AAPL for Apple).

🗓️ Select a start and end date to define the period of historical data you want to view.

View Data:

The app will display:

📉 A line chart showing the closing prices for the selected date range.

📊 A line chart of trading volumes over the same period.

📈 A candlestick chart showing the open, high, low, and close prices for each day in the range.

⚠️ Error Handling

❌ If an invalid stock ticker or date range is provided, appropriate error messages will be displayed.

🚫 If no data is available for the selected stock or period, a warning will appear.

🛠️ Customization

Feel free to adjust or enhance the app by modifying:

🎨 Styling: The app uses custom CSS for a more appealing user interface.

📅 Date Ranges: Change the default 90-day range or adjust the data-fetching logic.

📊 Additional Features: Add more technical indicators, moving averages, or financial reports to enhance the tool.

🎯 Example

You can start by entering a stock symbol (e.g., GOOGL), selecting a start date (e.g., 90 days ago), and an end date (e.g., today). The app will generate the following charts:

📉 Closing Price Chart

📊 Trading Volume Chart

📈 Candlestick Chart

🙏 Acknowledgements

Streamlit: For creating a powerful tool for building interactive apps. 🚀

Yahoo Finance API: For providing reliable financial data. 💡

Plotly: For rendering interactive and visually appealing charts. 🎨

Enjoy using Finance Tracker to keep track of your investments and make informed decisions! 📊💼