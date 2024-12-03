**Una tienda en línea quiere analizar si un nuevo proceso de checkout aumenta el uso de cupones de descuento. Para ello, realizó un test A/B donde los clientes fueron asignados aleatoriamente a dos grupos:
- Grupo A (checkout tradicional): 500 clientes.
  - 130 de ellos usaron un cupón de descuento
- Grupo B (nuevo checkout): 500 clientes.
  - 175 de ellos usaron un cupón de descuento
Tiene el **nuevo proceso de checkout** un impacto significativo en el uso de cupones? Porqué?**

## Respuesta

### Resultados del Test A/B

1. **Proporciones observadas:**
   - Grupo A (checkout tradicional): \( p_A = 0.26 \) (26%).
   - Grupo B (nuevo checkout): \( p_B = 0.35 \) (35%).

2. **Proporción conjunta (\( \hat{p} \)):**
   \[
   \hat{p} = 0.305
   \]

3. **Estadístico \( z \):**
   \[
   z = -3.09
   \]

4. **P-valor:**
   \[
   p\text{-valor} = 0.002
   \]

5. **Umbral crítico (con \( \alpha = 0.05 \)):**
   \[
   z_{\text{crítico}} = \pm 1.96
   \]

### Conclusión:

Dado que \( z = -3.09 \) está fuera del rango crítico (\( -1.96 \leq z \leq 1.96 \)) y el \( p \)-valor es menor que 0.05 (\( p\text{-valor} = 0.002 \)), rechazamos la hipótesis nula \( H_0 \).

**Interpretación:** El nuevo proceso de checkout tiene un efecto significativo en el uso de cupones.
