import speech_recognition as sr

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print("Heard:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn’t catch that.")
            return ""
        except sr.RequestError:
            print("Could not request results.")
            return ""
