# 🚀 Revenue Operations Intelligence Platform

An end-to-end **Revenue Operations (RevOps) analytics platform** that transforms lead, opportunity, customer, product, and sales data into executive insights across the revenue lifecycle.

Built with **Python, PostgreSQL, SQL, Power BI, and DAX**, the platform provides a unified view of funnel performance, pipeline health, sales effectiveness, customer value, and product contribution.

> **Note on Data:** This project uses a synthetic dataset generated to simulate a realistic B2B revenue operations environment. All companies, customers, sales activity, pipeline values, revenue figures, and business outcomes are simulated for analytical and portfolio demonstration purposes.

## 📌 Project Snapshot

| Metric                  |   Value |
| ----------------------- | ------: |
| Leads Analyzed          | 100,000 |
| Opportunities Evaluated |  25,000 |
| Customers Modeled       |  10,000 |
| Revenue Pipeline        |   $2.0B |
| Revenue Generated       | $342.8M |
| Win Rate                |   17.0% |
| Average Deal Size       |  $80.5K |
| Average Sales Cycle     | 96 Days |
| Executive Dashboards    |       4 |

---

# 📊 Dashboard Preview

## Executive Performance Overview

![Executive Performance Overview](assets/page1.png)

## Funnel Performance & Conversion Analytics

![Funnel Performance & Conversion Analytics](assets/page2.png)

## Sales Performance & Territory Intelligence

![Sales Performance & Territory Intelligence](assets/page3.png)

## Product & Customer Intelligence

![Product & Customer Intelligence](assets/page4.png)

---

# 🎯 Business Problem

Revenue organizations often operate with fragmented reporting across Marketing, Sales, and Customer teams.

This makes it difficult to answer critical questions such as:

* Where is revenue leaking through the funnel?
* Which acquisition channels produce the highest-quality opportunities?
* Which territories and sales representatives drive the strongest performance?
* Which customers and products contribute the most revenue?
* How healthy is the current revenue pipeline?

The objective of this project was to build a centralized analytics platform that brings these perspectives together into a single Revenue Operations view.

---

# 💡 Solution

The platform integrates the revenue lifecycle from lead generation through opportunity conversion and customer revenue analysis.

It enables stakeholders to:

* Monitor pipeline health and revenue performance
* Analyze funnel conversion from Lead to Won
* Identify acquisition channels with stronger conversion outcomes
* Evaluate sales representative and territory performance
* Understand customer and product revenue concentration
* Track executive KPIs through interactive Power BI dashboards

The result is a unified analytics environment designed to support more informed revenue decisions.

---

# 🏗️ Architecture

```text
Python Data Generation
        │
        ▼
Raw CSV Datasets
        │
        ▼
PostgreSQL Data Warehouse
        │
        ▼
SQL Analytics Layer
        │
        ▼
Power BI Semantic Model
        │
        ▼
Executive Analytics & Insights
```

![Platform Architecture](assets/architecture.png)

The architecture separates data generation, storage, analytics, semantic modeling, and visualization into distinct layers.

---

# 🗄️ Data Model

The platform uses a **star schema** designed for analytical reporting and Power BI performance.

![Data Model](assets/data_model.png)

## Fact Tables

| Table                | Purpose                                     |
| -------------------- | ------------------------------------------- |
| `fact_leads`         | Lead generation and funnel activity         |
| `fact_opportunities` | Pipeline, opportunity, and revenue tracking |

## Dimension Tables

| Table           | Purpose                                  |
| --------------- | ---------------------------------------- |
| `dim_customer`  | Customer attributes and segmentation     |
| `dim_product`   | Product information                      |
| `dim_sales_rep` | Sales representative attributes          |
| `dim_date`      | Time intelligence and reporting calendar |

### Model Design Principles

* Star schema architecture
* Single-direction filtering
* Analytical performance optimization
* DAX-based time intelligence
* Scalable reporting structure

---

# 📈 Executive Analytics

The Power BI solution is organized into four analytical views.

## 1. Executive Performance Overview

Provides a high-level view of overall revenue performance and pipeline health.

### Key Metrics

* Total Pipeline
* Booked Revenue
* Win Rate
* Average Deal Size
* Average Sales Cycle

### Key Insights

* Pipeline exceeds **$2.0B**
* Generated revenue exceeds **$342M**
* North America is the highest-performing territory
* Enterprise CRM is the largest product contributor to booked revenue
* Win-rate performance highlights opportunities for conversion improvement

---

## 2. Funnel Performance & Conversion Analytics

Analyzes movement through the revenue funnel from lead acquisition to won opportunities.

