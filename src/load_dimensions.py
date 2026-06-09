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

print("Loading dim_product...")
print("Loading dim_sales_rep...")
print("Loading dim_customer...")

# Read CSV files
products = pd.read_csv("data/raw/dim_product.csv")
sales_reps = pd.read_csv("data/raw/dim_sales_rep.csv")
customers = pd.read_csv("data/raw/dim_customer.csv")

# Load into PostgreSQL
products.to_sql(
    "dim_product",
    engine,
    if_exists="append",
    index=False
)

sales_reps.to_sql(
    "dim_sales_rep",
    engine,
    if_exists="append",
    index=False
)

customers.to_sql(
    "dim_customer",
    engine,
    if_exists="append",
    index=False
)

print("Dimension tables loaded successfully!")