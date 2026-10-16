select
    orders.order_id,
    orders.customer_id,
    orders.order_date,
    orders.status,
    payments.payment_method,
    payments.amount
from {{ ref('stg_orders') }} as orders
left join {{ ref('stg_payments') }} as payments
    on orders.order_id = payments.order_id
