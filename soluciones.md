# Estadistica Descriptiva

### 1
**¿Qué require en general de más recursos para su cálculo, la media o la mediana?**

-----------
Solución:

- **Media**: Es más sencilla y rápida de calcular. Solo se necesita sumar todos los valores y dividir entre la cantidad de datos. 

- **Mediana**: Requiere ordenar los datos primero. Una vez ordenados, seleccionas el valor central o el promedio de los dos valores centrales.

En general, **la mediana** requiere más recursos debido al proceso de ordenamiento, mientras que la **media** es más eficiente computacionalmente. Sin embargo, para datos ya ordenados, la mediana puede calcularse rápidamente.

### 2
**Supongamos que todos los precios de los productos en un e-commerce aumentan en un 5%. ¿Cómo afecta esto al precio medio de los productos?**

a) no puede determinarse sin más datos

b) El precio medio de los productos aumenta en un 5%

c) El precio medio de los productos se mantiene igual

-----------
Solución:

**b) El precio medio de los productos aumenta en un 5%**

El precio medio $\bar{x}$ es el promedio de todos los precios. Si todos los precios aumentan en un 5%, esto significa que cada precio individual $x_i$ se multiplica por 1.05. Por lo tanto, el nuevo precio medio será:

$$
\text{Nuevo precio medio} = \frac{\sum_{i=1}^n (x_i \cdot 1.05)}{n} = 1.05 \cdot \frac{\sum_{i=1}^n x_i}{n} = 1.05 \cdot \bar{x}
$$

Esto indica que el precio medio aumenta exactamente en un 5%.

### 3
**Supongamos que todos los precios de los productos en un e-commerce aumentan en un 5%. ¿Cómo afecta esto a la mediana del precio?**

a) La mediana del precio de los productos aumenta en un 5%

b) la mediana no varía

c) no puede determinarse sin más datos, la mediana requiere de una ordenación exhaustiva de todos los precios

-----------
Solución:

**a) La mediana del precio de los productos aumenta en un 5%**

La mediana es el valor central de un conjunto de datos **ordenados**. Si todos los precios aumentan en un 5%, entonces **cada precio se multiplica por 1.05**, lo que no altera el orden de los datos.

Esto significa que la **mediana también aumenta exactamente en un 5%**, ya que el aumento afecta por igual a todos los valores del conjunto y no depende de cálculos adicionales o reordenamientos.  

### 4
**Supongamos que todos los precios de los productos en un e-commerce aumentan en un 5%. ¿Cómo afecta esto a la desviación estándar del precio?**

a) la desviación estándar no cambia, una subida homogénea en todos los productos cancela el cambio en la desviación estándar

b) la desviacion estándar aumenta un 5%

c) no puede determinarse con los datos proporcionados, los valores extremos podrían influir severamente en la desviación estándar

-----------
Solución:

**b) La desviación estándar aumenta un 5%**

La desviación estándar ($\sigma$) mide cuánto se dispersan los valores respecto a la media. Si todos los precios aumentan en un 5%, entonces cada valor se multiplica por 1.05. Esto escala tanto la media como las diferencias individuales respecto a la media por el mismo factor, lo que hace que la desviación estándar también se multiplique por 1.05.

El aumento proporcional en todos los valores mantiene la relación entre las diferencias intacta, pero incrementa su magnitud. Por lo tanto, la desviación estándar aumenta exactamente en un 5%.

Recordad también de las propiedades de la Varianza (cuadrado de la desviación), que la varianza de una variable multiplicada por una constante (1.05 en este caso) es igual al cuadrado de dicha constante multiplicado por la varianza de la variable original:

$$
Var(1.05 \cdot X) = 1.05^{2} \cdot Var(X) \rightarrow \sigma = 1.05 \cdot \sigma_X
$$

### 5
**Supongamos que todos los precios de los productos en un e-commerce aumentan en un 5%. ¿Cómo afecta esto a la rango inter-cuartil de los precios?**

Recordar que el rango intercuartil es la diferencia entre los percentiles 25 y 75

a) El rango no cambia

b) El rango aumenta en un 5%

c) No puede determinarse con los datos proporcionados

-----------
Solución:

**(b) El rango aumenta en un 5%.**

