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

Example run:

Hello. Voice assistant is ready, also how are you doing today.
Speak now...
You said: I am doing well.
 what do you need me to do for you today
Speak now...
Sorry, I did not understand. Please repeat.

source code
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
recognizer = sr.Recognizer()


def speak(message):
    print(message)
    engine.say(message)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Speak now...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
    except sr.WaitTimeoutError:
        speak("I did not hear anything. Please try again.")
        return None
    except (OSError, AttributeError) as error:
        print(f"Microphone error: {error}")
        speak("I cannot access the microphone.")
        return None

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I did not understand. Please repeat.")
    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
    return None


def handle_command(command):
    if not command:
        return True

    if "hello" in command or "hi" in command:
        speak("Hello. How can I help you?")
    elif "time" in command:
        speak(f"The time is {datetime.now().strftime('%I:%M %p')}.")
    elif "date" in command or "day" in command:
        speak(f"Today is {datetime.now().strftime('%A, %B %d, %Y')}.")
    elif command.startswith("search for "):
        topic = command.removeprefix("search for ").strip()
        if topic:
            webbrowser.open(
                "https://www.google.com/search?q=" + topic.replace(" ", "+")
            )
            speak(f"Searching the web for {topic}.")
        else:
            speak("Please tell me what you want to search for.")
    elif command in {"goodbye", "exit", "quit", "stop"}:
        speak("Goodbye.")
        return False
    else:
        speak("I do not know that command. Please try again.")
    return True

def main():
    speak("Hello. Voice assistant is ready. What can I do for you today?")
    while True:
        command = listen()
        if not handle_command(command):
            break


if __name__ == "__main__":
    main()
