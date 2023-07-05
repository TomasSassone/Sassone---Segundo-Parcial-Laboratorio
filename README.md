# Segundo Parcial Laboratorio I - Proyecto Pygame
## Abra's Adventure


![abra-start](https://github.com/TomasSassone/SegundoParcialLaboratorio/assets/72427373/010ab999-306e-455e-b9da-1e9fcf3da896)


## Alumno
Tomás Santiago Sassone - 1°D

## Descripción
El proyecto consiste en crear un juego de temática libre utilizando el módulo Pygame.
El mismo debe incluir además formularios que conformen menúes varios (settings, selector de niveles, pausa, etc), tres niveles
cuya dificultad vaya aumentando progresivamente, enemigos, trampas, objetos con diversas funciones y un boss final.

Decidí desarrollar una narrativa centrada en la franquicia de Pokémon; A través de los distintos niveles, nuestro jugador controlará a un Abra,
un Pokémon de tipo psíquico, y tendrá que pasar por las distintas pantallas eliminando enemigos hasta llegar al boss final, donde terminará el juego.
El personaje posee las mecánicas básicas de movimiento, además de un ataque cuerpo a cuerpo, un proyectil y la habilidad de flotar, reduciendo
la velocidad de su caída y enriqueciendo la experiencia de desplazamiento por los niveles.

En el código del juego, se hace uso de diversos recursos, desde funciones, colecciones, y clases (Progamación Orientada a Objetos) hasta bases de datos para guardar la
puntuación y el nombre del jugador (SQLite).

![video-nivel](https://github.com/TomasSassone/SegundoParcialLaboratorio/assets/72427373/a58ceef6-a0d3-49db-b0d2-50600a8f36e8)



## Características del juego
1. Nuestro personaje puede moverse hacia los lados, saltar, flotar y realizar dos ataques; uno cuerpo a cuerpo y uno a distancia.
2. Los enemigos aparecerán sobre distintas superficies y dañarán al jugador al colisionar con el mismo. Además, su sprite podrá ser aleatorio entre dos variaciones.
3. Las plataformas podrán tener trampas moviéndose sobre ellas, que dañarán al jugador si éste las toca. Las trampas también pueden estar en el aire, moviéndose
  en zonas específicas que dificultarán el movimiento del jugador.
4. El jugador podrá encontrarse con dos tipos de ítems; pociones que le restaurarán una vida y carameloraros, que aumentarán su puntuación.
5. El boss final tiene muchos más puntos de vida que los enemigos, estará bloqueando la salida y lanzará piedras hacia el jugador si recibe daño de parte del mismo.
6. Los niveles deben completarse en un tiempo determinado. Si el temporizador llega a cero, el personaje morirá y será necesario reintentar el nivel.


## Fuentes
[Documentación oficial de Pygame](https://www.pygame.org/docs/index.html)

[Python Classes and Objects](https://www.w3schools.com/python/python_classes.asp)

[The Ultimate Introduction to Pygame](https://www.youtube.com/watch?v=AY9MnQ4x3zk&t=8699s)


## Gracias por ver! 🕹
