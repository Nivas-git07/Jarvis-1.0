"""
Voice Service

Flow:
Microphone → Whisper → Kokoro
"""

from voice.microphone import listen
from voice.stt import transcribe
from voice.tts import speak


def start():

    while True:

        print("\n🎤 Speak... (Ctrl+C to exit)")

        audio = listen()

        print("🧠 Transcribing...")

        text, language = transcribe(audio)

        if not text.strip():
            print("⚠️ No speech detected.")
            continue

        print(f"\n🌍 Language : {language}")
        print(f"📝 Text     : {text}")

        print("\n🔊 Speaking...")

        speak(text)