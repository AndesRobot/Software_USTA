import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from vosk import Model, KaldiRecognizer
import pyaudio
import json
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

class STTNode(Node):
    def __init__(self):
        super().__init__('stt_node')
        # Models: directory where the downloaded unzipped models will be located (Change)
        # vosk-model-small-en-us-0.15: basic model of decompressed English (Change)
        model_path = os.path.expanduser('/home/juan/robo_voice/Models/vosk-model-small-en-us-0.15')
        if not os.path.exists(model_path):
            self.get_logger().error(f"The model was not found in: {model_path}")
            return

        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)

        self.publisher_ = self.create_publisher(String, 'voice_commands', 10)

        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                      channels=1,
                                      rate=16000,
                                      input=True,
                                      frames_per_buffer=8192)
        self.stream.start_stream()

        self.get_logger().info("STT node started. Say 'analyze' to display graphs or 'goodbye' to exit.")
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

                    if "analiza" in text.lower():
                        self.get_logger().info("Command 'analyze' detected.")
                        audio_data, fs = self.grabar_audio_segmento()
                        aplicar_filtros_y_graficar(audio_data, fs)

                    elif "adiós" in text.lower():
                        self.get_logger().info("Keyword 'bye' detected. Closing node.")
                        break

        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        rclpy.shutdown()

    def grabar_audio_segmento(self, segundos=5):
        fs = 16000
        frames = []
        self.get_logger().info("Recording audio segment for analysis...")
        for _ in range(0, int(fs / 4096 * segundos)):
            data = self.stream.read(4096, exception_on_overflow=False)
            frames.append(data)
        audio_bytes = b''.join(frames)
        audio_data = np.frombuffer(audio_bytes, dtype=np.int16).astype(np.float32)
        audio_data = audio_data / np.max(np.abs(audio_data))  
        return audio_data, fs

def aplicar_filtros_y_graficar(audio_data, fs):
    t = np.arange(len(audio_data)) / fs
    N = len(audio_data)
    f = np.fft.fftfreq(N, 1/fs)[:N//2]

    f0 = 1000
    bw = 100
    q = f0 / bw
    b_notch, a_notch = signal.iirnotch(f0, q, fs)
    b_butter_low, a_butter_low = signal.butter(4, 2000/(fs/2), 'low')
    b_butter_high, a_butter_high = signal.butter(4, 1000/(fs/2), 'high')
    b_lowpass = signal.firwin(50, 3000/(fs/2), pass_zero='lowpass')

    filtered_notch = signal.lfilter(b_notch, a_notch, audio_data)
    filtered_butter_low = signal.lfilter(b_butter_low, a_butter_low, audio_data)
    filtered_butter_high = signal.lfilter(b_butter_high, a_butter_high, audio_data)
    filtered_lowpass = signal.lfilter(b_lowpass, 1.0, audio_data)

    plt.figure(figsize=(15, 20))

    def plot_signal(title, signal_data, idx):
        plt.subplot(5, 2, idx)
        plt.plot(t, signal_data)
        plt.title(title + ' (Time)')
        plt.xlabel('Time (s)')
        plt.grid()

        plt.subplot(5, 2, idx + 1)
        fft_data = np.abs(np.fft.fft(signal_data))[:N//2]
        plt.plot(f, fft_data)
        plt.title(title + ' (Frequency)')
        plt.xlabel('Frequency (Hz)')
        plt.grid()

    plot_signal("Original", audio_data, 1)
    plot_signal("Notch filter", filtered_notch, 3)
    plot_signal("Butterworth Low Pass", filtered_butter_low, 5)
    plot_signal("Butterworth High Pass", filtered_butter_high, 7)
    plot_signal("Low Pass FIR", filtered_lowpass, 9)

    plt.tight_layout()
    plt.show()

def main(args=None):
    rclpy.init(args=args)
    STTNode()

if __name__ == '__main__':
    main()
