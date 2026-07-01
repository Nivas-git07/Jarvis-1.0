"""
Microphone Module

Records audio from the microphone
and returns it as a NumPy array.
"""

import sounddevice as sd
import numpy as np

from config import (
    SAMPLE_RATE,
    CHANNELS,
    RECORD_SECONDS,
)


def listen() -> np.ndarray:
    """
    Record audio from the microphone.

    Returns:
        np.ndarray: Recorded audio.
    """

    print("🎤 Listening...")

    audio = sd.rec(
        int(SAMPLE_RATE * RECORD_SECONDS),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="float32",
    )

    sd.wait()

    print("✅ Recording Complete")

    return np.squeeze(audio)