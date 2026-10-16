import os
import numpy as np
import pandas as pd

def generate_dbt_seeds():
    os.makedirs("seeds", exist_ok=True)
    np.random.seed(42)
    n_customers = 200
    n_orders = 1000

    # 1. Raw Customers
    customers = pd.DataFrame({
        'id': range(1, n_customers + 1),
        'first_name': [f"User_{i}" for i in range(1, n_customers + 1)],
        'last_name': [f"LastName_{i}" for i in range(1, n_customers + 1)],
        'email': [f"user_{i}@example.com" if i % 10 != 0 else f"user_{i}invalid" for i in range(1, n_customers + 1)],
        'signup_date': pd.date_range(start='2025-01-01', periods=n_customers, freq='D').strftime('%Y-%m-%d')
    })
    customers.to_csv("seeds/raw_customers.csv", index=False)

    # 2. Raw Orders
    statuses = ['completed', 'completed', 'completed', 'returned', 'placed', 'shipped']
    orders = pd.DataFrame({
        'id': range(1001, 1001 + n_orders),
        'user_id': np.random.randint(1, n_customers + 1, size=n_orders),
        'order_date': pd.date_range(start='2025-06-01', periods=n_orders, freq='h').strftime('%Y-%m-%d %H:%M:%S'),
        'status': np.random.choice(statuses, size=n_orders)
    })
    orders.to_csv("seeds/raw_orders.csv", index=False)

    # 3. Raw Payments
    methods = ['credit_card', 'coupon', 'bank_transfer', 'gift_card']
    payments = pd.DataFrame({
        'id': range(5001, 5001 + n_orders),
        'order_id': orders['id'],
        'payment_method': np.random.choice(methods, size=n_orders),
        'amount_cents': np.random.randint(500, 50000, size=n_orders) # Суми в копійках/центах
    })
    payments.to_csv("seeds/raw_payments.csv", index=False)

    print("✅ Seed files successfully generated in 'seeds/' folder!")

if __name__ == "__main__":
    generate_dbt_seeds()