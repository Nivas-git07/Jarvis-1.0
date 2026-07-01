import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ==========================
# Audio
# ==========================

SAMPLE_RATE = 16000
CHANNELS = 1
RECORD_SECONDS = 5

# ==========================
# Whisper
# ==========================

WHISPER_MODEL = os.getenv("WHISPER_MODEL", "medium")
DEVICE = "cuda"
COMPUTE_TYPE = "float16"
LANGUAGE = None

# ==========================
# Kokoro (FIXED PATHS)
# ==========================




KOKORO_MODEL = os.path.join(
    BASE_DIR,
    "voice",
    "models",
    "kokoro",
    "kokoro-v1.0.onnx",
)

KOKORO_VOICES = os.path.join(
    BASE_DIR,
    "voice",
    "models",
    "kokoro",
    "voices-v1.0.bin",
)

VOICE = "af_heart"
SPEED = 1.0