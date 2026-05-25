# ==============================================================================
# Script de Procesamiento de Datos Climáticos (Escenario A)
# Creado por: Paco Gomez (Desarrollador)
# ==============================================================================
import os
import pandas as pd
import matplotlib.pyplot as plt

# Carga de datos climáticos históricos
df = pd.read_csv("datos/global_temp_data.csv")

# Cálculo automatizado de indicadores estadísticos requeridos
temp_promedio = df["Temperatura_Promedio"].mean()
temp_maxima = df["Temperatura_Promedio"].max()
temp_minima = df["Temperatura_Promedio"].min()
precip_promedio = df["Precipitaciones_Promedio"].mean()

# Generación del reporte de texto de resultados
with open("resultados/resumen_indicadores.txt", "w", encoding="utf-8") as f:
    f.write("====================================================\n")
    f.write("       REPORTE DE INDICADORES CLIMÁTICOS (UTN)       \n")
    f.write("====================================================\n\n")
    f.write(f"Temperatura Promedio Historica: {temp_promedio:.2f} °C\n")
    f.write(f"Temperatura Maxima Registrada:  {temp_maxima:.2f} °C\n")
    f.write(f"Temperatura Minima Registrada:  {temp_minima:.2f} °C\n")
    f.write(f"Promedio Anual de Precipitaciones: {precip_promedio:.2f} mm\n")

# Generación de la visualización gráfica de evolución térmica
plt.figure(figsize=(8, 5))
plt.plot(df["Anio"], df["Temperatura_Promedio"], marker='o', color='red', linewidth=2, label="Anomalia de Temperatura (°C)")
plt.axhline(temp_promedio, color='blue', linestyle='--', alpha=0.7, label=f"Promedio Historico ({temp_promedio:.2f}°C)")
plt.title("Evolucion de la Temperatura Global (1980 - 2025)", fontsize=12, fontweight='bold')
plt.xlabel("Anio")
plt.ylabel("Temperatura (°C)")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("resultados/evolucion_temperatura.png", dpi=150)
plt.close()

print("[OK-SCRIPT] Procesamiento de datos climáticos completado con éxito.")