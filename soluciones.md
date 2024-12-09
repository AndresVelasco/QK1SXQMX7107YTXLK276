# Estadistica Descriptiva

### 1
**¿Qué require en general de más recursos para su cálculo, la media o la mediana?**

---
Solución:

**En general, **la mediana** requiere más recursos debido al proceso de ordenamiento, mientras que la **media** es más eficiente computacionalmente**

- **Media**: Es más sencilla y rápida de calcular. Solo se necesita sumar todos los valores y dividir entre la cantidad de datos. 

- **Mediana**: Requiere ordenar los datos primero. Una vez ordenados, seleccionas el valor central o el promedio de los dos valores centrales.

En el **caso particular** de que los datos estuviesen ya ordenados, la mediana puede calcularse rápidamente.

---

### 2
**Supongamos que todos los precios de los productos en un e-commerce aumentan en un 5%. ¿Cómo afecta esto al precio medio de los productos?**

a) no puede determinarse sin más datos

b) El precio medio de los productos aumenta en un 5%

c) El precio medio de los productos se mantiene igual

---
Solución:

**b) El precio medio de los productos aumenta en un 5%**

El precio medio $\bar{x}$ es el promedio de todos los precios. Si todos los precios aumentan en un 5%, esto significa que cada precio individual $x_i$ se multiplica por 1.05. Por lo tanto, el nuevo precio medio será:

$$
\text{Nuevo precio medio} = \frac{\sum_{i=1}^n (x_i \cdot 1.05)}{n} = 1.05 \cdot \frac{\sum_{i=1}^n x_i}{n} = 1.05 \cdot \bar{x}
$$

Esto indica que el precio medio aumenta exactamente en un 5%.

---

### 3
**Supongamos que todos los precios de los productos en un e-commerce aumentan en un 5%. ¿Cómo afecta esto a la mediana del precio?**

a) La mediana del precio de los productos aumenta en un 5%

b) la mediana no varía

c) no puede determinarse sin más datos, la mediana requiere de una ordenación exhaustiva de todos los precios

---
Solución:

**a) La mediana del precio de los productos aumenta en un 5%**

La mediana es el valor central de un conjunto de datos **ordenados**. Si todos los precios aumentan en un 5%, entonces **cada precio se multiplica por 1.05**, lo que no altera el orden de los datos.

Esto significa que la **mediana también aumenta exactamente en un 5%**, ya que el aumento afecta por igual a todos los valores del conjunto y no depende de cálculos adicionales o reordenamientos.  

---

### 4
**Supongamos que todos los precios de los productos en un e-commerce aumentan en un 5%. ¿Cómo afecta esto a la desviación estándar del precio?**

a) la desviación estándar no cambia, una subida homogénea en todos los productos cancela el cambio en la desviación estándar

b) la desviacion estándar aumenta un 5%

c) no puede determinarse con los datos proporcionados, los valores extremos podrían influir severamente en la desviación estándar

---
Solución:

**b) La desviación estándar aumenta un 5%**

La desviación estándar ($\sigma$) mide cuánto se dispersan los valores respecto a la media. Si todos los precios aumentan en un 5%, entonces cada valor se multiplica por 1.05. Esto escala tanto la media como las diferencias individuales respecto a la media por el mismo factor, lo que hace que la desviación estándar también se multiplique por 1.05.

El aumento proporcional en todos los valores mantiene la relación entre las diferencias intacta, pero incrementa su magnitud. Por lo tanto, la desviación estándar aumenta exactamente en un 5%.

Recordad también de las propiedades de la Varianza (cuadrado de la desviación), que la varianza de una variable multiplicada por una constante (1.05 en este caso) es igual al cuadrado de dicha constante multiplicado por la varianza de la variable original:

$$
Var(1.05 \cdot X) = 1.05^{2} \cdot Var(X) \rightarrow \sigma = 1.05 \cdot \sigma_X
$$

---

### 5
**Supongamos que todos los precios de los productos en un e-commerce aumentan en un 5%. ¿Cómo afecta esto a la rango inter-cuartil de los precios?**

Recordar que el rango intercuartil es la diferencia entre los percentiles 25 y 75

a) El rango no cambia

b) El rango aumenta en un 5%

c) No puede determinarse con los datos proporcionados

