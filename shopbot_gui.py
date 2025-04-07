import tkinter as tk
import speech_recognition as sr
import pyttsx3
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_and_search():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        speak("What product do you want to search for?")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            status_label.config(text=f"You said: {query}")
            flipkart_url = f"https://www.flipkart.com/search?q={query}"
            webbrowser.open(flipkart_url)
        except:
            status_label.config(text="Sorry, I didn’t catch that.")
            speak("Sorry, I didn’t catch that.")

root = tk.Tk()
root.title("Voice Shopping Assistant")
root.geometry("400x200")

label = tk.Label(root, text="Press the button and speak the product name", font=("Arial", 12))
label.pack(pady=20)

button = tk.Button(root, text="🎤 Speak", command=listen_and_search, font=("Arial", 14))
button.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack(pady=10)

root.mainloop()


