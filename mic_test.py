import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎙️ Speak something...")
    audio = recognizer.listen(source)

try:
    print("📝 You said:", recognizer.recognize_google(audio))
except sr.UnknownValueError:
    print("❌ Could not understand audio")
except sr.RequestError:
    print("❌ Could not request results, check internet")
