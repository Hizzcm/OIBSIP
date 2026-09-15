# Python Task 1 - Voice Assistant

## Project Description

This beginner Python project uses `speech_recognition` to capture voice input and `pyttsx3` to provide spoken responses. The assistant greets the user, listens to two voice inputs, and repeats recognized speech.

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