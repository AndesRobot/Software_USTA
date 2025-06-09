***

# STT_Node - Nodo de reconocimiento de voz con ROS 2 y Vosk 
Este repositorio contiene el nodo de ROS 2 en python que utiliza el motor de reconocimiento de voz Vosk para convertir voz a texto en tiempo real y publicar los comandos reconocidos en un tópico llamado `/voice_commands`.

## Requisitos
Antes de ejecutar este nodo, asegúrate de tener instalados los siguientes requisitos:

### Dependencias de Python
```bash
pip install vosk pyaudio
```
### ROS 2 
Este código está diseñado para funcionar con ROS 2 Humble, se debe tener el entorno de ROS 2 configurado correctamente.

### Modelo de Vosk
Descarga un modelo de Vosk y colócalo en un directorio de facil acceso o crear uno en el paquete. Los modelos se pueden descargar en la siguiente pagina: https://alphacephei.com/vosk/models.

## Ejecución

1. Inicia tu entorno ROS 2:

```bash
source /opt/ros/<tu-distribucion>/setup.bash
```

2. Clona el repositorio en tu workspace de ROS 2:
   
```bash
cd ~/ros2_ws/src
git clone <este-repositorio>
cd ..
colcon build
source install/setup.bash
```
3. Ejecuta el nodo:

```bash
ros2 run <nombre_del_paquete> stt_node
```
### Funcionalidad

* Captura audio desde el micrófono en tiempo real.
* Usa Vosk para transcribir el audio a texto.
* Publica el texto reconocido en el tópico voice_commands como un mensaje tipo `std_msgs/msg/String`.
* Si detecta la palabra clave "adiós", el nodo se cierra automáticamente.

## Nueva versión con análisis y filtros
Esta nueva versión amplía las capacidades del nodo stt_node al detectar la palabra clave "analyze". Al activarse:

* Graba un segmento de audio de 5 segundos.
* Aplica diferentes tipos de filtros al audio:
   * Filtro Notch para eliminar frecuencias específicas (como 1000 Hz).
   * Filtro Butterworth de paso bajo y paso alto.
   * Filtro FIR de paso bajo.
* Se generan y muestran gráficas comparando la señal original con las señales filtradas tanto en el dominio del tiempo como de la frecuencia (FFT).

Esto permite visualizar y evaluar la calidad del audio, así como el impacto de cada filtro sobre la señal.

## Uso del tópico
Puedes suscribirte al tópico con:
```bash
ros2 topic echo /voice_commands
```


***
