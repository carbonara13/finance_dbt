{% macro cents_to_dollars(column_name, decimal_places=2) -%}
    ROUND(CAST({{ column_name }} AS NUMERIC) / 100.0, {{ decimal_places }})
{%- endmacro %}
