from kokoro_onnx import Kokoro
import sounddevice as sd

from config import (
    KOKORO_MODEL,
    KOKORO_VOICES,
    VOICE,
    SPEED,
)

print("🔊 Loading Kokoro...")

tts = Kokoro(
    model_path=KOKORO_MODEL,
    voices_path=KOKORO_VOICES,
)

print("✅ Kokoro Loaded")


def speak(text: str):
    samples, sample_rate = tts.create(
        text=text,
        voice=VOICE,
        speed=SPEED,
        lang="en-us",
    )

    print(f"🤖 {text}")

    sd.play(samples, sample_rate)
    sd.wait()