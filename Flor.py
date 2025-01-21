import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configuración de la figura
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_ylim(0, 1.5)
ax.set_xticks([])
ax.set_yticks([])

# Generar datos iniciales
theta = np.linspace(0, 2 * np.pi, 1000)
flower, = ax.plot([], [], lw=2, color='magenta')

# Función para actualizar los frames
def update(frame):
    k = 5  # Número de pétalos
    r = np.abs(np.sin(k * theta + frame / 10) + 1) / 2
    flower.set_data(theta, r)
    return flower,

# Configuración de la animación
ani = FuncAnimation(
    fig, update, frames=np.arange(0, 200), interval=50, blit=True
)

plt.show()
