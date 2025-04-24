import os
import asyncio
import edge_tts
from pydub import AudioSegment
from pydub.playback import play

class Speech:
    def __init__(self, voice="en-US-AvaMultilingualNeural"):
        self.voice = voice
        self.output_file = "./data/out.mp3"

    async def speak_async(self, text):
        communicate = edge_tts.Communicate(text, self.voice)
        await communicate.save(self.output_file)

    def speak(self, text):
        asyncio.run(self.speak_async(text))
        try:
            sound = AudioSegment.from_file(self.output_file, format="mp3")
            play(sound)
            os.remove(self.output_file)
        except Exception as e:
            print(f"Playback error: {e}")
