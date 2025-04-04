SELECT 
    inc_number, 
    inc_category, 
    inc_priority, 
    inc_sla_due, 
    inc_sys_created_on, 
    inc_resolved_at, 
    inc_assignment_group, 
    inc_state,
    inc_caller_id,
    inc_short_description,
    inc_close_code,
    inc_close_notes,
    EXTRACT(YEAR FROM inc_sys_created_on::timestamp) AS year,
    EXTRACT(MONTH FROM inc_sys_created_on::timestamp) AS month,
    EXTRACT(DAY FROM inc_sys_created_on::timestamp) AS day

FROM public.sample