---
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
IQR_{\text{nuevo}} = Q_3 \text{ nuevo} - Q_1 \text{ nuevo}, \quad
IQR_{\text{nuevo}} = (Q_3 \times 1.05) - (Q_1 \times 1.05) = 1.05 \times (Q_3 - Q_1)
$$

---

### 6
**Supongamos que todos los precios de los productos en un e-commerce disminuyen en $5. ¿Cómo afecta esto al precio medio de los productos?**

a) no puede determinarse sin más datos

b) El precio medio de los productos disminuye en $5

c) El precio medio de los productos se mantiene igual

---
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

---

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

---

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

---

### 9
**Supongamos que todos los precios de los productos en un e-commerce disminuyen en $5. ¿Cómo afecta esto a la rango inter-cuartil de los precios?**

Recordar que el rango intercuartil es la diferencia entre los percentiles 25 y 75

a) El rango no cambia

b) El rango disminuye $5

c) No puede determinarse con los datos proporcionados

---
Solución:

**(a) El rango no cambia.**

El rango intercuartil (IQR) se define como:

$$
IQR = Q_3 - Q_1
$$

Donde:
- $Q_3$ es el percentil 75 (tercer cuartil).
- $Q_1$ es el percentil 25 (primer cuartil).

Si a todos los valores del conjunto de datos se les resta una constante $-5$, tanto $Q_1$ como $Q_3$ disminuyen en $5$. Sin embargo, la diferencia entre ellos ($Q_3 - Q_1$) permanece igual, ya que ambas posiciones se desplazan en la misma cantidad.

Por lo tanto, el **rango intercuartil no cambia** cuando se suma o resta una constante a todos los valores del conjunto.

---

### 10
**Supongamos que los precios de un e-commerce tienen una desviación estándar de 10$. Todos los precios disminuyen un 5%. Cuál es la nueva desviación estándar?**

a) No puede calcularse

b) $10.5

c) $9.5

---
Solución:

**(c) $9.5**

Es en esencia igual que una pregunta anterior

Dismimuir los precios disminuyen un 5% es multiplicar todos los precios por $0.95$. 

La **varianza** de una variable multiplicada por una constante es igual al cuadrado de la constante multiplicado por la varianza original:

$$
Var(0.95 \cdot X) = 0.95^{2} \cdot Var(X)
$$

Como la desviación no es más que la raíz cuadrada de la varianza, la nueva desviación es $0.95$ multiplicdo por la desviación original.

---

# Probabilidad

### 1
**Una moneda se tira al aire 5 veces. ¿Cual es la probabilidad de obtener como máximo 4 caras?**

--- 
Solución: 

**Lo más sencillo es calcular esto como la probabilidad de NO obtener 5 caras:**

$$
1 - (\frac{1}{2})^{5}
$$

La probabilidad de obtener una cara es $\frac{1}{2}$. 

Cada lanzamiento es un **evento independiente** por lo que las probabilidades se multiplican.

---

### 2
**Cuando lanzas un par de dados, un doble es cuando ambos dados muestran el mismo número, por ejemplo, ambos muestran '1' o ambos muestran '4'. ¿Cuál es la probabilidad de obtener un doble al lanzar un par de dados?**

---
Solución: 

**La probabilidad de obtener un doble es **6/36** que es igual a **1/6** o aproximadamente **16.67%****

Esto es porque el número de sucesos posible es **6x6=36** (todas las combinaciones de 2 dados con 6 caras) y el número de casos favorables **6** ($1+1$, $2+2$, $3+3$, $4+4$, $5+5$, $6+6$)

---

### 3
**El juego de Monopoly se juega lanzando un par de dados. Si caes en la cárcel, para salir debes lanzar un doble en cualquiera de tus siguientes tres turnos, o pagar una multa. ¿Cuál es la probabilidad de salir de la cárcel sin pagar una multa?**

---
Solución: 

$$
1 - (\frac{5}{6})^3 \approx 0.42 (42\\%)
$$

Para calcular la probabilidad de lanzar un doble en cualquiera de los siguientes tres turnos, parece más fácil calcular la probabilidad del evento contrario (complementario) que es no sacar ningun doble, para luego restarla a uno.

$$
P(\text{al menos un doble en 3 turnos}) = 1 - P(\text{ningun doble en 3 turnos})
$$
$$
P(\text{ningun doble en 3 turnos}) = P(\text{no-doble}) \cdot P(\text{no-doble}) \cdot P(\text{no-doble})
$$

