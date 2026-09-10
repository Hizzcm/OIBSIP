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
