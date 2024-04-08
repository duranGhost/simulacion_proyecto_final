import numpy as np
import mayavi.mlab as mlab

# Definir la carretera
carretera_x = np.linspace(0, 500, 100)
carretera_y = np.zeros_like(carretera_x)
carretera_z = np.zeros_like(carretera_x)

# Definir la posición de los semáforos
semaforo_x = np.array([150, 350])
semaforo_y = np.zeros_like(semaforo_x)
semaforo_z = np.zeros_like(semaforo_x)

# Definir la posición de los estudiantes saliendo de Hipocampito
estudiantes_x = np.array([100, 400])
estudiantes_y = np.zeros_like(estudiantes_x)
estudiantes_z = np.zeros_like(estudiantes_x)

# Crear la figura 3D
mlab.figure(bgcolor=(1, 1, 1), size=(800, 600))

# Graficar la carretera
mlab.plot3d(carretera_x, carretera_y, carretera_z, color=(0, 0, 0), tube_radius=2)

# Graficar los semáforos
mlab.points3d(semaforo_x, semaforo_y, semaforo_z, color=(1, 0, 0), mode='sphere', scale_factor=10)

# Graficar los estudiantes
mlab.points3d(estudiantes_x, estudiantes_y, estudiantes_z, color=(0, 0, 1), mode='sphere', scale_factor=10)

# Configurar la vista
mlab.view(azimuth=45, elevation=60, distance=600, focalpoint=(250, 0, 0))

# Mostrar la simulación
mlab.show()