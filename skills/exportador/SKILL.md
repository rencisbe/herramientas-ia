# Skill: Motor de Exportación PPTX

## Propósito
Tomar un DataFrame de Pandas y graficarlo automáticamente dentro de una plantilla corporativa de PowerPoint (.pptx), guardando el resultado como un archivo nuevo.

## Reglas de Implementación
1. Utilizar la librería `python-pptx` y `pandas`.
2. **Inmutabilidad de la Plantilla:** NUNCA sobrescribir el archivo de origen. Siempre guardar el resultado en la ruta de salida.
3. La función debe recibir el índice del slide donde se insertará la gráfica (ej. `slide_index=1` para el segundo slide).
4. El gráfico debe ser de tipo Línea (Line Chart) para mostrar la tendencia de CPU.