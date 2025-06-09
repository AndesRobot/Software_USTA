import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from vosk import Model, KaldiRecognizer
import pyaudio
import json
import os

class STTNode(Node):
    def __init__(self):
        super().__init__('stt_node')
        # Modelos: directory where the downloaded unzipped models will be located (Change)
        # vosk-model-small-en-us-0.15: basic model of decompressed English (Change)
        model_path = os.path.expanduser('Modelos/vosk-model-small-en-us-0.15')
        if not os.path.exists(model_path):
            self.get_logger().error(f"The model was not found in: {model_path}")
            return

        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)

        self.publisher_ = self.create_publisher(String, 'voice_commands', 10)
        # Configuración del microfono
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                      channels=1,
                                      rate=16000,
                                      input=True,
                                      frames_per_buffer=8192)
        self.stream.start_stream()

        self.get_logger().info("STT Node (Vosk, english) started.")
        self.listen_loop()

    def listen_loop(self):
        while rclpy.ok():
            data = self.stream.read(4096, exception_on_overflow=False)
            if self.recognizer.AcceptWaveform(data):
                result = json.loads(self.recognizer.Result())
                text = result.get("text", "")
                if text:
                    self.get_logger().info(f"Recognized: {text}")
                    msg = String()
                    msg.data = text
                    self.publisher_.publish(msg)

                    if "adiós" in text.lower():
                        # bye: word for ending, put according to language (Change)
                        self.get_logger().info("Keyword 'bye' detected. Closing node.")
                        break
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    STTNode()

if __name__ == '__main__':
    main()