Del ejercicio anterior:

$$
P(\text{doble}) = \frac{1}{6}
$$ 

por lo que:

$$
P(\text{no-doble}) = 1 - P(\text{doble}) = 1 - \frac{1}{6} = \frac{5}{6}
$$

---

### 4
**En un e-commerce, se sabe que el 70% de los usuarios que visitan el sitio web realizan una compra. Además, el 40% de los usuarios que realizan una compra han visto un producto específico, mientras que solo el 20% de los usuarios que no realizan una compra han visto ese mismo producto. Si un usuario ha visitado el producto específico, ¿cuál es la probabilidad de que realice una compra?**

--- 
Solución:

**La probabilidad de que un usuario que ha visto el producto específico realice una compra es**

$$
P(\text{Compra} \mid \text{Visto}) \approx 0.82 (82\\%)
$$

Explicación:

Del enunciado conocemos:
- $P(\text{Compra}) = 0.7$ (probabilidad de que un usuario realice una compra)
- $P(\text{No Compra}) = 1 - P(\text{Compra}) = 0.3$ (probabilidad de que un usuario no realice una compra)
- $P(\text{Visto} \mid \text{Compra}) = 0.4$ (probabilidad de que un usuario que realiza una compra haya visto el producto)
- $P(\text{Visto} \mid \text{No Compra}) = 0.2$ (probabilidad de que un usuario que no realiza una compra haya visto el producto)

**IMPORTANTE: la frase "el 40% de los usuarios que realizan una compra han visto un producto específico" puede resultar ambigua. Pero notad que se enfoca en los usuarios que realizan una compra como el grupo base (condicional).  Luego indica que dentro de ese grupo, el 40% corresponde a los que han visto el producto específico. Esto implica la probabilidad condicional $P(\text{Visto} \mid \text{Compra})$**

La pregunta: *Si un usuario ha visitado el producto específico, ¿cuál es la probabilidad de que realice una compra?* debe interpretarse como:

$P(\text{Compra} \mid \text{Visto})$

Este es un problema de probabilidad condicional, donde usamos el teorema de Bayes:

$$
P(\text{Compra} \mid \text{Visto}) = \frac{P(\text{Visto} \mid \text{Compra}) \cdot P(\text{Compra})}{P(\text{Visto})}
$$

Primero, calculamos \(P(\text{Visto})\), la probabilidad total de que un usuario haya visto el producto, usando la regla de la probabilidad total:

$$
P(\text{Visto}) = P(\text{Visto} \mid \text{Compra}) \cdot P(\text{Compra}) + P(\text{Visto} \mid \text{No Compra}) \cdot P(\text{No Compra})
$$

Sustituyendo los valores:

$$
P(\text{Visto}) = (0.4 \cdot 0.7) + (0.2 \cdot 0.3) = 0.28 + 0.06 = 0.34
$$

Ahora usamos el teorema de Bayes para calcular $P(\text{Compra} \mid \text{Visto})$:

$$
P(\text{Compra} \mid \text{Visto}) = \frac{P(\text{Visto} \mid \text{Compra}) \cdot P(\text{Compra})}{P(\text{Visto})}
$$

Sustituyendo los valores:

$$
P(\text{Compra} \mid \text{Visto}) = \frac{0.4 \cdot 0.7}{0.34} = \frac{0.28}{0.34} \approx 0.8235
$$

Por lo tanto, la probabilidad de que un usuario que ha visto el producto específico realice una compra es:

$$
P(\text{Compra} \mid \text{Visto}) \approx 82.35\\%
$$

---

### 5
**En un e-commerce, se sabe que el 30% de los usuarios que visitan el sitio web tienen una cuenta premium. Además, el 50% de los usuarios con cuenta premium realizan una compra, mientras que solo el 20% de los usuarios sin cuenta premium realizan una compra.Si un usuario realiza una compra, ¿cuál es la probabilidad de que tenga una cuenta premium?**

--- 
Solución:

**La probabilidad de que un usuario que realiza una compra tenga una cuenta premium es:**

$$
P(\text{Premium} \mid \text{Compra}) \approx = 0.43 (43.48\\%)
$$

Explicación:

