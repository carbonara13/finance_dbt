select
    cast(id as integer) as order_id,
    cast(user_id as integer) as customer_id,
    cast(order_date as timestamp) as order_date,
    lower(trim(status)) as status
from {{ source('raw', 'raw_orders') }}
