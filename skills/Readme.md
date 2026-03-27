## Arquitectura de Skills (TDD)

Este proyecto reemplaza la arquitectura monolítica anterior (Visual Basic) por un sistema moderno en Python. Se construye de manera modular utilizando un enfoque basado en "Skills" (habilidades independientes). Cada componente tiene una responsabilidad única, reglas de negocio estrictas documentadas en su respectivo `SKILL.md`, y es validado continuamente mediante pruebas automatizadas (Pytest).

### ✅ Skills Completados

* **1. Extractor Seguro de Datos (`skills/extractor`)**
    * **Propósito:** Conexión de solo lectura a la base de datos para extraer métricas de rendimiento (CPU, AWTs, Skew, etc.).
    * **Reglas de Negocio Implementadas:**
        * Separación de lógica: Lectura dinámica de consultas desde archivos `.sql` externos (cero *hardcoding* de SQL en Python).
        * **Zero-Impact:** Inyección obligatoria de un string `SET QUERY_BAND` de baja prioridad en cada sesión para garantizar que las extracciones no afecten el rendimiento de los entornos de los clientes.
        * Manejo seguro de conexiones y retorno de datos estructurados vía Pandas.
    * **Estado:** Pruebas (TDD) 100% exitosas.

* **2. Motor de Exportación Visual (`skills/exportador`)**
    * **Propósito:** Transformar los DataFrames de métricas en gráficas insertadas automáticamente en las presentaciones de resultados.
    * **Reglas de Negocio Implementadas:**
        * Integración con `python-pptx` para la generación de gráficos nativos (ej. *Line Charts*).
        * **Inmutabilidad:** Garantía estricta de que la plantilla corporativa base (`Monthly Operations Report - Template.pptx`) solo se utiliza en modo lectura y nunca es sobrescrita. Los resultados se guardan siempre en una ruta de salida nueva.
    * **Estado:** Pruebas (TDD) 100% exitosas.

### ⏳ Skills Pendientes (Backlog)

* **3. Analista IA (`skills/analista_ia`)**
    * **Propósito:** Procesamiento de los CSVs/DataFrames a través de un LLM (LangChain) para generar diagnósticos automatizados en texto sobre cuellos de botella.
    * **Restricción Crítica:** Prevención estricta de alucinaciones matemáticas; el modelo de IA no debe inventar recomendaciones si no hay anomalías numéricas comprobables.
* **4. Anonimizador de Payload (`skills/anonimizador_payload`)**
    * **Propósito:** Filtro de seguridad de datos (Zero-Shadow IT).
    * **Restricción Crítica:** Enmascarar direcciones IP, nombres de nodos y referencias explícitas a las cuentas de los clientes antes de enviar cualquier *payload* al modelo de lenguaje.
* **5. Validador de Acceso SSO (`skills/validador_sso`)**
    * **Propósito:** Reemplazar el antiguo esquema de licenciamiento manual y llaves de seguridad locales.
    * **Restricción Crítica:** Validar tokens de identidad (RBAC) para asegurar que la ejecución esté restringida exclusivamente al grupo `Teradata_DBA_ManagedServices`.

### 🚀 Próximos Pasos

1.  **Prueba de Integración End-to-End (E2E):** Crear un script orquestador rápido (`demo.py`) para probar la conexión en cadena del `extractor` con el `exportador`, generando un reporte PowerPoint real a partir de un archivo CSV de muestra.
2.  **Desarrollo del Componente IA:** Iniciar el ciclo TDD para el Skill del `analista_ia`, configurando los prompts del sistema y conectándolo de forma segura.