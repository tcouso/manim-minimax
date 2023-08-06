# Guión Cápsula de Búqueda Minimax


## Introducción

En este video, explicaremos el funcionamiento del algoritmo "búsqueda minimax". Este algoritmo permite implementar programas capaces de competir en juegos contra un adversario, donde el truco consistirá en construir nuestro programa de manera tal que pueda predecir los diferentes caminos que puede tomar el juego.

¿Pero por qué molestarnos en predecir el juego? Quizás podríamos simplificarnos la vida si, en lugar de anticipar todo lo que va a pasar, identificamos diferentes tipos de situaciones que pueden suceder en un juego, y guardamos en la memoria reglas que podamos usar cuando sea conveniente.

Un ejemplo muy simple. Tenemos los siguientes tableros de gato, somos los círculos y es nuestro turno. 

* Cualquiera que haya jugado a este juego sabrá que, si no bloqueamos la opción de victoria de los círculos, lo más problable es que perdamos en la siguiente jugada. 

* Al mismo tiempo, si tenemos una opción de victoria inmediata, lo lógico es tomarla. 

* Podemos repetir este ejecicio con otro tipo de situaciones más elaboradas y terminar con un programa que juegue al gato como lo haría una persona.


Sin embargo, tenemos un problema: los juegos tienen muchos tableros posibles que tendríamos que considerar. El gato, con solo 9 espacios, tiene 9! formas de jugar. 

Si queremos ser exhaustivos, tendriamos que considerar todos los escenarios posibles que nos puedan aparecer, lo que naturalmente son muchas reglas para programar.

Si quisieramos luego usar el mismo método para un juego más complejo, como el "conecta 4", la tarea pasa a ser aún más compleja, por lo que vale la pena darle la oportunidad a la idea de anticipar los resultados del juego.

¿Pero en qué consiste exactamente anticipar el juego?

En el contexto de juegos con adversario, es básicamente realizar el ejercicio de simular el desarrollo del juego alternando entre nuestra perspectiva o la de nuestro oponente.

## Analogía Min vs Max

Esta simulación puede explicarse mediante una analogía útil. Supongamos que tenemos dos jugadores imaginarios: Max y Min. Max está jugando con los círculos y  Min juega con las cruces. Nuestra metología para decidir qué hacer será simular un juego entre Max y Min, y buscar la jugada que sea más beneficiosa para Max.

Lo primero que Max tiene que hacer es mirar los resultados a los que conducen las diferentes jugadas que puede hacer desde un tablero en particular. Una vez que los tengamos, Max tiene que mirar cada uno de los tableros, y evaluarlo en base a si es una victoria, derrota o un empate. La idea aquí es elegir la jugada que lleve al mejor resultdado para Max.

Si evaluamos todos los tableros sucesores de este tablero, tenemos que ninguno es victoria, derrota o empate. Un tablero así se denomina no terminal. Cuando Max se enfrenta a un estado no terminal, significa que habrá que simular el turno de Min para saber a qué resultado nos llevará eventualmente esa jugada. 

Hagamos este proceso para el tablero de más a la derecha y simulemos el turno de Min desde ahí. Min está igual de interesado que Max en ganar, de modo que también va a buscar los tableros a los que conducen cada jugada que tiene disponible, y luego evaluar cada uno de estos en base a si es una victoria, derrota o empate para sí mismo. En este caso, Min detecto una victoria para sí mismo, de modo que optará por la jugada asociada al tablero de la izquierda. Así, el tablero que evaluamos inicialmente podrá ser etiquetado como una derrota para Max, expresando un principio importante: Un estado no terminal que evalúa Max será tan bueno como el peor de sus hijos.

Para los estados no terminales que encuentre Min, se tendrá que volver nuevamente a tomar la perspectiva de Max y repetir el procedimiento.


## Puntaje minimax

Formalicemos un poco más lo que hicimos recién. La manera de evaluar una jugada que Max empleó consistia en dos casos posibles:
* Verificar si las jugadas disponibles llevan a una victoria, derrota o un empate
* En caso de llevar a tableros no terminales, simular la elección de Min en ese escenario para evaluar la jugada

Estos dos casos se fomalizan en las siguientes expresiones: utility y minimax, para asignar puntajes a tableros terminales y no terminales, respectivamente.

Utility asigna tres puntajes a tableros terminales: 1 para victorias de Max, -1 para derrotas de Max y 0 para empates.

Minimax es una generalización de Utility para estados no terminales. Recibirá un tablero cualquiera y, en caso de no ser terminal, tomará, ya sea el máximo valor del puntaje de los tableros del siguiente nivel, si estamos en el turno de Max, o el Mínimo valor del puntaje de los tableros del siguiente nivel, si estamos en el turno de Min. En caso de ser, terminal, tomará el valor de la utilidad del estado. En este punto se explican los nombres de los jugadores de la simulación Max maximiza los puntajes, mientras que Min minimiza los puntajes.

