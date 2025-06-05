import speech_recognition as sr
import pyttsx3
import datetime

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150) 

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that. Please try again.")
            return ""
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting to the speech service.")
            return ""

def process_command(query):\
    if "hello" in query:
        speak("Hi! How can I assist you today?")
    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "on led" in query:
        speak("ok sir")
        
    elif "off led" in query:    
        speak(f"ok sir")
        
    elif "exit" in query or "stop" in query:
        speak("Goodbye!")
        return False
    else:
        speak("I don't know that command. Try saying 'time', 'wikipedia something', or 'exit'.")
    return True

def main():
    speak("Voice assistant started. Say 'hello' to begin or 'exit' to stop.")
    while True:
        query = take_command()
        if query:
            if not process_command(query):
                break

if __name__ == "__main__":
    main()