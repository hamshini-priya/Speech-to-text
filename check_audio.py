import soundfile as sf

audio, sr = sf.read("audio/doctor1_16k.wav")

print("Sample rate:", sr)
print("Shape:", audio.shape)
print("Duration:", len(audio) / sr, "seconds")