Veamos un ejemplo. Vamos a calcular el valor minimax para asignar un puntaje al nodo raíz. El primer estado no es terminal, de modo tendremos que obtener el valor minimax de todos los estados sucesores. En el nivel 1, nos encontramos con que los estados tampoco son terminales, de modo que, nuevamente, para cada uno de estos tendremos que obtener los estados sucesores. Finalmente, llegamos al nivel 2, cuyos estados son terminales, de modo que el valor minimax será la utilidad de los nodos.

Ahora propagaremos el valor hacia los niveles más bajos. En el nivel 1 es el turno de Min, por lo que el valor minimax para cada nodo será el mínimo de los valores sus respectivos nodos hijo. En el nivel 0 es el turno de Max, de modo que el valor minimax del nodo raíz será el máximo valor minimax de los nodos del nivel 1 de profundidad.

Notamos que una vez que se disponen de estas etiquetas para todo el árbol de juego, elegir la mejor jugada desde un estado $s$ se reduce a elegir la jugada asociada al valor minimax($s$).

## Funciones de Evaluación

Un último comentario sobre los alcances de la solución. Calcular el valor minimax requiere que hagamos una exploración completa del arbol de estados del juego; eso es equivalente a simular todo desarrollo posible de un juego desde el el inicio. Para un juego como el gato, con 9! estados, podemos efectivamente hacer eso sin problemas significativos de desempeño, pero rápidamente se vuelve imposible de hacer para juegos de más complejidad.

Sin embargo, podemos hacer una transa y ceder precisión a cambio de explorar menos estados del juego. Esto es posible si modificamos el valor minimax para incluir una altura máxima $h$, y para entregar el valor de una de evaluación en caso de haberse alcanzado la altura máxima.

La función de evaluación será un procedimiento que nos otorga una estimación sobre qué tan bueno es un estado en particular, pese a no ser un empate o victoria de alguno de los jugadores. 

Retomemos brevemente el ejemplo del gato, pero ahora limitando la profundidad de la simulación al nivel 1 de profundidad. Como función de evaluación, podemos optar por el siguiente método:

evaluación = opciones de victoria Max - opciones de victorioa Min

Si aplicamos ese criterio para el tablero hijo de más a la derecha, notamos que existen dos opciones de victoria para Max (diagonal y columna derecha) y dos opciones de victoria para Min (fila superior y columna izquierda), de modo que nuestra evaluación asignará un puntaje de cero a dicho estado. Es posible verificar que, en base a este criterio, casi todos los tableros tienen un puntaje de cero. 

Para el tablero de la izquierda, no obstante, podemos verificar que Max tiene dos opciones de victoria (diagonal y columna derecha) mientras que min tiene solo una (fila inferior), de modo que nuestra evaluación otorgará un puntaje de 1 en este caso.

Así, vemos que es posible tomar la misma decisión que se tomaría al explorar el árbol completo, pero recorriendo solamente un nivel de profundidad. La calidad de la decisión de nuestro agente queda condicionada a la calidad de la estimación que elijamos. Si bien para este caso en concreto no se observan diferencias, en otras situaciones es posible que nuestro agente tome decisiones sub-óptimas.

## Pseudocódigo

El algoritmo que hemos construido a lo largo de este video se denomina "búsqueda minimax". A nivel de pseudocódigo, este puede implementarse a partir de dos funciones recursivas $max\_value(s)$ y $min\_value(s)$. Tales funciones calculan el valor minimax($s$) y el movimiento asociado a tal valor cuando es el turno de Max o Min, respectivamente.


Asumiendo que es el turno de Max en el estado $s$, comenzamos la simulación llamando a max_value($s$). Esta función tiene dos bloques de código. 

El primero es para el caso base, es decir, cuando el estado $s$ entregado es terminal, o cuando alcanzamos la profundidad máxima de exploración.

* Si el estado $s$ es terminal, la función devolverá la utilidad de dicho estado.
* Si $h=0$, alcanzamos la profundidad máxima de exploración de estados sin llegar a un estado terminal, de modo que entregaremos el valor de la función de evaluación sobre el último estado que alcanzamos.


El segundo bloque de código es el caso recursivo, cuando el estado $s$ no es terminal. Aquí, la función calculará calculará min_value($s*$) para cada uno de los estados sucesores, y retornará el máximo de dichos valores una vez que terminen de ser calculados, pues a Max le interesa llegar a los estados de máximo puntaje posible.

Veamos ahora lo que está pasando en min_value($s$).

* Si el estado $s$ es terminal, la función devolverá la utilidad de dicho estado.
* Si $h=0$, alcanzamos la profundidad máxima de exploración de estados sin llegar a un estado terminal, de modo que entregaremos el valor de la función de evaluación sobre el último estado que alcanzamos.

Si el estado $s$ no es terminal, la función calculará max_value($s*$) para todos los estados sucesores, y retornará ahora el mínimo de dichos valores cuando terminen de ser calculados, pues a Min le interesa llegar a los estados de mínimo puntaje posible. 

Con la nueva llamada a max_value, notamos que se repite el ciclo recién descrito. Este continuará hasta alcanzar el caso base, donde se asignará un valor al estado alcanzado, y todos los estados visitados terminarán de ser evaluados, de modo que Max pueda realizar la jugada óptima.