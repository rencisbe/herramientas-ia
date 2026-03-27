/* Métrica 01: Utilización de CPU Básica */
SELECT 
    TheDate,
    TheTime,
    NodeID,
    CPUUExec,
    CPUUServ
FROM 
    dbc.ResUsageSPMA 
WHERE 
    TheDate BETWEEN CURRENT_DATE - 30 AND CURRENT_DATE
ORDER BY 
    TheDate, TheTime;