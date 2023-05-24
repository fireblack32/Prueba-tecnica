# PRUEBA TECNICA PYTHON
## Prueba tecnica para KODLAND
### Funciones Generales
Primero realice la instalacion del la libreria desde cmd con el comando: pip install pygame
La cual es la que se require para realizar el codigo.
Utilizando Visual Studio Code comence importando la libreria comence nombrando el juego el cual decidi nombrar ESQUIVA ESQUIVA
Cree la ventana en la cual trabaje para realizar el juego, dandole un alto y ancho, tambien definiendo los colores que se van a utilizar
Para poder realizar el menu principal de una manera simple realice una funcion global para poder ingresar escritos en la ventana antes creada

### Juego
Definimos el inicio y el final del juego, asi mismo como el inicio de la funcion PYGAME, con un ciclo while realizamos la definicion de la posicion, el tamaño y el movimiento el cual solo sera de derecha a izquierda en el objeto el cual sera un rectangulo y la posicion y el tamaño se dejan como variables globales, y el fondo de la ventana que será negro para despues realizar la creacion del objeto con los anteriores parametros

Despues se realiza la creacion del enemigo, de la misma forma que antes para el tamaño pero para la posicion se añadio la funcion random para dar una posicion aleatoria y un desplazamiento en el eje Y para que busque la colicion con el jugador

Por ultimo utilizando la funcion creada anterior mente para escribir se realiza el menu principal con un ciclo while dando las opciones de comenzar a jugar o salir del juego con un ciclo for y 2 condicionales





