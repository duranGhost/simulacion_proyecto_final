import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definicion de carros
carros_x = np.array([450, 100])
carros_y = np.zeros_like(carros_x)
carros_z = np.zeros_like(carros_x)

# Definicion de carretera
carretera_x = np.linspace(0, 500, 100)
carretera_y = np.zeros_like(carretera_x)
carretera_z = np.zeros_like(carretera_x)

# Definicion de semaforos
# --------------------------------------------
# Rojo
semaforo_rojo_x = np.array([170, 370])
semaforo_rojo_y = np.zeros_like(semaforo_rojo_x)
semaforo_rojo_z = np.zeros_like(semaforo_rojo_x)
# Amarillo
semaforo_amarillo_x = np.array([160, 360])
semaforo_amarillo_y = np.zeros_like(semaforo_amarillo_x)
semaforo_amarillo_z = np.zeros_like(semaforo_amarillo_x)
# Verde
semaforo_verde_x = np.array([150, 350])
semaforo_verde_y = np.zeros_like(semaforo_verde_x)
semaforo_verde_z = np.zeros_like(semaforo_verde_x)
# --------------------------------------------

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
ax.scatter3D(semaforo_rojo_x, semaforo_rojo_y, semaforo_rojo_z, color='red', s=100)
ax.scatter3D(semaforo_amarillo_x, semaforo_amarillo_y, semaforo_amarillo_z, color='yellow', s=100)
ax.scatter3D(semaforo_verde_x, semaforo_verde_y, semaforo_verde_z, color='green', s=100)

# Graficar los estudiantes
ax.scatter3D(estudiantes_x, estudiantes_y, estudiantes_z, color='blue', s=100)

# Graficar los carros
ax.scatter3D(carros_x, carros_y, carros_z, color='brown', s=150)

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