# TP: Gestión Colaborativa, Control de Versiones y Organización Empresarial (Git, GitHub y Jira)

## 🏛️ Universidad Tecnológica Nacional (UTN)
* **Carrera:** Tecnicatura Universitaria en Programación (TUP) - Modalidad a Distancia.
* **Cátedra:** Organización Empresarial.
* **Año Lectivo:** 2026.

---

## 👥 Integrantes y Roles (Célula de Desarrollo Ágil)
Para cumplir con los requerimientos metodológicos de la cátedra bajo el enfoque de **Aprendizaje Basado en Problemas (ABP)**, se estructuró el trabajo simulando una célula ágil de tres roles interpretados de la siguiente manera:

1. **P1 - Líder y Organizador (Hugo Pérez / S-Seipel):** Responsable de la gobernanza del repositorio, inicialización de la estructura de directorios (`/scripts`, `/datos`, `/resultados`) y documentación general.
2. **P2 - Desarrollador Técnico (Paco Gómez / S-Seipel):** Responsable del desarrollo del script lógico en Python para el procesamiento de datos climáticos.
3. **P3 - Revisor y QA (Luis Rodríguez / S-Seipel):** Responsable de la revisión técnica del código (*Peer Review*), comentarios de mejora en el Pull Request, control de seguridad e higiene del código y configuración del archivo `.gitignore`.

---

## 📊 Escenario Seleccionado: Escenario A - Análisis de Datos Climáticos

### 1. Objetivo del Proyecto
Desarrollar un script automatizado y reproducible en Python para importar, procesar y analizar un conjunto de datos meteorológicos históricos. El sistema calcula indicadores clave de temperaturas y precipitaciones para finalmente exportar gráficos y reportes estadísticos que asistan a la toma de decisiones organizacionales.

### 2. Descripción del Dataset Utilizado
Se adoptaron datos abiertos basados en el análisis climático **GISTEMP (NASA)**, con un set de datos de series temporales que registran:
* **Año:** Período de registro (1980 - 2025).
* **Temperatura Promedio Anual:** Anomalías y registros de temperatura global en grados Celsius (°C).
* **Precipitaciones Promedio:** Registro anual acumulado de lluvias medido en milímetros (mm).

---

## 📂 Estructura del Repositorio
El repositorio sigue estrictamente el estándar de orden de directorios exigido:
```text
tp-organizacion-empresarial/
├── datos/
│   └── global_temp_data.csv       # Archivo de datos fuente
├── scripts/
│   └── analisis_datos.py         # Script lógico en Python 
├── resultados/
│   ├── evolucion_temperatura.png  # Gráfico estadístico exportado
│   └── resumen_indicadores.txt    # Reporte de texto con indicadores calculados
├── .gitignore                     # Configuración de exclusión de Git
└── README.md                      # Documentación del proyecto (este archivo)
```
---

## 🚀 Instrucciones de Ejecución en Google Colab

Este proyecto es 100% reproducible y autónomo. Para ejecutar el análisis:

1. **Clonar el repositorio** e ingresar a la carpeta del proyecto en su celda de Colab:
   ```bash
   !git clone [https://github.com/S-Seipel/tp-organizacion-empresarial.git](https://github.com/S-Seipel/tp-organizacion-empresarial.git)
   %cd tp-organizacion-empresarial
   ```
   
2. **Ejecutar el script técnico:**
   El programa creará automáticamente cualquier estructura faltante, procesará los datos climáticos y exportará los resultados ejecutando:
   ```bash
   !python scripts/analisis_datos.py
   ```
   
3. **Revisar Resultados:**
   Los reportes e imágenes generados se guardarán automáticamente en la carpeta `/resultados`.

---
