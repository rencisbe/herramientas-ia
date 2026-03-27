from pathlib import Path

import pandas as pd
import teradatasql

QUERY_BAND_SQL = (
    "SET QUERY_BAND='ApplicationName=Monthly_Report;UtilityData=Background;' "
    "FOR SESSION;"
)


ddef run_query_from_file(host: str, user: str, password: str, sql_path: str) -> pd.DataFrame:
    with open(sql_path, encoding="utf-8") as f:
        sql = f.read()

    conn = None
    try:
        conn = teradatasql.connect(host=host, user=user, password=password)
        cur = conn.cursor()
        try:
            cur.execute(QUERY_BAND_SQL)
        finally:
            cur.close()
        return pd.read_sql(sql, conn)
    finally:
        if conn is not None:
            conn.close()