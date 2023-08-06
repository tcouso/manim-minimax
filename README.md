# Animaciones de Búsqueda Minimax con Manim

## General
* Animaciones con la librería de python [Manim](https://www.manim.community/), creadas para capsula educativa sobre búsqueda minimax.
* Explicaciones y ejemplos basados fuertemente en el capítulo 6 del texto de Russel & Norvig: [Artificial intelligence: A Modern Approach](http://aima.cs.berkeley.edu/).

## Compilado

### Paso 1: Prepara tu Archivo de Animación Python

Primero, necesitas escribir tus animaciones en un archivo Python. Este script incluye el código para crear tu animación. En nuestro ejemplo, este archivo es ```pseudocode_scene.py```. Reemplázalo por el nombre de tu archivo Python.

### Paso 2: Entendiendo las flags

El comando Manim viene con varias flags que te ayudan a personalizar el video de salida. En nuestro ejemplo, hemos usado la flag ```-qh```.

```-qh``` establece la calidad del video de salida. Tiene opciones como l para baja calidad, m para calidad media, h para alta calidad y p para calidad de producción (la más alta).

Asegúrate de reemplazar estas banderas según tu requerimiento.

### Paso 3: Nombre del Video de Salida

Por último, debes nombrar el video de salida. En nuestro caso, es PseudoCode. Reemplázalo con el nombre que quieres que tenga tu archivo de video de salida.

### Paso 4: Ejecutando el Comando

Después de establecer todos los parámetros, ejecuta el comando en tu terminal:

```
manim -qh pseudocode_scene.py PseudoCode
```



