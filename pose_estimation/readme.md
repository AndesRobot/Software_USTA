# Pose Estimator Node - Estimación de Postura en Tiempo Real usando MediaPipe y ROS 2

Este nodo de ROS 2 implementa un sistema de estimación de postura corporal utilizando **MediaPipe**. Procesa imágenes en tiempo real desde una cámara USB, detecta puntos clave del cuerpo, calcula los ángulos de los brazos y publica los resultados en dos tópicos específicos.

## Funcionalidad

- Recibe imágenes desde `/camera/image_raw`.
- Usa MediaPipe para detectar pose humana.
- Publica:
  - Ángulo del brazo izquierdo en `/angles/left_arm`
  - Ángulo del brazo derecho en `/angles/right_arm`
- Visualiza la pose y proyecta una línea indicadora si el ángulo supera un umbral.

## Requisitos

### ROS 2

- ROS 2 Humble instalado y correctamente configurado
- `cv_bridge` y `image_transport`

```bash
sudo apt install ros-humble-cv-bridge ros-humble-image-transport
```

### Python y Librerías

```bash
pip install opencv-python mediapipe numpy
```

> Si hay conflicto con protobuf:
```bash
pip install "protobuf<4.0.0"
```

## Instalación y Ejecución

### 1. Crear el workspace y clonar el repositorio

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone <URL-del-repo>
cd ..
colcon build
source install/setup.bash
```

### 2. Crear el nodo

El archivo principal del nodo debe llamarse `pose_node.py` y debe estar ubicado en la carpeta `robocup_pose_estimation/robocup_pose_estimation`.

Copia el código fuente del nodo a ese archivo y asegúrate de que sea ejecutable:

```bash
chmod +x pose_node.py
```

### 3. Configurar la cámara

ROS 2 no accede automáticamente a la webcam, por lo que se recomienda **usar el nodo `usb_cam`**, el cual puede incluirse en un archivo `pose_launch.py`. Asegúrate de tener instalado el paquete:

```bash
sudo apt install ros-humble-usb-cam
```

### 4. Crear el archivo de lanzamiento `pose_launch.py`

Ubícalo en la carpeta `robocup_pose_estimation/launch/`:

```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='usb_cam',
            parameters=[{
                'video_device': '/dev/video0',  # Cambia esto si usas otro dispositivo
                'image_width': 1280,
                'image_height': 720,
                'framerate': 30.0,
                'pixel_format': 'yuyv',
                'brightness': -10,
                'contrast': 50,
                'saturation': 70,
                'sharpness': 50,
                'autoexposure': False,
                'exposure': 100,
                'gain': 80,
                'white_balance_temperature_auto': True,
                'white_balance_temperature': 4600,
                'focus_auto': False,
                'focus': 50,
                'camera_name': 'webcam',
                'camera_info_url': ''
            }],
            remappings=[('/image_raw', '/camera/image_raw')]
        ),
        Node(
            package='robocup_pose_estimation',
            executable='pose_node',
            name='pose_estimator'
        )
    ])
```

### 5. Ejecutar el nodo

```bash
ros2 launch robocup_pose_estimation pose_launch.py
```

Esto lanza tanto la cámara como el nodo de estimación de postura.

## 🎥 ¿Cómo cambiar de cámara?

Para usar una cámara diferente, identifica el nombre del dispositivo usando:

```bash
v4l2-ctl --list-devices
```

Luego edita `pose_launch.py` y reemplaza:

```python
'video_device': '/dev/video1'
```

## Tópicos Publicados

| Tópico              | Tipo de Mensaje        | Descripción                                     |
|---------------------|------------------------|-------------------------------------------------|
| `/angles/left_arm`  | `std_msgs/msg/Float32` | Ángulo estimado del brazo izquierdo             |
| `/angles/right_arm` | `std_msgs/msg/Float32` | Ángulo estimado del brazo derecho               |

## Visualización

El nodo muestra una ventana que:
- Dibuja la pose detectada.
- Muestra los ángulos estimados en pantalla.
- Proyecta una flecha si el ángulo supera el umbral definido.

## Personalización

Puedes modificar dentro del nodo:
- `PROJECTION_THRESHOLD`: Ángulo mínimo para mostrar proyección.
- Colores de proyección (`PROJECTION_COLOR_LEFT`, `PROJECTION_COLOR_RIGHT`).
- Resolución y parámetros de cámara en `pose_launch.py`.

---

## Créditos

Este nodo fue desarrollado como parte del sistema de percepción corporal del equipo RoboCup 2025.

---

¡Gracias por usar este nodo! Para soporte adicional, contribuciones o mejoras, contáctanos o realiza un Pull Request.
