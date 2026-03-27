import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from src.extractor import run_query_from_file

def test_extractor_injects_query_band_and_returns_dataframe():
    # 1. Configuración de la simulación (Mock)
    mock_df = pd.DataFrame({
        "TheDate": ["2026-03-25", "2026-03-26"],
        "NodeID": ["33", "33"],
        "CPUUExec": [45.2, 88.5]
    })
    
    # Ruta temporal de nuestro archivo SQL creado en el paso 2
    sql_file_path = "skills/extractor_teradata/queries/01_cpu_utilization.sql"

    # 2. Ejecución interceptando Pandas y TeradataSQL
    with patch('pandas.read_sql') as mock_read_sql, \
         patch('teradatasql.connect') as mock_connect:
        
        # Le decimos al mock que devuelva nuestro DataFrame simulado
        mock_read_sql.return_value = mock_df
        
        # Ejecutamos la función que AÚN NO EXISTE (esto hará que el test falle)
        resultado = run_query_from_file(
            host="dummy_host", 
            user="dummy_user", 
            password="dummy_password", 
            sql_path=sql_file_path
        )
        
        # 3. Verificaciones (Asserts)
        # Verificar que la conexión se llamó con los parámetros correctos
        mock_connect.assert_called_once_with(host="dummy_host", user="dummy_user", password="dummy_password")
        
        # Verificar que la función devuelve un DataFrame
        assert isinstance(resultado, pd.DataFrame)
        assert len(resultado) == 2
        
        # Validar que NO estamos inventando datos
        assert resultado.iloc[1]["CPUUExec"] == 88.5