Del enunciado conocemos:
- $P(\text{Premium}) = 0.7$ (probabilidad de que un usuario tenga una cuenta premium)
- $P(\text{Compra} \mid \text{Premium}) = 0.4$ (probabilidad de que un usuario con cuenta premium realize una compra)
- $P(\text{Compra} \mid \text{No Premium}) = 0.2$ (probabilidad de que un usuario sin cuenta premium realize una compra)

La pregunta: *Si un usuario realiza una compra, ¿cuál es la probabilidad de que tenga una cuenta premium* debe interpretarse como:

$$
P(\text{Premium} \mid \text{Compra})
$$

Este es un problema de probabilidad condicional, y utilizaremos el **teorema de Bayes**:

$$
P(\text{Premium} \mid \text{Compra}) = \frac{P(\text{Compra} \mid \text{Premium}) \cdot P(\text{Premium})}{P(\text{Compra})}
$$

Primero, calculamos $P(\text{Compra})$ usando la **regla de la probabilidad total**:

$$
P(\text{Compra}) = P(\text{Compra} \mid \text{Premium}) \cdot P(\text{Premium}) + P(\text{Compra} \mid \text{No Premium}) \cdot P(\text{No Premium})
$$

Sabemos que $P(\text{No Premium}) = 1 - P(\text{Premium}) = 0.7$. Sustituyendo los valores:

$$
P(\text{Compra}) = (0.5 \cdot 0.3) + (0.2 \cdot 0.7) = 0.15 + 0.14 = 0.29
$$

Ahora usamos el **teorema de Bayes** para calcular \(P(\text{Premium} \mid \text{Compra})\):

$$
P(\text{Premium} \mid \text{Compra}) = \frac{P(\text{Compra} \mid \text{Premium}) \cdot P(\text{Premium})}{P(\text{Compra})}
$$

Sustituyendo los valores:

$$
P(\text{Premium} \mid \text{Compra}) = \frac{0.5 \cdot 0.3}{0.29} = \frac{0.15}{0.29} \approx 0.4348
$$

---

# Teorema del Limite Central

### 1
**Se lanza una moneda 400 veces. ¿Cuáles son aproximadamente las probabilidades de obtener más de 210 caras?**
**(Utiliza la regla empírica y la aproximación normal a la distribución binomial)**

---
Solución:

**La probabilidad aproximada se obtener más de $210$ caras es: $16\\%$**

Explicación:

La probabilidad $p$ de obtener cara en un lanzamiento es $\frac{1}{2} = 0.5$

En media, si repitiesemos **el experimento** de los 400 lanzamientos, varias veces, se obtendrían $400 \cdot 0.5 = 200$ caras.

Hay que tener en cuenta la aproximación normal de la distribución binomial según la cual este tipo de experimento (en este caso lanzar una moneda 400 veces), si es repetido muchas veces el número de éxitos
se distribuye según una curva normal, con media y desviación estándar:

$$
\mu = 400 \cdot 0.5 = 200
$$
$$
\sigma = \sqrt{n \cdot p \cdot (1-p)} = \sqrt{400 \cdot 0.5 \cdot 0.5} = \sqrt{100} = 10
$$

Dado que la pregunta es: *la probabilidad de obtener más de 210 caras* se puede leer como *la probabilidad de obtener un número de éxitos mayor a la media más una desviación estándar*

En una distribución normal, aproximadamente (regla empírica) **el 34% de los datos están entre la media y la media más una desviación estándar, y la mitad por supuesto quedan más arriba de la media**.

Por lo que más allá de 210 (una desviación estándar de la media) son:

$$
50 - 34 = 16%
$$

Si no nos acordasemos de la regla empírica, podemos resolverlo teniendo en cuenta que el valor estándarizado de 210 es 1 (media más **1** desviación estándar) podemos utilizar la función acumulativa de densidad de probabilidad de la función normal
que nos da la probabilidad de encontrar un valor igual o menor que el valor estandarizado dado.

```python
from scipy.stats import norm
prob = 1 - norm.cdf(1) 
```

`norm.cdf(1)` nos da la probabilidad de encontrar un valor **por debajo** de 1, por lo que la probabilidad contraria es el complementario.

Alternativamente sin haber calculado previamente el valor estándarizado $z$:

```python
from scipy.stats import norm
prob = 1 - norm.cdf(210, loc=200, scale=10) 
```

