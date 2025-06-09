***

# TTS_Node - Nodo TTS para ROS 2 y Coqui TTS
Existen dos versiones del nodo: una versión simple utilizando `espeak`, y una versión avanzada usando **Coqui TTS**, con soporte para voz natural en español e inglés.

## Requisitos
Antes de ejecutar este nodo, asegúrate de tener instalados los siguientes requisitos:

### Dependencias de Python
```bash
pip install TTS
```
### Instalación de paquetes de software
```bash
sudo apt install espeak alsa-utils
```
### ROS 2 
Estos códigos están diseñados para funcionar con ROS 2 Humble, se debe tener el entorno de ROS 2 configurado correctamente.

## Versiones del nodo

### Versión 1 - Simple con espeak
* Utiliza la herramienta `espeak` para síntesis rápida.
* Ligera, sin dependencias externas.
* Solo voz robótica, no natural.

### Versión 2 - Avanzada con Coqui TTS
* Utiliza el modelo `tts_models/en/vctk/vits`(voz natural, multilenguaje).
* Requiere indicar el speaker (voz en inglés).
* Soporte para español si se cambia el modelo a `tts_models/es/css10/vits`.

## Uso del tópico
Puedes suscribirte al tópico con:
```bash
ros2 topic pub /speak std_msgs/String "{data: 'Message'}"
```

***
