# FinSight — Financial Stock Analysis Assistant

FinSight is a Streamlit app powered by OpenAI's GPT-4o and yFinance that lets users ask natural language questions about stock prices and technical indicators. The app dynamically calls Python functions to fetch real-time stock data, compute indicators like SMA, EMA, RSI, MACD, and visualize stock price trends over the past year.

---

## Features

- Conversational chatbot interface to ask about stocks
- Real-time retrieval of stock prices using Yahoo Finance
- Calculation of popular technical indicators:
  - Simple Moving Average (SMA)
  - Exponential Moving Average (EMA)
  - Relative Strength Index (RSI)
  - Moving Average Convergence Divergence (MACD)
- Plotting 1-year stock price trends with Matplotlib
- Integration with OpenAI's Function Calling API for dynamic tool invocation

---

## Project Structure

- `app.py` — Main Streamlit application with chat UI and OpenAI interaction
- `functions.py` — Python implementations of stock price retrieval and technical indicators
- `tools_metadata.py` — Metadata definitions describing functions for OpenAI tool calls
- `openai_client.py` — OpenAI API client initialization

---

## Setup Instructions

1. **Clone the repo.**
   ```bash
   git clone https://github.com/rishabhpoikayil/finsight.git
   cd finsight

2. **Create and activate a virtual environment.**
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate

3. **Install dependencies.**
   ```bash
   pip install -r requirements.txt

4. **Set your OpenAI API key.** <br>
   Create a file named API_KEY in the project root and paste your OpenAI key inside:
    ```bash
    echo "sk-..." > API_KEY

5. **Run the app.**
   ```bash
   streamlit run app.py
