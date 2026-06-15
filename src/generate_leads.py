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

lead_sources = np.random.choice(
    [
        "Organic Search",
        "LinkedIn Ads",
        "Google Ads",
        "Referral",
        "Email Campaign",
        "Webinar"
    ],
    size=N_LEADS,
    p=[
        0.30,   # Organic Search
        0.25,   # LinkedIn
        0.20,   # Google
        0.12,   # Referral
        0.08,   # Email
        0.05    # Webinar
    ]
)

mql_rates = {
    "Organic Search": 0.55,
    "LinkedIn Ads": 0.45,
    "Google Ads": 0.35,
    "Referral": 0.65,
    "Email Campaign": 0.30,
    "Webinar": 0.25
}

sql_rates = {
    "Organic Search": 0.70,
    "LinkedIn Ads": 0.60,
    "Google Ads": 0.50,
    "Referral": 0.75,
    "Email Campaign": 0.45,
    "Webinar": 0.40
}

win_rates = {
    "Organic Search": 0.28,
    "LinkedIn Ads": 0.22,
    "Google Ads": 0.18,
    "Referral": 0.35,
    "Email Campaign": 0.15,
    "Webinar": 0.12
}

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


# -----------------------------
# Funnel Logic
# -----------------------------

# Lead → MQL

leads["mql_flag"] = leads["lead_source"].apply(
    lambda x: bool(np.random.binomial(1, mql_rates[x]))
)


# MQL → SQL

leads["sql_flag"] = leads.apply(
    lambda row: (
        bool(
            np.random.binomial(
                1,
                sql_rates[row["lead_source"]]
            )
        )
        if row["mql_flag"]
        else False
    ),
    axis=1
)

# SQL → Converted

leads["converted"] = leads.apply(
    lambda row: (
        bool(
            np.random.binomial(
                1,
                win_rates[row["lead_source"]]
            )
        )
        if row["sql_flag"]
        else False
    ),
    axis=1
)
# Lead Status

leads["lead_status"] = np.where(
    leads["converted"],
    "Converted",
    np.where(
        leads["sql_flag"],
        "SQL",
        np.where(
            leads["mql_flag"],
            "MQL",
            "Open"
        )
    )
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