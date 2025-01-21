from turtle import *
import colorsys

# Configuración de la ventana
bgcolor('black')
pensize(2)
speed(0)
tracer(2)

# Función para escribir el nombre
def escribir_nombre():
    penup()
    goto(-200, 100)  # Posiciona la tortuga en la parte superior
    pendown()
    color("cyan")
    for letter in "Oscar":
        write(letter, font=("Arial", 48, "normal"))
        penup()
        forward(50)  # Espacio entre las letras
        pendown()

# Función para dibujar la flor
def dibujar_flor():
    h = 0
    for i in range(195):
        color = colorsys.hsv_to_rgb(h, 0.9, 1)
        h += 0.006
        pencolor(color)
        lt(179)
        backward(i * 0.1)
        circle(i * 0.3, 120)
        rt(14)
        forward(i * 0.1)
        circle(i * 0.3, 120)

# Llamar a la función para escribir el nombre y luego dibujar la flor
escribir_nombre()
ontimer(dibujar_flor, 2000)  # Retrasa la ejecución de la función dibujar_flor por 2 segundos

done()
