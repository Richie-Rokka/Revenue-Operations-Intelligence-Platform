import pandas as pd
import numpy as np
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

# ----------------------------------------
# Load Actual Dimension Keys
# ----------------------------------------

customers = pd.read_sql(
    "SELECT customer_id FROM dim_customer",
    engine
)

sales_reps = pd.read_sql(
    "SELECT sales_rep_id FROM dim_sales_rep",
    engine
)

products = pd.read_sql(
    "SELECT product_id FROM dim_product",
    engine
)

# ----------------------------------------
# Configuration
# ----------------------------------------

np.random.seed(42)

N_OPPORTUNITIES = 25000

# ----------------------------------------
# Pipeline Stages
# ----------------------------------------

stages = [
    "Qualification",
    "Discovery",
    "Proposal",
    "Negotiation",
    "Closed Won",
    "Closed Lost"
]

stage_probs = [
    0.20,
    0.20,
    0.20,
    0.15,
    0.15,
    0.10
]

# ----------------------------------------
# Create Opportunity Dataset
# ----------------------------------------

opportunities = pd.DataFrame({

    "opportunity_id": range(
        1,
        N_OPPORTUNITIES + 1
    ),

    "customer_id": np.random.choice(
        customers["customer_id"].values,
        N_OPPORTUNITIES
    ),

    "sales_rep_id": np.random.choice(
        sales_reps["sales_rep_id"].values,
        N_OPPORTUNITIES
    ),

    "product_id": np.random.choice(
        products["product_id"].values,
        N_OPPORTUNITIES
    ),

    "stage": np.random.choice(
        stages,
        N_OPPORTUNITIES,
        p=stage_probs
    )
})

# ----------------------------------------
# Revenue Logic
# ----------------------------------------

product_values = {}

for pid in products["product_id"]:
    if pid == products["product_id"].iloc[0]:
        product_values[pid] = 1200
    elif pid == products["product_id"].iloc[1]:
        product_values[pid] = 3600
    else:
        product_values[pid] = 12000

opportunities["expected_revenue"] = (
    opportunities["product_id"]
    .map(product_values)
    *
    np.random.randint(
        1,
        11,
        N_OPPORTUNITIES
    )
)

# ----------------------------------------
# Sales Cycle
# ----------------------------------------

opportunities["sales_cycle_days"] = np.random.randint(
    15,
    180,
    N_OPPORTUNITIES
)

# ----------------------------------------
# Dates
# ----------------------------------------

opportunities["opportunity_created_date"] = pd.to_datetime(
    np.random.choice(
        pd.date_range(
            "2022-01-01",
            "2026-12-31"
        ),
        N_OPPORTUNITIES
    )
)

opportunities["close_date"] = (
    opportunities["opportunity_created_date"]
    +
    pd.to_timedelta(
        opportunities["sales_cycle_days"],
        unit="D"
    )
)

# ----------------------------------------
# Win Logic
# ----------------------------------------

opportunities["won"] = (
    opportunities["stage"] == "Closed Won"
)

opportunities["actual_revenue"] = np.where(
    opportunities["won"],
    opportunities["expected_revenue"],
    0
)

# ----------------------------------------
# Validation
# ----------------------------------------

print(
    "Customer ID Range:",
    opportunities["customer_id"].min(),
    opportunities["customer_id"].max()
)

print(
    "Sales Rep ID Range:",
    opportunities["sales_rep_id"].min(),
    opportunities["sales_rep_id"].max()
)

print(
    "Product ID Range:",
    opportunities["product_id"].min(),
    opportunities["product_id"].max()
)

# ----------------------------------------
# Save
# ----------------------------------------

opportunities.to_csv(
    "data/raw/fact_opportunities.csv",
    index=False
)

print(
    f"Generated {len(opportunities):,} opportunities"
)

print(opportunities.head())