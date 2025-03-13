import pandas as pd
import sqlite3
import yfinance as yf

print("Starting ETL process...")

# Extract - Fetch S&P 500 price movements data from Yahoo Finance
symbol = "SPY"
print(f"Fetching data for {symbol} from Yahoo Finance...")
data = yf.download(symbol, start="2000-01-20", end="2025-01-19")
print("Data fetched successfully!")

# Transform - Extract useful information
print("Transforming data...")
data.reset_index(inplace=True)
data = data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
data.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
data['percent_change'] = (data['close']-data['open'])/data['open']*100
print("Data transformed successfully!")

# Load - Save the data to a SQLite database
print("Loading data into SQLite database...")
conn = sqlite3.connect("etl_pipeline_project/database/sp500_price_data.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS sp500_prices (
               date TEXT, 
               open REAL, 
               high REAL, 
               low REAL, 
               close REAL, 
               volume INTEGER, 
               percent_change REAL
               )''')
data.to_sql("sp500_prices", conn, if_exists="replace", index=False)
conn.commit()
conn.close()
print("ETL process completed! Data saved to sp500_price_data.db")