---

### 2
**Un grupo grande de personas se reúne y cada persona lanza una moneda 100 veces. ¿Qué porcentaje aproximado de personas obtendrá entre 40 y 60 cruces?**
**(Utiliza la regla empírica)**

Solución:

**La probabilidad aproximada se obtener más entre $40$ y $60$ caras es: $95.5\%$**

Explicación:

De manera análoga al ejercicio anterior, la desviación estándar del número de éxitos (cruces en este caso) al repetirse el experimento (cada uno de los 100 lanzamientos) es:

$$
\sigma = \sqrt{n \cdot p \cdot (1-p)} = \sqrt{100 \cdot 0.5 \cdot 0.5} = \sqrt{25} = 5
$$

Y la media por supuesto 50 (cruces).

40 y 60 consituyen por tanto **2 desviaciones estándar de la media en ambos sentidos**, lo que aproximadamente según la regla empírica abarca el 95.5% de las posibilidades.

Si no recordasemos esta regla, podemos utilizar la función acumulativa de densidad de probabilidad de la función normal de la siguiente manera:

```python
from scipy.stats import norm
prob = norm.cdf(2) - norm.cdf(-2) 
```

`norm.cdf(2)` nos da la probabilida de encontrar un valor por debajo de 2

`norm.cdf(-2)` nos da la probabilida de encontrar un valor por debajo de -2

La resta de ambos es la probabilidad de encontrarlo entre medias.

---

### 3
**Las puntuaciones de un determinado examen siguen una distribución normal con una media de 1350 y una desviación estándar de 120.
Para calificar para un determinado trabajo, una candidata necesita estar en el 2.5% superior. ¿Qué puntuación aproximada necesita?**
**(Utiliza la regla empírica)**

--- 
Solución: **1590**

Explicación:

La regla empírica establece que:
- El 68% de los datos están dentro de $1\sigma$ de la media,
- El 95% de los datos están dentro de $2\sigma$ de la media,
- El 99.7% de los datos están dentro de $3\sigma$ de la media.

