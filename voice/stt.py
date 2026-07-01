"""
Speech-to-Text Module

Uses Faster-Whisper to convert
microphone audio into text.
"""

import tempfile

import soundfile as sf
from faster_whisper import WhisperModel

from config import (
    WHISPER_MODEL,
    DEVICE,
    COMPUTE_TYPE,
    SAMPLE_RATE,
    LANGUAGE,
)

print("🧠 Loading Whisper Model...")

model = WhisperModel(
    WHISPER_MODEL,
    device=DEVICE,
    compute_type=COMPUTE_TYPE,
)

print("✅ Whisper Loaded")


def transcribe(audio) -> tuple[str, str]:
    """
    Convert audio to text.

    Args:
        audio: NumPy audio array.

    Returns:
        tuple:
            text
            detected_language
    """

    with tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=True
    ) as temp:

        sf.write(
            temp.name,
            audio,
            SAMPLE_RATE
        )

        segments, info = model.transcribe(
            temp.name,
            language=LANGUAGE,
            beam_size=5,
            vad_filter=True,
        )

        text = " ".join(
            segment.text.strip()
            for segment in segments
        ).strip()

        return (
            text,
            info.language,
        )