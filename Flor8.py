import turtle
import colorsys
import pyautogui
from PIL import Image
import time

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
    frames = []
    for char in text:
        text_turtle.clear()  # Limpiar el texto anterior
        text_turtle.write(char, font=("Arial", 24, "normal"))
        text_turtle.forward(20)
        screen.update()  # Actualizar la pantalla
        # Esperar un poco antes de tomar la captura
        time.sleep(speed)
        # Capturar la pantalla con pyautogui
        img_path = "frame_text.png"
        screenshot = pyautogui.screenshot(region=(screen._root.winfo_rootx(), screen._root.winfo_rooty(), 800, 800))
        screenshot.save(img_path)
        frames.append(screenshot)
    return frames

# Configuración del turtle para la flor
flower_turtle = turtle.Turtle()
flower_turtle.speed(0)
flower_turtle.width(2)

# Función para dibujar la flor
def draw_flower():
    h = 0
    frames = []
    for i in range(195):
        flower_turtle.clear()  # Limpiar la flor anterior
        color = colorsys.hsv_to_rgb(h, 0.9, 1)
        flower_turtle.pencolor(color)
        flower_turtle.lt(179)
        flower_turtle.backward(i * 0.1)
        flower_turtle.circle(i * 0.3, 120)
        flower_turtle.rt(14)
        flower_turtle.forward(i * 0.1)
        flower_turtle.circle(i * 0.3, 120)
        h += 0.006
        # Capturar la pantalla con pyautogui
        time.sleep(0.1)
        screenshot = pyautogui.screenshot(region=(screen._root.winfo_rootx(), screen._root.winfo_rooty(), 800, 800))
        frames.append(screenshot)
        screen.update()  # Actualizar la pantalla
    return frames

# Función principal que combina el texto y la flor
def main():
    # Llamamos a la animación del texto primero
    frames_text = animate_text("Happy New Year")
    
    # Después de escribir el texto, dibujamos la flor
    flower_turtle.penup()
    flower_turtle.goto(0, -100)
    flower_turtle.pendown()
    frames_flower = draw_flower()
    
    # Guardar la animación como un GIF
    frames = frames_text + frames_flower
    frames[0].save("animation3.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)

    # Eliminar los archivos temporales
    turtle.bye()

# Llamar a la función principal
main()
