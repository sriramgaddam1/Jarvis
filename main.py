import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import urllib.parse


engine = pyttsx3.init()

def speak(text):
  engine.say(text)
  engine.runAndWait()


def proccessCommand(c):
  print(c)
  if "open google" in c.lower():
    speak("Opening google")
    webbrowser.open("https://google.com")
  elif "open facebook" in c.lower():
    speak("Opening facebook")
    webbrowser.open("https://facebook.com")
  elif "open github" in c.lower():
    speak("Opening github")
    webbrowser.open("https://github.com")
  elif "open gpt" in c.lower():
    speak("Opening gpt")
    webbrowser.open("https://chatgpt.com")
  elif "open facebook" in c.lower():
    speak("Opening facebook")
    webbrowser.open("https://facebook.com")
  elif "open linkedin" in c.lower():
    speak("Opening Linkedin")
    webbrowser.open("https://linkedin.com")
  elif "open youtube" in c.lower():
    speak("Opening Youtube")
    webbrowser.open("https://youtube.com")
  elif c.lower().startswith("play"):
    song = c.lower().split(" ")[1]
    link=musicLibrary.music[song]
    speak(f"Playing {song}")
    webbrowser.open(link)
  elif c.lower().startswith("search about"):
    query = c.lower().replace("search about", "").strip()
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={encoded_query}"
    webbrowser.open(url)
  elif c.lower().startswith("search"):
    query = c.lower().replace("search", "").strip()
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={encoded_query}"
    webbrowser.open(url)

    

if __name__ == "__main__":
  speak("Intializing jarvis....")
  while True:
    r = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
          print("Listening...")
          audio = r.listen(source)
        print("Recognizing...")
        word=r.recognize_google(audio)
        if "jarvis" in word.lower():
           speak("Hii sir,how can i help you")
           with sr.Microphone() as source:
            print("jarvis Active...")
            audio = r.listen(source)
            print("Recognizing...")
            command=r.recognize_google(audio)
            proccessCommand(command)
        else :
            proccessCommand(word)

    except Exception as e:
        print("Error {0}".format(e))
