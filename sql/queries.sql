SELECT * FROM fact_nav;

SELECT AVG(nav_value) AS average_nav
FROM fact_nav;

SELECT fund_id, MAX(nav_value)
FROM fact_nav
GROUP BY fund_id;