SELECT TheDate, NodeID, CPUUExec
FROM dbc.ResUsageSpma
WHERE TheDate >= CURRENT_DATE - 2;
