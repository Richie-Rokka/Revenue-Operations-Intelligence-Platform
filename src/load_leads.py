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

leads = pd.read_csv(
    "data/raw/fact_leads.csv"
)


print(
    "Lead Count:",
    len(leads)
)

assert (
    "lead_id" in leads.columns
)

assert (
    "customer_id" in leads.columns
)

leads.to_sql(
    "fact_leads",
    engine,
    if_exists="append",
    index=False
)

print("Lead data loaded successfully!")