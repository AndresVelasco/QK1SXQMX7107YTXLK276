## Cálculos para el Test Chi-Cuadrado

### Tabla de Frecuencias Observadas

| **Origen del tráfico** | **Electrónica** | **Ropa** | **Hogar** | **Total** |
|------------------------|----------------|----------|-----------|-----------|
| Orgánico              | 30             | 50       | 40        | 120       |
| Pago por clic         | 40             | 30       | 60        | 130       |
| Redes Sociales        | 20             | 40       | 90        | 150       |
| **Total**             | 90             | 120      | 190       | 400       |

---

### **Cálculo de las Frecuencias Esperadas**

Las frecuencias esperadas se calculan utilizando la fórmula:

\[
E_{ij} = \frac{\text{(Total de la fila i)} \times \text{(Total de la columna j)}}{\text{Total general}}
\]

1. **Frecuencia esperada para la celda (Orgánico, Electrónica):**
   \[
   E_{11} = \frac{(120 \times 90)}{400} = 27
   \]

2. **Frecuencia esperada para la celda (Orgánico, Ropa):**
   \[
   E_{12} = \frac{(120 \times 120)}{400} = 36
   \]

3. **Frecuencia esperada para la celda (Orgánico, Hogar):**
   \[
   E_{13} = \frac{(120 \times 190)}{400} = 57
   \]

4. Se repite este cálculo para todas las celdas.

### Tabla de Valores Esperados

| **Origen del tráfico** | **Electrónica (E)** | **Ropa (E)** | **Hogar (E)** | **Total** |
|------------------------|--------------------|--------------|---------------|-----------|
| Orgánico              | 27.00             | 36.00        | 57.00         | 120       |
| Pago por clic         | 29.25             | 39.00        | 61.75         | 130       |
| Redes Sociales        | 33.75             | 45.00        | 71.25         | 150       |
| **Total**             | 90                | 120          | 190           | 400       |

---

### **Cálculo del Estadístico \( \chi^2 \)**

La fórmula para calcular \( \chi^2 \) es:

\[
\chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}
\]

Donde:
- \( O_{ij} \): Frecuencias observadas.
- \( E_{ij} \): Frecuencias esperadas.

1. **Para la celda (Orgánico, Electrónica):**
   \[
   \chi^2_{11} = \frac{(30 - 27)^2}{27} = \
