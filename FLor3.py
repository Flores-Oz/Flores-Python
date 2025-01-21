import pygame
import sys
import math
import colorsys
import turtle
from threading import Thread

# Función para la animación en Pygame
def animate_name_and_flower(width=800, height=800):
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    
    # Colores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Fuente
    font_path = "fonts/Ballet.ttf"  # Ruta de la fuente (ajusta según sea necesario)
    font = pygame.font.Font(font_path, 74)

    # Variables para la animación
    fixed_name_text = ""  # Para el nombre fijo
    write_speed = 300  # Velocidad de escritura (en milisegundos)
    last_update_time = pygame.time.get_ticks()

    # Texto fijo para el nombre
    fixed_name = "Happy New Year"

    state = "fixed_name"  # Estado inicial

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Actualiza tiempo y texto
        current_time = pygame.time.get_ticks()
        if state == "fixed_name":
            if current_time - last_update_time >= write_speed and len(fixed_name_text) < len(fixed_name):
                fixed_name_text += fixed_name[len(fixed_name_text)]
                last_update_time = current_time
            if len(fixed_name_text) == len(fixed_name):
                state = "flower"  # Cambia a la animación de la flor

        # Dibujar fondo y estrellas
        screen.fill(BLACK)

        # Mostrar el nombre fijo animado
        fixed_name_surface = font.render(fixed_name_text, True, WHITE)
        fixed_name_rect = fixed_name_surface.get_rect(center=(width // 2, height // 5))
        screen.blit(fixed_name_surface, fixed_name_rect)

        pygame.display.flip()
        clock.tick(60)

# Función para la flor con Turtle
def draw_turtle_flower():
    screen = turtle.Screen()
    screen.bgcolor('black')
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    
    h = 0

    for i in range(195):
        color = colorsys.hsv_to_rgb(h, 0.9, 1)
        h += 0.006
        t.pencolor(color)
        t.lt(179)
        t.backward(i * 0.1)
        t.circle(i * 0.3, 120)
        t.rt(14)
        t.forward(i * 0.1)
        t.circle(i * 0.3, 120)

    turtle.done()

# Función que arranca ambas animaciones
def start_animations():
    # Crear hilos para ambas animaciones (Pygame y Turtle)
    pygame_thread = Thread(target=animate_name_and_flower)
    turtle_thread = Thread(target=draw_turtle_flower)

    # Iniciar ambos hilos
    pygame_thread.start()
    turtle_thread.start()

# Llamar la función para arrancar las animaciones
start_animations()
