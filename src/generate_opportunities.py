import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# ----------------------------------------
# Database Connection
# ----------------------------------------

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
# Load Dimension Tables
# ----------------------------------------

customers = pd.read_sql(
    """
    SELECT
        customer_id,
        company_size,
        region
    FROM dim_customer
    """,
    engine
)

sales_reps = pd.read_sql(
    """
    SELECT
        sales_rep_id,
        sales_rep_name,
        territory
    FROM dim_sales_rep
    """,
    engine
)

products = pd.read_sql(
    """
    SELECT
        product_id,
        product_name,
        plan_tier
    FROM dim_product
    """,
    engine
)

# ----------------------------------------
# Configuration
# ----------------------------------------

np.random.seed(42)

N_OPPORTUNITIES = 25000

# ----------------------------------------
# Create Opportunities
# ----------------------------------------

opportunities = pd.DataFrame({

    "opportunity_id": range(
        1,
        N_OPPORTUNITIES + 1
    ),

    "customer_id": np.random.choice(
        customers["customer_id"],
        N_OPPORTUNITIES
    ),

    "sales_rep_id": np.random.choice(
        sales_reps["sales_rep_id"],
        N_OPPORTUNITIES
    ),

    "product_id": np.random.choice(
        products["product_id"],
        N_OPPORTUNITIES
    )
})

# ----------------------------------------
# Enrich Dataset
# ----------------------------------------

opportunities = opportunities.merge(
    customers,
    on="customer_id",
    how="left"
)

opportunities = opportunities.merge(
    sales_reps,
    on="sales_rep_id",
    how="left"
)

opportunities = opportunities.merge(
    products,
    on="product_id",
    how="left"
)

# ----------------------------------------
# Rep Performance Tiers
# ----------------------------------------

rep_factor = {}

for rep in sales_reps["sales_rep_id"]:

    rep_factor[rep] = np.random.choice(
        [0.85, 1.00, 1.15, 1.30],
        p=[0.20, 0.50, 0.20, 0.10]
    )

# ----------------------------------------
# Territory Multipliers
# ----------------------------------------

territory_multiplier = {
    "North America": 1.35,
    "Europe": 1.15,
    "APAC": 0.95,
    "LATAM": 0.85
}

# ----------------------------------------
# Product Base Value
# ----------------------------------------

product_value = {
    "Starter CRM": 1200,
    "Growth CRM": 3600,
    "Enterprise CRM": 12000
}

# ----------------------------------------
# Company Size Multiplier
# ----------------------------------------

company_multiplier = {
    "SMB": 1.0,
    "Mid-Market": 2.0,
    "Enterprise": 4.0
}

# ----------------------------------------
# Revenue Logic
# ----------------------------------------

opportunities["expected_revenue"] = (

    opportunities["product_name"]
    .map(product_value)

    *

    opportunities["company_size"]
    .map(company_multiplier)

    *

    opportunities["territory"]
    .map(territory_multiplier)

    *

    opportunities["sales_rep_id"]
    .map(rep_factor)

    *

    np.random.randint(
        1,
        11,
        N_OPPORTUNITIES
    )

)

opportunities["expected_revenue"] = (
    opportunities["expected_revenue"]
    .round(0)
)

# ----------------------------------------
# Territory Sales Cycles
# ----------------------------------------

cycle_means = {
    "North America": 85,
    "Europe": 95,
    "LATAM": 100,
    "APAC": 110
}

opportunities["sales_cycle_days"] = (

    opportunities["territory"]

    .map(cycle_means)

    .apply(
        lambda x: max(
            15,
            int(
                np.random.normal(
                    x,
                    15
                )
            )
        )
    )
)

# ----------------------------------------
# Opportunity Dates
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
# Win Rates by Territory
# ----------------------------------------

win_rates = {
    "North America": 0.20,
    "Europe": 0.17,
    "LATAM": 0.15,
    "APAC": 0.14
}

opportunities["won"] = (

    opportunities["territory"]

    .apply(
        lambda x:
        np.random.rand()
        < win_rates[x]
    )
)

# ----------------------------------------
# Stage Logic
# ----------------------------------------

opportunities["stage"] = np.where(

    opportunities["won"],

    "Closed Won",

    np.random.choice(
        [
            "Qualification",
            "Discovery",
            "Proposal",
            "Negotiation",
            "Closed Lost"
        ],
        size=N_OPPORTUNITIES,
        p=[
            0.25,
            0.25,
            0.20,
            0.15,
            0.15
        ]
    )
)

# ----------------------------------------
# Actual Revenue
# ----------------------------------------

opportunities["actual_revenue"] = np.where(

    opportunities["won"],

    opportunities["expected_revenue"],

    0
)

# ----------------------------------------
# Keep Fact Columns Only
# ----------------------------------------

fact_opportunities = opportunities[[
    "opportunity_id",
    "customer_id",
    "sales_rep_id",
    "product_id",
    "opportunity_created_date",
    "close_date",
    "stage",
    "expected_revenue",
    "actual_revenue",
    "sales_cycle_days",
    "won"
]]

# ----------------------------------------
# Save
# ----------------------------------------

fact_opportunities.to_csv(
    "data/raw/fact_opportunities.csv",
    index=False
)

# ----------------------------------------
# Validation
# ----------------------------------------

print("\nOpportunity Summary")
print("-" * 50)

print(
    fact_opportunities[
        [
            "expected_revenue",
            "actual_revenue",
            "sales_cycle_days"
        ]
    ].describe()
)

print("\nWin Rate")

print(
    round(
        fact_opportunities["won"].mean() * 100,
        2
    ),
    "%"
)

print(
    f"\nGenerated {len(fact_opportunities):,} opportunities"
)