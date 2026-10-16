# finance_dbt

## Запуск

Запустити з каталозі проєкту:

```bash
source .venv/bin/activate
dbt seed
dbt run
dbt test
dbt docs generate
dbt docs serve
```

Документація генерується у `target/`: `index.html`, `manifest.json`, `catalog.json` і через `dbt docs serve`.

## Залежності
raw_customers --> stg_customers
raw_orders --> stg_orders
raw_payments --> stg_payments
stg_orders --> fct_orders
stg_payments --> fct_orders
stg_customers --> dim_customers
fct_orders --> dim_customers
