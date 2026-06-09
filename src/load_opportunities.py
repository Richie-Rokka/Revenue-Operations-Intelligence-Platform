import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv()

connection_url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

engine = create_engine(connection_url)

opportunities = pd.read_csv(
    "data/raw/fact_opportunities.csv"
)

# ----------------------------------------
# Validation
# ----------------------------------------

print("Customer ID Range:")
print(
    opportunities["customer_id"].min(),
    opportunities["customer_id"].max()
)

print("\nSales Rep ID Range:")
print(
    opportunities["sales_rep_id"].min(),
    opportunities["sales_rep_id"].max()
)

print("\nProduct ID Range:")
print(
    opportunities["product_id"].min(),
    opportunities["product_id"].max()
)

# ----------------------------------------
# Assertions
# ----------------------------------------

assert (
    opportunities["customer_id"].min() >= 10001
)

assert (
    opportunities["customer_id"].max() <= 20000
)

assert (
    opportunities["sales_rep_id"].min() >= 201
)

assert (
    opportunities["sales_rep_id"].max() <= 300
)

assert (
    opportunities["product_id"]
    .isin([7, 8, 9])
    .all()
)

# ----------------------------------------
# Load
# ----------------------------------------

opportunities.to_sql(
    "fact_opportunities",
    engine,
    if_exists="append",
    index=False
)

print("Opportunity data loaded successfully!")