with customer_orders as (
    select
        customer_id,
        cast(min(order_date) as date) as first_order_date,
        cast(max(order_date) as date) as most_recent_order_date,
        count(*) as number_of_orders,
        sum(case when status = 'completed' then amount else 0 end) as total_lifetime_value
    from {{ ref('fct_orders') }}
    group by customer_id
)
select
    customers.customer_id,
    customers.first_name,
    customers.last_name,
    customers.signup_date,
    customer_orders.first_order_date,
    customer_orders.most_recent_order_date,
    coalesce(customer_orders.number_of_orders, 0) as number_of_orders,
    coalesce(customer_orders.total_lifetime_value, 0) as total_lifetime_value
from {{ ref('stg_customers') }} as customers
left join customer_orders
    on customers.customer_id = customer_orders.customer_id
