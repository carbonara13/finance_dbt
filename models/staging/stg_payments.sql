select
    cast(id as integer) as payment_id,
    cast(order_id as integer) as order_id,
    lower(trim(payment_method)) as payment_method,
    {{ cents_to_dollars('amount_cents') }} as amount
from {{ source('raw', 'raw_payments') }}
