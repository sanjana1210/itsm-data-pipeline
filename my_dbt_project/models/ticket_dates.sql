SELECT 
    inc_number,
    EXTRACT(YEAR FROM inc_sys_created_on::timestamp) AS year,
    EXTRACT(MONTH FROM inc_sys_created_on::timestamp) AS month,
    EXTRACT(DAY FROM inc_sys_created_on::timestamp) AS day
FROM {{ ref('cleaned_tickets') }}
