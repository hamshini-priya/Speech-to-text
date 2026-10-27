# Speech-to-Text Converter 🎙️

A Python-based application that converts audio files into text using **OpenAI Whisper** and the Hugging Face Transformers library.

## 🚀 Features

- Converts speech into text.
- Supports audio files such as WAV and FLAC.
- Uses Whisper Medium for speech recognition.
- Preprocesses audio by converting stereo to mono and resampling to 16 kHz when needed.
- Supports English transcription.

## 🛠️ Technologies Used

- Python
- Hugging Face Transformers
- OpenAI Whisper
- PyTorch
- Torchaudio
- SoundFile

## 📁 Project Structure

```text
speech-to-text/
├── audio/
│   ├── 2.wav
│   ├── 3.wav
│   └── sample.flac
├── speech_to_text.py
├── speech_to_text1.py
└── README.md
```

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone <your-repository-url>
cd speech-to-text
```

**2. Create a virtual environment (optional)**

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install transformers torch torchaudio soundfile
```

## ▶️ Usage

1. Place your audio file in the project directory or the appropriate audio folder.
2. Update the audio file path in the Python script.
3. Run the application:

```bash
python speech_to_text.py
```

4. View the transcribed text in the terminal.

## 📌 Example Output

```text
Loading Whisper Medium...
Loading audio...
Transcribing audio...

Speech To Text Output:
Your transcribed speech appears here.
```

## 🎯 Applications

- Voice-to-text conversion
- Audio transcription
- Speech recognition experiments
- Accessibility tools
- Audio data processing

## 🔮 Future Improvements

- Add a graphical user interface.
- Support multiple languages.
- Allow users to upload audio files.
- Export transcripts to TXT or PDF files.

## 👩‍💻 Author

**Your Name**

## 📄 License

This project is intended for educational and learning purposes.
