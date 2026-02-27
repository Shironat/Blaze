import pvporcupine
import pyaudio

class WakeWordDetector:
    def __init__(self, keyword_path):
        self.porcupine = pvporcupine.create(
            keyword_paths=[keyword_path]
        )
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length
        )

    def listen(self):
        while True:
            pcm = self.stream.read(self.porcupine.frame_length)
            pcm = memoryview(pcm).cast('h')
            result = self.porcupine.process(pcm)
            if result >= 0:
                return True