import soundfile as sf
import torch

audio, sample_rate = sf.read("audio/sample1.wav")

print(audio)
print(sample_rate)

waveform = torch.tensor(audio)

print(waveform.shape)