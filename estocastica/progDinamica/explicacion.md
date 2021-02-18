# La programacion dinamica

## ¿ Que es y que no es?

La programacion dinamica es una tecnica inventada por el profesor richard bellman en el año 1953.


Nos guiamos bajo la premisa de divide y vencera. 

Por lo tanto consite en los siguientes paso:

* Dividir cada subproblema en problemas mas pequeños
* Calcular su computo recursivamente 
* Usar estas soluciones pequeñas en conjunto para construir y solucionar la grande


cuando nos dicen que hay subproblemas superpuestos lo que nos dicen es que ese problema puede divirse en problemitas más faciles. 

NO tiene nada que ver con algo que cambia su estado, no es solo un termino de marketing que se empleo para poder recibir financiamiento por parte del estado. 

## ¿ Que es memoiziation y que tiene que ver con esto?

la tecnica de memoization que es muy diferente a memorization es almacenar los computos que se puedan volver a repetir. 

Usando la gran promesa de que podemos (optimizar tiempo) vs (espacio en memoria)

En la mayoria de algoritmos para que logremos que sean mucho mas eficientes, siempre tendremos que sacrificar uno de los dos, depende cual de los dos nos conviene mas.

## Diferencia entre Subestructura optima y problemas superpuestos.

Una Subestructura optima nos dice solamente que podemos dividir el problema grandote en cuestión, en problemas muchísimo más pequeños. 

Mientras que subproblmeas superpuestos, es que para resolver el mismo problema se usa la misma logica para calcular el mayor.

Por ejemplo en la sucesion de fibonnaci para calcular f(5) = f(4) + f(3), para calcular f(4) = f(3) - f(2). Si nos damos cuenta es la misma logica para resolver lo mismo. 

Aqui usamos memoization para no tener que repetir el mismo calculo de f(3) cuando salgamos de la recursion de f(4).


## ¿Por que esto está en el ojo del data scientist? 

por que si tenemos un computador con capacidades limitadas en cuanto a memoria o no tenmos la infraestructura necesario para requerir estos computos. 

Tendremos que optar por la solucion que nos lleve más tiempo. En camvio si trabajamos haciendo simulaciones en tiempo real optaremos por sacrificar mas espacio en memoria. 


en resumen en programacion dinamica hacemos uso de 3 cosas:
* Subestructuras optimas -> dividir y vencer haciendo menos obteniendo mas
* Subproblemas superpuestos -> que significa que sigue la misma logica para resolver los problemas desde el más grande al mas pequeño en una sola cadena.

* Memoization -> almacenar los datos de los subproblemas superpuestos para no tener que volver a repetirlos completamente y optimizar la eficiencia del algoritmo. 