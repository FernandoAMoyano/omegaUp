# Problema de Nicolás - Selección de Juguetes

## Descripción

Nicolás es un niño muy caprichoso y sabe que su mamá hará lo posible por mantenerlo feliz. Nicolás suele aprovecharse de este hecho (por favor, no seas como Nicolás).

Cada vez que Nicolás y su mamá van a hacer las compras, el niño exige que se le compren *N* juguetes. Normalmente termina ocurriendo, pero esta vez, la madre se puso firme y le dijo a Nicolás que no le comprará *N* juguetes, sino solamente *N - 1*. Es decir, si siempre le compraba 6 juguetes, esta vez le comprará solo 4.

Nicolás está en una situación difícil y necesita conseguir la mayor diversión posible. Cada juguete tiene un nivel de diversión, la diversión final es la suma de los niveles de diversión de los juguetes adquiridos. Tu trabajo es conseguir la mayor diversión posible.

## Entrada

- Una línea con la cantidad *N* de juguetes que eligió inicialmente Nicolás.
- *N* líneas, cada una con el nivel de diversión de un juguete.

## Salida

Una línea con la mayor diversión posible habiendo dejado exactamente un juguete sin comprar (puede ser cualquiera, siempre y cuando la diversión obtenida sea la mayor posible).

## Ejemplo

| Entrada | Salida | Descripción |
|---------|--------|-------------|
| 5<br>8<br>5<br>3<br>6<br>8 | 27 | Nicolás puede tomar los juguetes 1, 2, 4 y 5. |

## Cotas

- 2 ≤ *N* ≤ 1.000.000
- 1 ≤ *Nivel de diversión* ≤ 100

## Subtareas

- *N* = 2 (19 puntos)
- *N* ≤ 1.000 (30 puntos)
- *N* ≤ 40.000 (33 puntos)
- Sin más restricciones (18 puntos)