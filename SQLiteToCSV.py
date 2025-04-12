import sqlite3
import pandas as pd
import os

# Path to your SQLite file
db_path = r"C:\Users\Student\SQL-Project\mental_health.sqlite"

# Output directory for CSVs
output_dir = r"C:\Users\Student\SQL-Project\sqlite_csv_export"
os.makedirs(output_dir, exist_ok=True)

# Connect to SQLite DB
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get list of tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Export each table to CSV
for (table_name,) in tables:
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    csv_file = os.path.join(output_dir, f"{table_name}.csv")
    df.to_csv(csv_file, index=False)
    print(f"Exported {table_name} to {csv_file}")

conn.close()
