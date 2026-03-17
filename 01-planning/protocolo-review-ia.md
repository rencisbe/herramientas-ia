Auditoría Forense de Código: Proyecto IA Teradata (Monthly Report)
Objetivo: Validar la inmutabilidad de la arquitectura contenerizada, garantizar la anonimización de datos antes de enviarlos a la IA, certificar la seguridad del acceso (SSO) y asegurar un impacto cero (Zero-Impact) en los entornos de base de datos de los clientes.
Auditor: ____________________ | Commit Hash: ____________________ | Fecha: ____________

Fase 1: Análisis Estático, Dependencias e Inmutabilidad
Objetivo: Rastrear inyección de librerías no autorizadas y garantizar que el código no pueda ser alterado por los DBAs en sus máquinas locales.

1.1. Auditoría de Contenedores y Entorno (Docker/Microservicios)
Comando/Acción: Revisar el archivo Dockerfile y docker-compose.yml (o pipelines de CI/CD).

Evidencia Requerida: * El código fuente debe ser copiado al contenedor (COPY . /app) y ejecutarse bajo un usuario sin privilegios de root (USER nonroot).

No deben existir volúmenes (volumes:) que mapeen los scripts de Python locales del usuario hacia el contenedor, previniendo alteraciones manuales del código.

Estado: [ ] Pass / [ ] Fail / [ ] N/A

1.2. Restricción de Librerías (Zero-Shadow IT)
Comando/Acción: Inspeccionar requirements.txt o Pipfile.

Evidencia Requerida: * Solo deben existir paquetes aprobados (teradatasql, pandas, python-pptx, librerías oficiales de LLM/LangChain).

Búsqueda en código de requests.post() o urllib para asegurar que no se estén enviando telemetrías o datos a APIs externas no autorizadas fuera del LLM corporativo.

Estado: [ ] Pass / [ ] Fail / [ ] N/A

Fase 2: Lógica Analítica y Control del Modelo de IA (LLM)
Objetivo: Evitar que la IA invente métricas de rendimiento y asegurar que respete el formato del reporte.

2.1. Prevención de Alucinaciones Matemáticas
Comando/Acción: Revisar los System Prompts (Instrucciones base) inyectados en el código de Python y ejecutar una prueba unitaria con un dataset simulado.

Evidencia Requerida: * El prompt debe contener instrucciones restrictivas estrictas (Ej. "Basa tu análisis ÚNICAMENTE en el JSON proporcionado. No asumas ni inventes métricas").

Al inyectar un dataset con AWT = 0 y Flow Control = 0, el LLM no debe generar recomendaciones genéricas sobre cuellos de botella inexistentes.

Estado: [ ] Pass / [ ] Fail / [ ] N/A

2.2. Precisión de Lógica de Negocio (DBA Skills)
Comando/Acción: Trazabilidad de las funciones de cálculo (Pandas) previas al envío a la IA.

Evidencia Requerida: * Verificar que la función que calcula el "Crecimiento de Objetos" (Baseline vs Actual) maneje correctamente valores nulos o divisiones por cero (NaN, Inf), evitando que el pipeline colapse antes de llegar a la IA.

Estado: [ ] Pass / [ ] Fail / [ ] N/A

Fase 3: Seguridad de Datos y Autenticación
Objetivo: Blindar el acceso exclusivo a Teradata Managed Services y proteger la información del cliente.

3.1. Autenticación SSO y Control de Roles (RBAC)
Comando/Acción: Intento de ejecución del pipeline simulando un usuario no autenticado o con un rol distinto.

Evidencia Requerida: * La aplicación debe rechazar la ejecución si el token de identidad (ej. Azure Entra ID, Okta) no contiene explícitamente el grupo o rol Teradata_DBA_ManagedServices.

No debe existir ningún mecanismo de bypass (ej. llaves maestras en texto plano o el viejo sistema de "Security Keys" quemado en el código).

Estado: [ ] Pass / [ ] Fail / [ ] N/A

3.2. Escaneo de Secretos y Anonimización de Payload
Comando/Acción: Búsqueda profunda en repositorio y revisión de logs.

Evidencia Requerida: * Las credenciales de conexión a Teradata (UID, PWD) y la API_KEY del LLM deben extraerse de un gestor de secretos (Environment Variables, HashiCorp Vault, AWS Secrets), nunca de un archivo .config visible.

El JSON generado para el LLM debe pasar por una función de enmascaramiento que elimine IPs, nombres de servidores específicos y nombres de la empresa cliente antes de salir a la red.

Estado: [ ] Pass / [ ] Fail / [ ] N/A

Fase 4: Rendimiento e Impacto en Base de Datos
Objetivo: Certificar que la herramienta no se convertirá en un problema de rendimiento ("Rogue Query") para el cliente.

4.1. Workload Management (WLM) y Query Banding
Comando/Acción: Inspeccionar el string de conexión y la sesión generada por teradatasql.

Evidencia Requerida: * Toda conexión iniciada por la herramienta debe inyectar un SET QUERY_BAND identificable (ej. SET QUERY_BAND='ApplicationName=MonthlyTool_AI;UtilityData=Background;' FOR SESSION;).

Validar que el usuario de servicio utilizado esté mapeado a un Workload de baja prioridad (Reporting/Background) en TASM/TIWM para no robar CPU a la operación del cliente.

Estado: [ ] Pass / [ ] Fail / [ ] N/A

4.2. Ejecución Asíncrona (Prevención de Timeouts)
Comando/Acción: Auditoría del flujo de ejecución en Python.

Evidencia Requerida: * Las consultas pesadas (como cruzar tablas gigantes de DBQL o ResUsage) no deben bloquear la interfaz. Deben ejecutarse de forma asíncrona (ej. usando asyncio, Celery, o tareas en segundo plano) con manejo de Timeouts adecuado.

Estado: [ ] Pass / [ ] Fail / [ ] N/A

Dictamen Forense Final
[ ] APROBADO: La arquitectura es inmutable, los datos están seguros/anonimizados y el impacto en DB está controlado. Listo para Deploy al equipo de Managed Services.
[ ] RECHAZADO CON OBSERVACIONES: Se detectaron hardcodings menores o alertas en los Prompts de la IA. Requiere ajuste.
[ ] FALLA CRÍTICA: Vulnerabilidad en SSO, credenciales expuestas o consultas ejecutadas sin Query Banding. Refactorización obligatoria.
