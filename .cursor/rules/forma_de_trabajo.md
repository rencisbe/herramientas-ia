# Reglas de Proyecto - Auditoría IA Teradata

## Stack Tecnológico
- **Lenguaje**: Python 3.11+ (Type hints obligatorios)
- **Infraestructura**: Docker (Rootless), CI/CD GitHub Actions
- **Librerías**: teradatasql, pandas, python-pptx, LangChain
- **Testing**: Pytest

## Principios de Inmutabilidad y Seguridad
1. **Zero-Shadow IT**: No usar librerías externas sin aprobación.
2. **Anonimización**: Prohibido enviar IPs o nombres de clientes al LLM.
3. **SSO First**: Toda ejecución requiere validación de rol `Teradata_DBA_ManagedServices`.

## Estructura de Carpetas
/src
  /collector      # Ingesta con teradatasql
  /processor      # Lógica de Pandas y limpieza
  /ai_agent       # Prompts y conexión a LLM
  /exporter       # Generación de PPTX
/tests
  /unit           # Tests de lógica
  /integration    # Tests de conexión y contenedores