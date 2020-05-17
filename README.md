Dadas las circunstancias, sistemas que requieran "tocar" áreas/superficies de uso masivo (Por ejemplo, sistemas de tickets para colas en un banco), podrían ser un foco de propagación de virus, es por eso que se podrían optar por sistemas o sensores que realicen las mismas tareas si la necesidad de presionar un botón/perilla, etc.

Se atacó de dos maneras:

1) Detección de Gestos, utilizando una cámara identificar los gestos de la mano para determinar que opción es la requerida por el usuario e imprimir el ticket. Para ellos se utiliza OpenCV para el manejo de la cámara y un algoritmo para la detección y análisis de Convex Hull.

2) Sensores de proximidad, utilizando un sensor de ultrasonido, poder detectar la cercanía de un objeto (Por ejemplo: la mano del interesado) y si cumple la condición de distancia mínima (10 cm en el ejemplo) imprimir el ticket, sin llegar a tocar la superficie. Se utilizó un sensor: HC-SR04, cableado a una Raspberry y un led que se enciende cuando se cumple la condición (solo para confirmación visual), al cumplir se imprimir el ticket y se toma una foto del Interesado.

https://www.youtube.com/watch?v=MnTine0iYT8&t=1s
