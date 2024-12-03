import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2, chi2_contingency

# Datos observados
observed = np.array([
    [30, 50, 40],  # Orgánico
    [40, 30, 60],  # Pago por clic
    [20, 40, 90]   # Redes Sociales
])

# Totales
row_totals = observed.sum(axis=1)
col_totals = observed.sum(axis=0)
total = observed.sum()

# Cálculo manual de frecuencias esperadas
expected = np.outer(row_totals, col_totals) / total

# Cálculo manual de chi-cuadrado
chi_squared_manual = np.sum((observed - expected) ** 2 / expected)

# Usando scipy para calcular chi-cuadrado, p-valor y grados de libertad
chi_squared, p_value, dof, expected_scipy = chi2_contingency(observed)

# Validación
print("Cálculo manual:")
print(f"Valor de chi-cuadrado (manual): {chi_squared_manual:.2f}")
print("Usando scipy:")
print(f"Valor de chi-cuadrado (scipy): {chi_squared:.2f}")
print(f"P-valor: {p_value:.5f}")
print(f"Grados de libertad: {dof}")

# Gráficos de barras (frecuencias observadas y esperadas)
categories = ["Electrónica", "Ropa", "Hogar"]
traffic_sources = ["Orgánico", "Pago por clic", "Redes Sociales"]

fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

# Frecuencias observadas
axes[0].bar(categories, observed[0], label="Orgánico", alpha=0.7)
axes[0].bar(categories, observed[1], label="Pago por clic", alpha=0.7, bottom=observed[0])
axes[0].bar(categories, observed[2], label="Redes Sociales", alpha=0.7,
            bottom=observed[0] + observed[1])
axes[0].set_title("Frecuencias Observadas")
axes[0].set_ylabel("Frecuencia")
axes[0].legend(title="Origen del tráfico")

# Frecuencias esperadas
axes[1].bar(categories, expected[0], label="Orgánico", alpha=0.7)
axes[1].bar(categories, expected[1], label="Pago por clic", alpha=0.7, bottom=expected[0])
axes[1].bar(categories, expected[2], label="Redes Sociales", alpha=0.7,
            bottom=expected[0] + expected[1])
axes[1].set_title("Frecuencias Esperadas")
axes[1].legend(title="Origen del tráfico")

plt.tight_layout()
plt.show()

# Gráfico de distribución chi-cuadrado
alpha = 0.05
critical_value = chi2.ppf(1 - alpha, dof)
x = np.linspace(0, chi_squared + 10, 500)
y = chi2.pdf(x, dof)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Distribución chi-cuadrado", lw=2)
plt.axvline(chi_squared, color="red", linestyle="--", label=f"Valor calculado: {chi_squared:.2f}")
plt.axvline(critical_value, color="blue", linestyle="--", label=f"Umbral crítico: {critical_value:.2f}")
plt.fill_between(x, y, where=(x >= critical_value), color="blue", alpha=0.3, label="Rechazo de H0")
plt.title("Distribución chi-cuadrado y valores calculados")
plt.xlabel("Valor de chi-cuadrado")
plt.ylabel("Densidad de probabilidad")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
