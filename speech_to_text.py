
from transformers import pipeline
import torchaudio
import torch
import soundfile as sf

print("Loading Whisper Medium...")
transcriber = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-medium"
)

print("Loading audio...")
audio, sample_rate = sf.read(
    "audio/sample2.flac",
    dtype="float32"
)

audio = torch.from_numpy(audio)

# Convert stereo to mono
if audio.ndim == 2:
    audio = audio.mean(dim=1)

print("Original sample rate:", sample_rate)

# Resample to 16 kHz if necessary
if sample_rate != 16000:
    resampler = torchaudio.transforms.Resample(
        orig_freq=sample_rate,
        new_freq=16000
    )
    audio = resampler(audio)
    sample_rate = 16000

print("Audio shape:", audio.shape)
print("Sample rate:", sample_rate)

print("Transcribing audio...")

result = transcriber(
    audio.numpy(),
    chunk_length_s=60,
    return_timestamps=True,
    generate_kwargs={
        "language": "en",
        "task": "transcribe",
        "condition_on_prev_tokens": False
    }
)

print("\nSpeech To Text Output:")
print(result["text"])
