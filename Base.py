import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definicion de carretera
carretera_x = np.linspace(0, 500, 100)
carretera_y = np.zeros_like(carretera_x)
carretera_z = np.zeros_like(carretera_x)

# Definicion de semaforos
semaforo_x = np.array([150, 350])
semaforo_y = np.zeros_like(semaforo_x)
semaforo_z = np.zeros_like(semaforo_x)

# Posicion estudiantes saliendo de Hipocampito
estudiantes_x = np.array([100, 400])
estudiantes_y = np.zeros_like(estudiantes_x)
estudiantes_z = np.zeros_like(estudiantes_x)

# Figura 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Graficar la carretera
ax.plot3D(carretera_x, carretera_y, carretera_z, color='black', linewidth=3)

# Graficar los semáforos
ax.scatter3D(semaforo_x, semaforo_y, semaforo_z, color='red', s=100)

# Graficar los estudiantes
ax.scatter3D(estudiantes_x, estudiantes_y, estudiantes_z, color='blue', s=100)

# Configurar la vista
ax.view_init(elev=30, azim=45)

# Configurar los límites de los ejes
ax.set_xlim(0, 500)
ax.set_ylim(-50, 50)
ax.set_zlim(-50, 50)

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar la simulación
plt.show()
