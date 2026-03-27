# Skill: Extractor Seguro Teradata

## Propósito
Conectarse a la base de datos, inyectar el Query Banding obligatorio para no afectar la operación, leer un archivo `.sql` dinámicamente y devolver los resultados como un DataFrame de Pandas.

## Reglas de Implementación
1. Utilizar la librería `teradatasql` y `pandas` (usar `pd.read_sql`).
2. NUNCA quemar (hardcode) consultas SQL en el código Python. El código debe recibir la ruta del archivo `.sql` y leer su contenido.
3. Antes de ejecutar cualquier consulta de extracción, la sesión debe ejecutar: 
   `SET QUERY_BAND='ApplicationName=Monthly_Report;UtilityData=Background;' FOR SESSION;`
4. Manejar correctamente el cierre de la conexión a la base de datos (usar bloques `try...finally` o context managers `with`).