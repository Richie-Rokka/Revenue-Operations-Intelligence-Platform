import pandas as pd
import numpy as np

np.random.seed(42)

# ----------------------------------------
# Load Customer Dimension
# ----------------------------------------

customers = pd.read_csv(
    "data/raw/dim_customer.csv"
)

# ----------------------------------------
# Configuration
# ----------------------------------------

N_LEADS = 100000

lead_sources = [
    "Google Ads",
    "LinkedIn Ads",
    "Referral",
    "Webinar",
    "Organic Search",
    "Email Campaign"
]

industries = [
    "Technology",
    "Healthcare",
    "Finance",
    "Retail",
    "Manufacturing"
]

company_sizes = [
    "SMB",
    "Mid-Market",
    "Enterprise"
]

regions = [
    "North America",
    "Europe",
    "APAC",
    "LATAM"
]

# ----------------------------------------
# Generate Leads
# ----------------------------------------

leads = pd.DataFrame({

    "lead_id": range(
        1,
        N_LEADS + 1
    ),

    "customer_id": np.random.choice(
        customers["customer_id"].values,
        N_LEADS
    ),

    "created_date": pd.to_datetime(
        np.random.choice(
            pd.date_range(
                "2022-01-01",
                "2026-12-31"
            ),
            N_LEADS
        )
    ),

    "lead_source": np.random.choice(
        lead_sources,
        N_LEADS
    ),

    "industry": np.random.choice(
        industries,
        N_LEADS
    ),

    "company_size": np.random.choice(
        company_sizes,
        N_LEADS
    ),

    "engagement_score": np.random.randint(
        1,
        101,
        N_LEADS
    ),

    "region": np.random.choice(
        regions,
        N_LEADS
    )
})

# ----------------------------------------
# Funnel Logic
# ----------------------------------------

leads["mql_flag"] = (
    leads["engagement_score"] >= 60
)

leads["sql_flag"] = (
    leads["engagement_score"] >= 75
)

leads["converted"] = (
    leads["engagement_score"] >= 85
)

leads["lead_status"] = np.where(
    leads["converted"],
    "Converted",
    "Open"
)

# ----------------------------------------
# Save
# ----------------------------------------

leads.to_csv(
    "data/raw/fact_leads.csv",
    index=False
)

print(f"Generated {len(leads):,} leads")
print(leads.head())