SELECT 
inc_category,
inc_priority,
    AVG(EXTRACT(EPOCH FROM (TO_TIMESTAMP(inc_resolved_at, 'DD-MM-YYYY HH24:MI') - 
                             TO_TIMESTAMP(inc_sys_created_on, 'DD-MM-YYYY HH24:MI')))) 
    AS avg_resolution_time
FROM public.sample
GROUP BY inc_category , inc_priority
