import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leer el archivo de Excel
ruta_archivo = 'resumen_datos.xlsx'
df = pd.read_excel(ruta_archivo, decimal=',')

# Eliminar espacios adicionales en los nombres de las columnas
df.columns = df.columns.str.strip()

# Crear la figura
plt.figure(figsize=(10, 6))

# Ordenar las parejas de columnas y etiquetas en el orden especificado
columnas = [
    ("Tiempof4", "Voltajef4", "N-S (1 imán)"),          # N-S (1 imán)
    ("Tiempof6", "Voltajef6", "S-N (1 imán)"),          # S-N (1 imán)
    ("Tiempof9", "Voltajef9", "NN-SS (2 imanes)"),      # NN-SS (2 imanes)
    ("Tiempof1", "Voltajef1", "SS-NN (2 imanes)"),      # SS-NN (2 imanes)
    ("Tiempof5", "Voltajef5", "NS-SN (2 imanes) I"),   # NS-SN (2 imanes)
    ("Tiempof8", "Voltajef8", "NS-SN (2 imanes) II"),      # NS-SN (2 imanes)
]

def integral_prom(ti, tf, df_tiempo, df_voltaje):
    """
    Calcula el área bajo la curva utilizando la regla del trapecio.
    """
    mask = (df_tiempo >= ti) & (df_tiempo <= tf)
    tiempo = df_tiempo[mask].values
    voltaje = df_voltaje[mask].values
    
    area_total = 0.0
    for i in range(len(tiempo) - 1):
        delta_t = tiempo[i + 1] - tiempo[i]
        promedio_voltaje = (voltaje[i] + voltaje[i + 1]) / 2
        area_total += promedio_voltaje * delta_t
    
    return area_total

n_s_peak1 = integral_prom(ti=0.75, tf=0.925, df_tiempo=df['Tiempof4'], df_voltaje=df['Voltajef4'])
print(f"Área bajo la curva de N-S (1 imán) en el primer pico: {n_s_peak1:.4f} V*s")
n_s_peak2 = integral_prom(ti=0.925, tf=1.05, df_tiempo=df['Tiempof4'], df_voltaje=df['Voltajef4'])
print(f"Área bajo la curva de N-S (1 imán) en el segundo pico: {n_s_peak2:.4f} V*s")
print("_____")
#----------------------------------------------

s_n_peak1 = integral_prom(ti=0.65, tf=0.8, df_tiempo=df['Tiempof6'], df_voltaje=df['Voltajef6'])
print(f"Área bajo la curva de S-N (1 imán) en el primer pico: {s_n_peak1:.4f} V*s")
s_n_peak2 = integral_prom(ti=0.8, tf=1.0, df_tiempo=df['Tiempof6'], df_voltaje=df['Voltajef6'])
print(f"Área bajo la curva de S-N (1 imán) en el segundo pico: {s_n_peak2:.4f} V*s")
print("_____")

#----------------------------------------------

nn_ss_peak1 = integral_prom(ti=1.15, tf=1.355, df_tiempo=df['Tiempof9'], df_voltaje=df['Voltajef9'])
print(f"Área bajo la curva de NN-SS (2 imanes) en el primer pico: {nn_ss_peak1:.4f} V*s")
nn_ss_peak2 = integral_prom(ti=1.355, tf=1.5, df_tiempo=df['Tiempof9'], df_voltaje=df['Voltajef9'])
print(f"Área bajo la curva de NN-SS (2 imanes) en el segundo pico: {nn_ss_peak2:.4f} V*s")
print("_____")

#----------------------------------------------

ss_nn_peak1 = integral_prom(ti=0.42, tf=0.56, df_tiempo=df['Tiempof1'], df_voltaje=df['Voltajef1'])
print(f"Área bajo la curva de SS-NN (2 imanes) en el primer pico: {ss_nn_peak1:.4f} V*s")
ss_nn_peak2 = integral_prom(ti=0.56, tf=0.7, df_tiempo=df['Tiempof1'], df_voltaje=df['Voltajef1'])
print(f"Área bajo la curva de SS-NN (2 imanes) en el segundo pico: {ss_nn_peak2:.4f} V*s")
print("_____")

#----------------------------------------------

ns_sn_1peak1 = integral_prom(ti=0.7, tf=0.93, df_tiempo=df['Tiempof5'], df_voltaje=df['Voltajef5'])
print(f"Área bajo la curva de NS-SN (2 imanes) I en el primer pico: {ns_sn_1peak1:.4f} V*s")
ns_sn_1peak2 = integral_prom(ti=0.93, tf=1.05, df_tiempo=df['Tiempof5'], df_voltaje=df['Voltajef5'])
print(f"Área bajo la curva de NS-SN (2 imanes) I en el segundo pico: {ns_sn_1peak2:.4f} V*s")
print("_____")

#----------------------------------------------
ns_sn_2peak1 = integral_prom(ti=1.2, tf=1.355, df_tiempo=df['Tiempof8'], df_voltaje=df['Voltajef8'])
print(f"Área bajo la curva de NS-SN (2 imanes) II en el primer pico: {ns_sn_2peak1:.4f} V*s")
ns_sn_2peak2 = integral_prom(ti=1.355, tf=1.5, df_tiempo=df['Tiempof8'], df_voltaje=df['Voltajef8'])
print(f"Área bajo la curva de NS-SN (2 imanes) II en el segundo pico: {ns_sn_2peak2:.4f} V*s")
print("_____")

# Graficar cada conjunto de tiempo y voltaje, truncado a t <= 1.5
for tiempo_col, voltaje_col, label in columnas:
    if tiempo_col in df.columns and voltaje_col in df.columns:
        tiempo = df[tiempo_col]
        voltaje = df[voltaje_col]
        
        # Aplicar la condición de truncamiento
        mask = tiempo <= 1.5
        tiempo_truncado = tiempo[mask]
        voltaje_truncado = voltaje[mask]
        
        # Graficar cada conjunto de datos truncado
        plt.plot(tiempo_truncado, voltaje_truncado, label=label)

# Configurar el título y etiquetas
plt.title('Gráfico Voltaje vs Tiempo', fontsize=18)
plt.xlabel('Tiempo (s)', fontsize=16)
plt.ylabel('Voltaje (V)', fontsize=16)

# Definir los ticks en función de los datos truncados
plt.xticks(np.arange(0, 1.6, 0.05))  # Ajuste de 0.05 para los ticks del tiempo hasta 1.5
plt.yticks(np.arange(-10, 11, 1))  # Rango de -10 a 10 con paso de 1

# Mejorar la visualización de los ticks y ajustar el layout
plt.xticks(rotation=45)
plt.tight_layout()  # Ajustar el gráfico para que no se superpongan los elementos
plt.legend()  # Mostrar leyenda para identificar cada conjunto
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
