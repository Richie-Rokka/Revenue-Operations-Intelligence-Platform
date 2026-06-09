import pandas as pd
from faker import Faker
import random

fake = Faker()

# --------------------------
# Product Dimension
# --------------------------

products = pd.DataFrame({
    "product_id": [7, 8, 9],
    "product_name": [
        "Starter CRM",
        "Growth CRM",
        "Enterprise CRM"
    ],
    "plan_tier": [
        "Starter",
        "Growth",
        "Enterprise"
    ],
    "monthly_price": [
        99,
        299,
        999
    ]
})

# --------------------------
# Sales Rep Dimension
# --------------------------

sales_reps = pd.DataFrame({
    "sales_rep_id": range(201, 301),

    "sales_rep_name": [
        fake.name()
        for _ in range(100)
    ],

    "territory": [
        random.choice([
            "North America",
            "Europe",
            "APAC",
            "LATAM"
        ])
        for _ in range(100)
    ],

    "hire_date": [
        fake.date_between(
            start_date="-10y",
            end_date="-1y"
        )
        for _ in range(100)
    ]
})

# --------------------------
# Customer Dimension
# --------------------------

customers = pd.DataFrame({
    "customer_id": range(10001, 20001),

    "customer_name": [
        fake.company()
        for _ in range(10000)
    ],

    "industry": [
        random.choice([
            "Technology",
            "Healthcare",
            "Finance",
            "Retail",
            "Manufacturing"
        ])
        for _ in range(10000)
    ],

    "company_size": [
        random.choice([
            "SMB",
            "Mid-Market",
            "Enterprise"
        ])
        for _ in range(10000)
    ],

    "country": [
        fake.country()
        for _ in range(10000)
    ],

    "region": [
        random.choice([
            "North America",
            "Europe",
            "APAC",
            "LATAM"
        ])
        for _ in range(10000)
    ],

    "acquisition_date": [
        fake.date_between(
            start_date="-4y",
            end_date="today"
        )
        for _ in range(10000)
    ]
})

print(sales_reps.head())

print(sales_reps.columns.tolist())

# ---------------------------------
# Save Dimension Tables
# ---------------------------------

products.to_csv(
    "data/raw/dim_product.csv",
    index=False
)

sales_reps.to_csv(
    "data/raw/dim_sales_rep.csv",
    index=False
)

customers.to_csv(
    "data/raw/dim_customer.csv",
    index=False
)

print("CSV files saved successfully!")