Para el **2.5% superior**, corresponde a aproximadamente **2 desviaciones estándar por encima de la media** ((Z \approx 2\$):

$$
1350 + 2 \cdot 120 = 1590
$$

Alternativamente, si no recordamos la regla podemos utilizar python. por ejemplo:

```python
from scipy.stats import norm

# Percentil deseado (2.5% superior significa 97.5% acumulado)
percentile = 0.975

# Usamos la ppf para calcular la puntuación correspondiente
score = norm.ppf(percentile, loc=1350, scale=120)
```

---

### 4
**En un e-commerce, el gasto promedio de un cliente en un día es de $50, con una desviación estándar de $20. Supongamos que seleccionas una muestra aleatoria de 100 clientes.
¿Cuál es la probabilidad de que la media sea mayor a $52?**

---
Solución:

**La probabilidad de que la media muestral sea mayor a 52 es aproximadamente 16\%**

Podemos usar `scipy.stats.norm.cdf` para calcular la probabilidad acumulada complementaria ($P(Z > z)$) donde $z$ es el valor estandarizado correspondiente a $z$:

```python
from scipy.stats import norm

# Parámetros de la población
mu = 50  # Media
sigma = 20  # Desviación estándar
n = 100  # Tamaño de la muestra

# Parámetros de la distribución muestral
sigma_stat = sigma / (n**0.5)

# Media muestral deseada
x = 52

# Calcular el valor Z
z = (x - mu) / sigma_stat

prob = 1 - norm.cdf(z) 
print(f"La probabilidad de que la media muestral sea mayor a ${x_bar} es aproximadamente: {prob:.4f}")
```
---

### 5
**En un e-commerce, el tiempo promedio que los clientes pasan navegando en el sitio web es de 8 minutos con una desviación estándar de 2 minutos. Supongamos que seleccionamos una muestra aleatoria de 50 clientes.**
**Utiliza python para calcular la probabilidad de que la media medida sobre la muestra sea mayor a 10 minutos**

---
Solución:

**La probabilidad es prácticamente 0**

La intención del ejercicio era que se distinguiesen claramente lo que es la media y desviación estándar poblacional (8 y 2 minutos respectivamente) de la media muestral y error estándar (o desviación estándar de la media muestral).

Resolviendo con python, `scipy.stats.norm`:

```python
from scipy.stats import norm

# Parámetros de la distribución
mu = 8  # Media poblacional
sigma = 2 / (50**0.5)  # Desviación estándar de la media muestral

# Probabilidad de que la media muestral sea mayor a 10 minutos
threshold = 10
probability = 1 - norm.cdf(threshold, loc=mu, scale=sigma)

print(f"La probabilidad de que la media muestral sea mayor a {threshold} minutos es {probability:.6f}")
```
---

### 6
**En un e-commerce, el tiempo promedio que los clientes pasan navegando en el sitio web es de 8 minutos con una desviación estándar de 2 minutos. Supongamos que seleccionamos una muestra aleatoria de 50 clientes.**
**Utilizando Python, calcula el intervalo simétrico que contiene el 95% de las medias muestrales (usa la función PPF para encontrar los percentiles correspondientes)**

---
Solución:

**El intervalo del 95\% es (7.446, 8.554)**

```python
from scipy.stats import norm

# Parámetros de la distribución
mu = 8
sigma = 2 / (50**0.5)  # Desviación estándar de la media muestral

# Percentiles para el intervalo del 95%
lower_bound = norm.ppf(0.025, loc=mu, scale=sigma)
upper_bound = norm.ppf(0.975, loc=mu, scale=sigma)

print(f"El intervalo del 95% es ({lower_bound:.3f}, {upper_bound:.3f})")
```

---

### 7
**Un e-commerce quiere estimar el gasto promedio de sus clientes por transacción. A partir de una muestra de 100 transacciones, se calcula:**
**Gasto promedio: $55**
**Desviación estándar: $10**
**Construye un intervalo de confianza del 90% para el gasto promedio por transacción**

---

Solución:

**El intervalo de confianza del 90% es (53.36, 56.64)**

```python
from scipy.stats import norm

# Datos
x_bar = 55  # Media muestral
s = 10  # Desviación estándar muestral
n = 100  # Tamaño de la muestra
confidence = 90
z = norm.ppf(1 - (1 - (confidence/100)) / 2)

# Margen de error
margin_error = z * (s / (n**0.5))

# Intervalo de confianza
lower_bound = x_bar - margin_error
upper_bound = x_bar + margin_error

print(f"El intervalo de confianza del {confidence}% es ({lower_bound:.2f}, {upper_bound:.2f})")
```

---

### 8
**A partir del ejercicio 7, qué tamaño de muestra necesitamos para reducir a la mitad la amplitud del intervalo de confianza?**

---

Solución:

**Necesitamos 4 veces el tamaño de muestra original (100), es decir: 400**

Eso se debe a que el margen de error es inversamente proporcional a la raíz cuadrado de $n$ (tamaño de muestra) por lo que, fijado un $z$ (correspondiente al 95%, para reducirse a la mitad necesita multiplicarse por 4.

$$
IC = \bar{x} \pm Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}
$$

Ver solución detallada en python, como continuación del código del ejercicio anterior.

```python
from scipy.stats import norm

# Datos
x_bar = 55  # Media muestral
s = 10  # Desviación estándar muestral
n = 100  # Tamaño de la muestra
confidence = 90
z = norm.ppf(1 - (1 - (confidence/100)) / 2)

# Margen de error
margin_error = z * (s / (n**0.5))

# Intervalo de confianza
lower_bound = x_bar - margin_error
upper_bound = x_bar + margin_error

print(f"El intervalo de confianza del {confidence}% con tamaño de muestra {n} es ({lower_bound:.2f}, {upper_bound:.2f})")

# ¿Qué tamaño de muestra necesitamos para reducir a la mitad la amplitud del intervalo de confianza?

# reducimos el margen de error y despejamos el numero de muestras en la fórmula del margen de error
margin_error=margin_error/2
n= ((z*s)/(margin_error))**2

# Intervalo de confianza
lower_bound = x_bar - margin_error
upper_bound = x_bar + margin_error

print(f"El intervalo de confianza del {confidence}% con tamaño de muestra {n} es ({lower_bound:.2f}, {upper_bound:.2f})")
```

---

### 9
**A partir del ejercicio 9, sin cambiar el tamaño de muestra y si se desea reducir la amplitud del intervalo de confianza en un 20%, cual es el nuevo nivel de confianza**

---

Solución: 

**El nuevo nivel de confianza, reduciendo la amplitud del rango en un 20% con tamaño de muestra 100 es del 81.18%**

A esto se llega disminuyendo el valor de $z$ en 2:

$$
IC = \bar{x} \pm Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}
$$

