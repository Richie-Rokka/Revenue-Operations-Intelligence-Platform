CREATE OR REPLACE VIEW vw_funnel_performance AS
SELECT
    COUNT(*) AS total_leads,

    SUM(
        CASE
            WHEN mql_flag THEN 1
            ELSE 0
        END
    ) AS mqls,

    SUM(
        CASE
            WHEN sql_flag THEN 1
            ELSE 0
        END
    ) AS sqls,

    SUM(
        CASE
            WHEN converted THEN 1
            ELSE 0
        END
    ) AS converted_leads,

    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN converted THEN 1
                ELSE 0
            END
        )
        / COUNT(*),
        2
    ) AS conversion_rate

FROM fact_leads;


CREATE OR REPLACE VIEW vw_pipeline_summary AS
SELECT
    COUNT(*) AS opportunities,
    SUM(expected_revenue) AS pipeline_value,
    SUM(actual_revenue) AS booked_revenue,
    SUM(CASE WHEN won THEN 1 ELSE 0 END) AS won_deals
FROM fact_opportunities;



CREATE OR REPLACE VIEW vw_sales_rep_performance AS
SELECT
    s.sales_rep_id,
    s.sales_rep_name,
    s.territory,
    COUNT(o.opportunity_id) AS opportunities,
    SUM(o.actual_revenue) AS revenue
FROM fact_opportunities o
JOIN dim_sales_rep s
    ON o.sales_rep_id = s.sales_rep_id
GROUP BY
    s.sales_rep_id,
    s.sales_rep_name,
    s.territory;



CREATE OR REPLACE VIEW vw_product_revenue AS
SELECT
    p.product_name,
    p.plan_tier,
    COUNT(o.opportunity_id) AS deals,
    SUM(o.actual_revenue) AS revenue
FROM fact_opportunities o
JOIN dim_product p
    ON o.product_id = p.product_id
GROUP BY
    p.product_name,
    p.plan_tier;



CREATE OR REPLACE VIEW vw_region_revenue AS
SELECT
    c.region,
    COUNT(o.opportunity_id) AS opportunities,
    SUM(o.actual_revenue) AS revenue
FROM fact_opportunities o
JOIN dim_customer c
    ON o.customer_id = c.customer_id
GROUP BY c.region;



CREATE OR REPLACE VIEW vw_win_rate AS
SELECT
    COUNT(*) AS total_opportunities,
    SUM(CASE WHEN won THEN 1 ELSE 0 END) AS won_deals,
    ROUND(
        100.0 *
        SUM(CASE WHEN won THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS win_rate
FROM fact_opportunities;



CREATE OR REPLACE VIEW vw_avg_deal_size AS
SELECT
    ROUND(
        AVG(actual_revenue),
        2
    ) AS avg_deal_size
FROM fact_opportunities
WHERE won = TRUE;


CREATE OR REPLACE VIEW vw_sales_cycle AS
SELECT
    ROUND(
        AVG(sales_cycle_days),
        2
    ) AS avg_sales_cycle_days
FROM fact_opportunities;