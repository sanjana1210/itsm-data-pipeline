SELECT 
    inc_assignment_group, 
    COUNT(CASE WHEN inc_state = 'Closed' THEN 1 END) * 100.0 / COUNT(*) AS closure_rate
FROM {{ ref('cleaned_tickets') }}
GROUP BY inc_assignment_group
