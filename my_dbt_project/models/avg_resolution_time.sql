SELECT 
    inc_category,
    inc_priority,
    AVG(EXTRACT(EPOCH FROM (inc_resolved_at - inc_sys_created_on))) AS avg_resolution_time
FROM public.sample
GROUP BY inc_category, inc_priority