El rango intercuartil (IQR) se calcula como la diferencia entre el percentil 75 ($Q_3$) y el percentil 25 ($(Q_1$):

$$
IQR = Q_3 - Q_1
$$

Si todos los precios aumentan en un 5%, cada valor del conjunto de datos, incluidos $Q_1$ y $Q_3$, se multiplica por $1.05$. Esto implica:

$$
Q_1 \text{ nuevo} = Q_1 \times 1.05, \quad Q_3 \text{ nuevo} = Q_3 \times 1.05
$$

El nuevo rango intercuartil será:

$$
IQR_{\text{nuevo}} = Q_3 \text{ nuevo} - Q_1 \text{ nuevo}
IQR_{\text{nuevo}} = (Q_3 \times 1.05) - (Q_1 \times 1.05) = 1.05 \times (Q_3 - Q_1)
$$


### 6
**Supongamos que todos los precios de los productos en un e-commerce disminuyen en $5. ¿Cómo afecta esto al precio medio de los productos?**

a) no puede determinarse sin más datos

b) El precio medio de los productos disminuye en $5

c) El precio medio de los productos se mantiene igual

-----------
Solución:

**(b) El precio medio de los productos disminuye en $5.**

El precio medio (promedio) de un conjunto de datos se calcula como:

$$
\bar{x} = \frac{\sum x_i}{n}
$$

Si a cada precio $(x_i$ se le resta $5$, el nuevo conjunto de precios será $x_i - 5$. El nuevo promedio será:

$$
\bar{x_b} = \frac{\sum (x_i - 5)}{n}
$$

Expandiendo:

$$
\bar{x_b} = \frac{\sum x_i - 5n}{n} = \frac{\sum x_i}{n} - 5
$$

Por lo tanto, el precio medio de los productos disminuye en $5$.

### 7
**Supongamos que todos los precios de los productos en un e-commerce disminuyen en $5. ¿Cómo afecta esto a la mediana del precio?**

a) la mediana no varía

b) no puede determinarse sin más datos, la mediana requiere de una ordenación exhaustiva de todos los precios

c) La mediana del precio de los productos disminuye en $5

---
Solución:

**(c) La mediana del precio de los productos disminuye en $5.**

La mediana es el valor que ocupa el lugar central en un conjunto de datos ordenado. Si a todos los valores de un conjunto se les resta $5$, el nuevo conjunto es simplemente el conjunto original desplazado hacia abajo en $5$. 

La posición relativa de los valores no cambia, pero el valor que ocupa la posición central sí disminuye en $5$. Esto implica que la mediana disminuye exactamente en \(5\).

### 8
**Supongamos que todos los precios de los productos en un e-commerce disminuyen en $5. ¿Cómo afecta esto a la desviación estándar del precio?**

a) la desviación estándar no cambia

b) la desviacion estándar disminuye en $5

c) no puede determinarse con los datos proporcionados

---
Solución:

**(a) La desviación estándar no cambia.**

La desviación estándar mide la **dispersión** de los datos respecto a la media. Se calcula como:

$$
\sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n}}
$$

Si a todos los valores $x_i$ se les resta una constante ($-5$), la nueva media $\bar{x}$ también disminuye en $5$. Sin embargo, la diferencia $x_i - \bar{x}$ permanece igual para cada dato, ya que tanto el valor como la media han cambiado en la misma cantidad. Esto significa que la dispersión de los datos no se ve afectada.

Por lo tanto, la desviación estándar no cambia al sumar o restar una constante a todos los datos del conjunto.

También podemos contestar recordando la propiedad de la **varianza** (cuadrado de la desviación) según la cual la varianza de la suma de dos variables independientes es igual a la suma de sus varianzas:

$$
Var(X + Y) = Var (X) + Var (Y)
$$

En nuestro caso, $Y$ es una constante ($5$) cuya varianza es obviamente $0$.

### 9
**Supongamos que todos los precios de los productos en un e-commerce disminuyen en $5. ¿Cómo afecta esto a la rango inter-cuartil de los precios?**

Recordar que el rango intercuartil es la diferencia entre los percentiles 25 y 75

a) El rango no cambia

b) El rango disminuye $5

c) No puede determinarse con los datos proporcionados

### 10
**Supongamos que los precios de un e-commerce tienen una desviación estándar de 10$. Todos los precios disminuyen un 5%. Cuál es la nueva desviación estándar?**

a) No puede calcularse

b) $10.5

c) $9.5

# Probabilidad

### 1
**Una moneda se tira al aire 5 veces. ¿Cual es la probabilidad de obtener como máximo 4 caras?**

### 2
**Cuando lanzas un par de dados, un doble es cuando ambos dados muestran el mismo número, por ejemplo, ambos muestran '1' o ambos muestran '4'. ¿Cuál es la probabilidad de obtener un doble al lanzar un par de dados?**

