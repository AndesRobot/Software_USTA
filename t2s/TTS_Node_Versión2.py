import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from TTS.api import TTS
import os
import torch
from TTS.utils.radam import RAdam
from collections import defaultdict

torch.serialization.add_safe_globals([RAdam, defaultdict, dict])

class TTSNode(Node):
    def __init__(self):
        super().__init__('tts_node')

        self.get_logger().info("Inicializando Coqui TTS...")

        #Modelo en ingles = tts_models/en/vctk/vits
        #Modelo en español = tts_models/es/css10/vits
        self.tts = TTS(model_name="tts_models/es/css10/vits", progress_bar=False, gpu=False)

        # Speakers disponibles en modelo en ingles: ['ED\n', 'p225', 'p226', 'p227', 'p228', 'p229', 'p230', 'p231', 'p232', 'p233',
        # 'p234', 'p236', 'p237', 'p238', 'p239', 'p240', 'p241', 'p243', 'p244', 'p245', 'p246', 'p247', 'p248', 'p249', 'p250',
        # 'p251', 'p252', 'p253', 'p254', 'p255', 'p256', 'p257', 'p258', 'p259', 'p260', 'p261', 'p262', 'p263', 'p264', 'p265', 
        # 'p266', 'p267', 'p268', 'p269', 'p270', 'p271', 'p272', 'p273', 'p274', 'p275', 'p276', 'p277', 'p278', 'p279', 'p280', 
        # 'p281', 'p282', 'p283', 'p284', 'p285', 'p286', 'p287', 'p288', 'p292', 'p293', 'p294', 'p295', 'p297', 'p298', 'p299', 
        # 'p300', 'p301', 'p302', 'p303', 'p304', 'p305', 'p306', 'p307', 'p308', 'p310', 'p311', 'p312', 'p313', 'p314', 'p316', 
        # 'p317', 'p318', 'p323', 'p326', 'p329', 'p330', 'p333', 'p334', 'p335', 'p336', 'p339', 'p340', 'p341', 'p343', 'p345', 
        # 'p347', 'p351', 'p360', 'p361', 'p362', 'p363', 'p364', 'p374', 'p376']
        self.selected_speaker = "p294" 

        self.get_logger().info(f"Modelo Coqui TTS cargado correctamente con speaker: {self.selected_speaker}")

        self.subscription = self.create_subscription(
            String,
            'speak',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        text = msg.data
        self.get_logger().info(f"TTS: '{text}'")
        output_path = "/tmp/tts_output.wav"

        # Generar audio con el speaker seleccionado
        self.tts.tts_to_file(text=text, file_path=output_path, speaker=self.selected_speaker)

        # Reproducir el archivo
        os.system(f"aplay {output_path}")

def main(args=None):
    rclpy.init(args=args)
    node = TTSNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
