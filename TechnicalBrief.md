Título de la tarea

# Desarrollo de Plataforma Segura y Asistida por IA para Informes de Rendimiento de Teradata.


## 1. Contexto

### 1.1. El sistema actual: La generación de informes mensuales se realiza mediante una herramienta monolítica ("thick client") desarrollada en Visual Studio por un equipo en India. El acceso está restringido a DBAs de Teradata mediante llaves de seguridad generadas manualmente. La herramienta extrae métricas profundas (línea base, crecimiento, CPU, I/O, CPU Skew, Suspect CPU, Statistics, Backups, Space, Workloads, AWTs, Flow Control, Delays), las procesa en Excel, genera tablas dinámicas y finalmente exporta a PowerPoint.

### 1.2. El problema: La aplicación falla constantemente por dependencias locales en Windows (ej. .NET Framework), es lenta y ejecuta consultas pesadas de forma ineficiente. El reporte generado carece de estructura analítica, mostrando datos incompletos. Además, el esquema de licenciamiento manual es burocrático, pero la necesidad de restringir el acceso exclusivamente a personal de Teradata sigue siendo un requisito de cumplimiento innegociable.

### 1.2. El objetivo concreto: Desarrollar una herramienta escalable, inmutable y asistida por IA que automatice la extracción de datos y la redacción del análisis, generando un reporte bien estructurado. Debe incluir un sistema de autenticación moderno que reemplace las llaves manuales, garantizando que solo el equipo de Teradata Managed Services pueda ejecutarla, sin posibilidad de alterar el código fuente.



## 2. Requerimientos técnicos

### 2.1. Lenguaje de programación: Python (ideal para pipelines de datos, automatización y consumo de APIs de IA).

### 2.2. Arquitectura y Despliegue: Arquitectura basada en microservicios o contenedores (Docker) gestionada a través de pipelines de CI/CD. Esto elimina las fallas por dependencias locales en las laptops de los DBAs.

### 2.3. Seguridad y Autenticación: Implementación de Single Sign-On (SSO) utilizando el proveedor de identidad corporativo (por ejemplo, Microsoft Entra ID / Azure AD) con validación de roles (RBAC). El código debe estar empaquetado y firmado, ejecutándose en un entorno de solo lectura para evitar modificaciones locales por parte de los usuarios.

### 2.4. Integraciones: * Librería teradatasql para la ingesta de datos.
API corporativa y segura de un modelo de lenguaje (LLM) para analizar las métricas y redactar las conclusiones.
Librerías pandas y python-pptx (o generación de un dashboard web) para la presentación estructurada del output.

### 2.5. Estructura del Output: El reporte debe reclasificar las métricas en secciones lógicas (Ej. Salud del Sistema, Análisis de Cuellos de Botella, Proyección de Capacidad), acompañadas de insights generados por la IA basados en los picos de AWTs o CPU Skew.


## 3. Constraints
### 3.1. Inmutabilidad: El código de la aplicación no puede ser editable por el usuario final bajo ninguna circunstancia.

### 3.2. Seguridad de Datos: Prohibido enviar datos sensibles, IPs o nombres exactos de clientes a APIs de IA públicas o no certificadas por la empresa; se debe anonimizar el payload o usar endpoints privados.

### 3.3. Performance: Las consultas de extracción de línea base, conteo de queries y estado de estadísticas no deben bloquear las sesiones de usuario; deben ejecutarse mediante mecanismos asíncronos o con prioridades de carga de trabajo (Workload Management) bajas.

### 3.4. Calidad de Código: Uso obligatorio de type hints en Python, cumplimiento de un linter estándar (ej. flake8 o black) y manejo seguro de credenciales mediante gestores de secretos, nunca "quemadas" (hardcoded) en el código.

## 4. Definition of Done
[ ] El sistema se autentica correctamente validando el rol del usuario (exclusivo para usuarios autorizados) sin requerir llaves de seguridad manuales.
[ ] La herramienta se ejecuta en un entorno aislado (ej. contenedor) sin fallar por dependencias del sistema operativo host.
[ ] El script de extracción recupera exitosamente las métricas clave (CPU, IO, Skew, Statistics, Space, AWT, Flow Control) sin degradar el rendimiento de la base de datos objetivo.
[ ] La IA procesa el dataset y devuelve un análisis en texto estructurado que identifica al menos un cuello de botella o anomalía justificable con los datos extraídos.
[ ] Se genera el artefacto final (PPTX o Dashboard) integrando las gráficas y el análisis de la IA con el formato corporativo esperado.