### 3
**El juego de Monopoly se juega lanzando un par de dados. Si caes en la cárcel, para salir debes lanzar un doble en cualquiera de tus siguientes tres turnos, o pagar una multa. ¿Cuál es la probabilidad de salir de la cárcel sin pagar una multa?**

### 4
**En un e-commerce, se sabe que el 70% de los usuarios que visitan el sitio web realizan una compra. Además, el 40% de los usuarios que realizan una compra han visto un producto específico, mientras que solo el 20% de los usuarios que no realizan una compra han visto ese mismo producto. Si un usuario ha visitado el producto específico, ¿cuál es la probabilidad de que realice una compra?**

### 5
**En un e-commerce, se sabe que el 30% de los usuarios que visitan el sitio web tienen una cuenta premium. Además, el 50% de los usuarios con cuenta premium realizan una compra, mientras que solo el 20% de los usuarios sin cuenta premium realizan una compra.Si un usuario realiza una compra, ¿cuál es la probabilidad de que tenga una cuenta premium?**

# Teorema del Limite Central

### 1
**Se lanza una moneda justa 400 veces. ¿Cuáles son aproximadamente las probabilidades de obtener más de 210 caras?**
**(Utiliza la regla empírica y la aproximación normal a la distribución binomial)**

### 2
**"Un grupo grande de personas se reúne y cada persona lanza una moneda 100 veces. ¿Qué porcentaje aproximado de personas obtendrá entre 40 y 60 cruces?"**
**(Utiliza la regla empírica)**

### 3
**Las puntuaciones de un determinado examen siguen una distribución normal con una media de 1350 y una desviación estándar de 120.
Para calificar para un determinado trabajo, una candidata necesita estar en el 2.5% superior. ¿Qué puntuación aproximada necesita?**
**(Utiliza la regla empírica)**

### 4
**En un e-commerce, el gasto promedio de un cliente en un día es de $50, con una desviación estándar de $20. Supongamos que seleccionas una muestra aleatoria de 100 clientes.
¿Cuál es la probabilidad de que la media sea mayor a $52?**

### 5
**En un e-commerce, el tiempo promedio que los clientes pasan navegando en el sitio web es de 8 minutos con una desviación estándar de 2 minutos. Supongamos que seleccionamos una muestra aleatoria de 50 clientes.**
**Utiliza python para calcular la probabilidad de que la media medida sobre la muestra sea mayor a 10 minutos**

### 6
**En un e-commerce, el tiempo promedio que los clientes pasan navegando en el sitio web es de 8 minutos con una desviación estándar de 2 minutos. Supongamos que seleccionamos una muestra aleatoria de 50 clientes.**
**Utilizando Python, calcula el intervalo simétrico que contiene el 95% de las medias muestrales (usa la función PPF para encontrar los percentiles correspondientes)**

### 8
**Un e-commerce quiere estimar el gasto promedio de sus clientes por transacción. A partir de una muestra de 100 transacciones, se calcula:**
**Gasto promedio: $55**
**Desviación estándar: $10**
**Construye un intervalo de confianza del 90% para el gasto promedio por transacción**

### 9
**A partir del ejercicio 8, qué tamaño de muestra necesitamos para reducir a la mitad la amplitud del intervalo de confianza?**

### 10
**A partir del ejercicio 8, sin cambiar el tamaño de muestra y si se desea reducir la amplitud del intervalo de confianza en un 20%, cual es el nuevo nivel de confianza**

# Inferencia

### 1

**Una tienda en línea quiere analizar si un nuevo proceso de checkout aumenta el uso de cupones de descuento. Para ello, realizó un test A/B donde los clientes fueron asignados aleatoriamente a dos grupos:
- Grupo A (checkout tradicional): 500 clientes.
  - 130 de ellos usaron un cupón de descuento
- Grupo B (nuevo checkout): 500 clientes.
  - 175 de ellos usaron un cupón de descuento
Tiene el **nuevo proceso de checkout** un impacto significativo en el uso de cupones? Porqué?**

# Datos Categóricos

### 1 

**Una tienda en línea quiere analizar si las categorías de productos comprados están asociadas con el canal de adquisición. Para ello recopilaron los siguientes datos**

| **Origen del tráfico** | **Electrónica** | **Ropa** | **Hogar** | **Total** |
|------------------------|----------------|----------|-----------|-----------|
| Orgánico              | 30             | 50       | 40        | 120       |
| Pago por clic         | 40             | 30       | 60        | 130       |
| Redes Sociales        | 20             | 40       | 90        | 150       |
| **Total**             | 90             | 120      | 190       | 400       |


**Existe una relación estadisticamente significativa entre el canal de adquisición y la categoría de producto comprada?**

# Regresión
