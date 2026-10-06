select database();
use ecommerce_db;

select count(distinct order_id) as unique_orders,count(distinct customer_id) as unique_customers,sum(quantity) as total_quantity_sold from ecommerce_sales;

select product,sum(quantity*unit_price) as Revenue from ecommerce_sales group by product order by Revenue desc limit 5;

select city,sum(quantity*unit_price) as Revenue from ecommerce_sales group by city order by Revenue desc;

select category,avg(quantity*unit_price) as Average from ecommerce_sales group by category order by Average desc ;

select customer_id,customer_name,sum(quantity*unit_price) as total_spending from ecommerce_sales group by customer_id,customer_name order by total_spending desc limit 10;

select product,avg(discount) as avg_discount from ecommerce_sales group by product having avg_discount>10;

SELECT
    product,
    AVG(discount) AS avg_discount
FROM ecommerce_sales
GROUP BY product
ORDER BY avg_discount DESC;


select order_status,count(*) as order_count from ecommerce_sales group by order_status;

select city,sum(quantity*unit_price) as Revenue from ecommerce_sales where order_status='Completed' group by city having Revenue>500000;