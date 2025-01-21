import turtle
import colorsys
import io 
from PIL import Image, ImageDraw
import os

# Configuración de la pantalla
screen = turtle.Screen()
screen.bgcolor('white')
screen.setup(width=1500, height=900)

# Lista para guardar los cuadros
frames = []

# Función para capturar un frame
def capture_frame():
    # Captura la imagen de la pantalla de Turtle como un archivo PostScript
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode='color')

    # Convierte el PostScript a imagen PNG usando Pillow
    with Image.open(io.BytesIO(ps.encode('utf-8'))) as img:
        img = img.convert('RGB')  # Asegura que esté en modo RGB
        frames.append(img)

# Configuración del turtle para el texto
text_turtle = turtle.Turtle()
text_turtle.color("black")
text_turtle.penup()
text_turtle.hideturtle()
text_turtle.goto(-200, 200)
text_turtle.speed(0)

# Función para animar el texto
def animate_text(text, speed=0.1):
    for char in text:
        text_turtle.write(char, font=("Arial", 24, "normal"))
        text_turtle.forward(20)
        capture_frame()  # Captura un frame después de cada letra
        screen.update()  # Actualiza la pantalla
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
        capture_frame()  # Captura un frame después de cada paso

# Función principal que combina el texto y la flor
def main():
    # Llamamos a la animación del texto primero
    animate_text("You can do it, you are the protagonist.")
    
    # Después de escribir el texto, dibujamos la flor
    flower_turtle.penup()
    flower_turtle.goto(0, -100)
    flower_turtle.pendown()
    draw_flower()
    
    # Guardar la animación como un GIF
    frames[0].save("animation9.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)
    print("GIF generado correctamente como 'animation.gif'")
    turtle.done()

# Llamar a la función principal
main()
