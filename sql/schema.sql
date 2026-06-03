CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY,
    fund_name TEXT,
    category TEXT
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    nav_value REAL,
    nav_date DATE
);