import sqlite3
import pandas as pd

# Simple query to get the worst days in the SPY ETF

conn = sqlite3.connect("etl_pipeline_project/database/sp500_price_data.db")

query = "SELECT date, percent_change FROM sp500_prices WHERE percent_change < -3 ORDER BY date ASC" 
data = pd.read_sql(query, conn)

conn.close()

print(data)