import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from TTS.api import TTS
import os
import torch
from TTS.utils.radam import RAdam
from collections import defaultdict

# Agrega todos los tipos necesarios para cargar modelos Coqui
torch.serialization.add_safe_globals([RAdam, defaultdict, dict])

class TTSNode(Node):
    def __init__(self):
        super().__init__('tts_node')
        self.subscription = self.create_subscription(
            String,
            'speak',
            self.listener_callback,
            10)
        self.get_logger().info("Inicializando Coqui TTS...")

        self.tts = TTS(model_name="tts_models/es/css10/vits", progress_bar=False, gpu=False)
        self.get_logger().info("Modelo Coqui TTS cargado correctamente.")

    def listener_callback(self, msg):
        text = msg.data
        self.get_logger().info(f"TTS: '{text}'")
        output_path = "/tmp/tts_output.wav"
        self.tts.tts_to_file(text=text, file_path=output_path)
        os.system(f"aplay {output_path}")

def main(args=None):
    rclpy.init(args=args)
    node = TTSNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
