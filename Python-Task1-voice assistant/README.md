# Voice Assistant

## Project Description

This beginner Python project is a simple voice assistant. It greets the user, listens to spoken input through a microphone, converts speech to text with Google's speech recognition service, and repeats the recognized text using text-to-speech.

## Features

- Captures microphone input with `speech_recognition`
- Converts speech to text with Google's speech recognition service
- Responds with text-to-speech using `pyttsx3`
- Handles speech that cannot be understood with a repeat message

## Requirements

- Python 3.12 or later
- A working microphone
- Internet access for Google speech recognition
- `PyAudio`, `SpeechRecognition`, and `pyttsx3`

Install the dependencies with:

```powershell
py -3.12 -m pip install SpeechRecognition pyttsx3 PyAudio
```

## Run

```powershell
py -3.12 assitant.py
```

Speak after the program displays `Speak now...`.

## Project Files

- `assitant.py` - source code
- `demo-output.txt` - example console output
