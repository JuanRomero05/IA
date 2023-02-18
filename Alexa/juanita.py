import speech_recognition as sr
import pyttsx3
import pywhatkit

name = "juanita"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        pc = listener.listen(source)

    try:
        rec = listener.recognize_google(pc, language="es")
        rec = rec.lower()
    except sr.UnknownValueError:
        print("I didn't understand you, try again")
        if 'juanita' in rec:
            rec = rec.replace('juanita', '')
    return rec


def run_juanita():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        print("Reproducing: " + music)
        talk("Reproducing: " + music)
        pywhatkit.playonyt(music)


if __name__ == '__main__':
    run_juanita()
