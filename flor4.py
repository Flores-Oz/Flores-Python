import turtle
import colorsys

# Configuración de la pantalla
screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width=800, height=800)

# Configuración del turtle para el texto
text_turtle = turtle.Turtle()
text_turtle.color("white")
text_turtle.penup()
text_turtle.hideturtle()
text_turtle.goto(0, 200)
text_turtle.speed(0)

# Función para animar el texto
def animate_text(text, speed=0.1):
    for char in text:
        text_turtle.write(char, font=("Arial", 24, "normal"))
        text_turtle.forward(20)
        turtle.delay(int(speed * 1000))  # Espera antes de escribir la siguiente letra

# Configuración del turtle para la flor
flower_turtle = turtle.Turtle()
flower_turtle.speed(0)
flower_turtle.width(2)

# Función para dibujar la flor
def draw_flower():
    h = 0
    for i in range(195):
        color = colorsys.hsv_to_rgb(h, 0.9, 1)
        flower_turtle.pencolor(color)
        flower_turtle.lt(179)
        flower_turtle.backward(i * 0.1)
        flower_turtle.circle(i * 0.3, 120)
        flower_turtle.rt(14)
        flower_turtle.forward(i * 0.1)
        flower_turtle.circle(i * 0.3, 120)
        h += 0.006

# Función principal que combina el texto y la flor
def main():
    # Llamamos a la animación del texto primero
    animate_text("Happy New Year")
    
    # Después de escribir el texto, dibujamos la flor
    flower_turtle.penup()
    flower_turtle.goto(0, -100)
    flower_turtle.pendown()
    draw_flower()
    
    turtle.done()

# Llamar a la función principal
main()