Y calculando la probabilidad de que la media quede entre $-z$ y $z$ como:

$cdf(z) - ( 1 - cdf(z) ) = 2*cdf(z) - 1$

Ver solución detallada en python, como continuación del código del ejercicio anterior.

```python
from scipy.stats import norm

# Datos
x_bar = 55  # Media muestral
s = 10  # Desviación estándar muestral
n = 100  # Tamaño de la muestra
confidence = 90
z = norm.ppf(1 - (1 - (confidence/100)) / 2)

# Margen de error
margin_error = z * (s / (n**0.5))

# Intervalo de confianza
lower_bound = x_bar - margin_error
upper_bound = x_bar + margin_error

print(f"a) El intervalo de confianza del {confidence}% con tamaño de muestra {n} es ({lower_bound:.2f}, {upper_bound:.2f})")

# ¿Qué tamaño de muestra necesitamos para reducir a la mitad la amplitud del intervalo de confianza?

# reducimos el margen de error y despejamos el numero de muestras en la fórmula del margen de error
margin_error=margin_error/2
n= ((z*s)/(margin_error))**2

# Intervalo de confianza
lower_bound = x_bar - margin_error
upper_bound = x_bar + margin_error

print(f"b) El intervalo de confianza del {confidence}% con tamaño de muestra {n} es ({lower_bound:.2f}, {upper_bound:.2f})")

# Se desea reducir la amplitud del intervalo de confianza en un 20%, cual es el nuevo nivel de confianza?

# ya que no podemos aumentar el tamaño de muestra, reducimos el margen de error disminuyendo z un 20%
decrease_factor=20
z=(1-(decrease_factor/100))*z

# una vex obtenido el nuevo z, calculamos la probabilidad asociada
confidence = 2*norm.cdf(z) - 1
print(f"c) El nuevo nivel de confianza para reducir el intervalo en un {decrease_factor}% es {confidence*100}%")
```

---

# Inferencia

### 1

**Una tienda en línea quiere analizar si un nuevo proceso de checkout aumenta el uso de cupones de descuento. Para ello, realizó un test A/B donde los clientes fueron asignados aleatoriamente a dos grupos:**
- Grupo A (checkout tradicional): 500 clientes.
  - 130 de ellos usaron un cupón de descuento
- Grupo B (nuevo checkout): 500 clientes.
  - 175 de ellos usaron un cupón de descuento
    
**¿Tiene el nuevo proceso de checkout un impacto significativo en el uso de cupones? Porqué?**

Tip: aplicar un z-test de dos muestras (A/B Test)

--- 
Solución:
**El test es significativo (el proceso de checkout aumenta el uso de cupones descuento porque el p-value resultante es apenas 0.1% (muy por debajo del 5% que normalmente se considera)**

Desarrollo:
[ab test](exercise-ab_test.ipynb)

---

### 2

**Una tienda en línea con clientes recurrentes ha implementado un nuevo diseño en su página de producto. El objetivo es analizar si el nuevo diseño incrementa significativamente el tiempo promedio que los usuarios pasan en la página.**
**Para ello cuentas con el siguiente CSV que contiene los datos de tiempo en página de cada cliente, antes y después:**

Los datos se encuentran adjuntos:

[CSV](data/paired_test_ecommerce_large.csv)

Tip: aplicar un z-test para dos muestras pareadas (paired z-test). Obviar cualquier consideración relativa al tamaño de la muestra (aplicar z-test en cualquier caso por simplicidad)

--- 
Solución:
**El test es significativo (el nuevo dise.o incremental el tiempo en página, el p-value resultante es ínfimo (muy por debajo del 5% que normalmente se considera)**

[paired test](exercise-paired_test.ipynb)

---

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

Tips:

- identifica previamente el tipo de test chi-squared que debe aplicar (hay 2 variables)
- puedes optar por calcular el valor de chi-cuadrado "a mano" y calcular el p-value a partir de ello o utilizar la función [scipy.stats.chi2_contingency](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html)
  
---
Solución:

[chi-squared](exercise_chisquared-independence.ipynb)

---

