import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import os

class TTSNode(Node):
    def __init__(self):
        super().__init__('tts_node')
        self.subscription = self.create_subscription(
            String,
            'speak',
            self.listener_callback,
            10)
        self.get_logger().info("TTS Node initialized.")

    def listener_callback(self, msg):
        text = msg.data
        self.get_logger().info(f"TTS: '{text}'")
        os.system(f'espeak "{text}"')  # puedes cambiar a 'festival'

def main(args=None):
    rclpy.init(args=args)
    node = TTSNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdo_