### Key Metrics

* Total Leads
* Lead → MQL Conversion
* MQL → SQL Conversion
* SQL → Won Conversion

### Key Insights

* Organic Search generates the highest lead volume
* Referral leads demonstrate the strongest win rate
* Webinar leads underperform relative to other acquisition channels
* Funnel leakage opportunities are visible between Lead and SQL stages

---

## 3. Sales Performance & Territory Intelligence

Evaluates sales effectiveness across territories and representatives.

### Key Metrics

* Total Revenue
* Won Deals
* Average Deal Size
* Average Sales Cycle
* Win Rate

### Key Insights

* North America is the strongest-performing territory
* Leonard Rice is the highest revenue-producing sales representative
* Average deal size exceeds **$80K**
* Average sales cycle is approximately **96 days**
* Performance varies significantly across territories

---

## 4. Product & Customer Intelligence

Analyzes customer value, industry contribution, and product revenue concentration.

### Key Metrics

* Total Customers
* Revenue per Customer
* Average Customer Value
* Enterprise Revenue Share
* Top Product Revenue Share
* Average Products per Customer

### Key Insights

* Enterprise customers contribute **55.9%** of total revenue
* Enterprise CRM contributes **70.5%** of total revenue
* Technology is the highest revenue-generating industry
* Customer acquisition remains consistently positive

---

# 🔍 Key Business Recommendations

## Funnel Optimization

* Increase investment in high-performing referral channels
* Improve webinar lead qualification and conversion processes
* Focus on reducing leakage between Lead and SQL stages

## Sales Performance

* Analyze and replicate successful North American sales practices
* Use top-performing representatives as benchmarks for coaching
* Investigate opportunities to reduce sales cycle duration in lower-performing territories

## Customer & Product Growth

* Prioritize high-value enterprise customer segments
* Expand adoption of the highest-performing products
* Monitor customer and product revenue concentration to identify growth opportunities

---

# ⚙️ Technology Stack

| Layer                 | Technology         |
| --------------------- | ------------------ |
| Data Generation       | Python             |
| Data Storage          | CSV                |
| Data Warehouse        | PostgreSQL         |
| Data Modeling         | Star Schema        |
| Analytics Layer       | SQL                |
| Business Intelligence | Power BI           |
| Business Logic        | DAX                |
| Time Intelligence     | DAX Calendar Table |

---

# 🛠️ Technical Capabilities Demonstrated

### Revenue Operations & Analytics

* Pipeline Analytics
* Funnel Performance Analysis
* Conversion Analysis
* Sales Performance Measurement
* Territory Intelligence
* Customer Revenue Analytics
* Product Performance Analysis

### Data Engineering & Analytics

* Python Data Generation
* ETL Concepts
* PostgreSQL Data Warehousing
* SQL Analytics
* Dimensional Modeling
* Star Schema Design

### Business Intelligence

* Executive KPI Reporting
* Power BI Dashboard Development
* DAX Measures
* Time Intelligence
* Interactive Reporting
* Business Insight Generation

---

# 📂 Repository Structure

```text
Revenue-Operations-Intelligence-Platform/
│
├── assets/
│   ├── architecture.png
│   ├── data_model.png
│   ├── page1.png
│   ├── page2.png
│   ├── page3.png
│   └── page4.png
│
├── data/
│   └── raw/
│
├── powerbi/
│   └── Revenue_Operations_Intelligence.pbix
│
├── sql/
│   ├── schema.sql
│   ├── create_views.sql
│   └── revenue_kpis.sql
│
├── src/
│   ├── generate_customers.py
│   ├── generate_leads.py
│   ├── generate_opportunities.py
│   └── etl/
│
├── .gitignore
└── README.md
```

---

# 🚀 Future Enhancements

Potential extensions to the platform include:

* Revenue Forecasting
* Customer Lifetime Value (CLV)
* Territory Optimization
* Sales Capacity Planning
* Predictive Lead Scoring
* Churn Analytics

---

# 👨‍💻 Author

**Abodunrin Oketade**

## 🤝 Let's Connect

I'm interested in opportunities and conversations around **Business Intelligence, Data Analytics, Commercial Analytics, Revenue Analytics, and Operational Performance**.

📍 Ontario, Canada
🔗 

<p>
<a href="https://www.linkedin.com/in/abodunrin-oketade">
<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

<a href="mailto:aoketade@gmail.com">
<img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
</a>

<a href="https://github.com/Richie-Rokka">
<img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github"/>
</a>

</p>

</div>

---

### Turning business data into actionable decisions.


