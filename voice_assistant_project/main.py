import speech_recognition as sr
import pyttsx3
import datetime
import requests
from textblob import TextBlob
from googlesearch import search
import pytesseract
from PIL import Image
import keyboard
import threading
import webbrowser

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('volume', 1)

# Function to speak text
def speak(text):
    print(f"Ken: {text}")
    engine.say(text)
    engine.runAndWait()

# Function for speech recognition
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return None
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand what you said.")
            return None
        except sr.RequestError:
            speak("I'm having trouble connecting. Please check your internet.")
            return None

def get_time_and_date():
    now = datetime.datetime.now()
    time = now.strftime("%I:%M:%S %p")
    date = now.strftime("%Y-%m-%d")
    speak(f"The time is {time} and today's date is {date}")

def predict_mood():
    speak("Please tell me something, and I will analyze how you're feeling.")
    user_input = listen()
    if user_input:
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            speak(" Sweet You sound happy and in a good mood today! Happy for you")
        elif sentiment < 0:
            speak("You might be feeling a bit sad or down is everything alright? I hope you feel better soon.")
        else:
            speak("You seem neutral today bored enough? not too happy and not too sad.")
    else:
        speak("I couldn't understand what you said. Could you try again?")

def get_weather():
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    city = "Haldwani,Uttarakhand"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        weather_data = response.json()
        if weather_data["cod"] == 200:
            temperature = weather_data["main"]["temp"]
            description = weather_data["weather"][0]["description"]
            speak(f"The current temperature in {city} is {temperature}°C with {description}.")
        else:
            speak("I couldn't fetch the weather data.")
    except:
        speak("Please check your internet connection.")

def get_news():
    news_api_key = "YOUR_NEWSAPI_KEY"
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api_key}"
    try:
        response = requests.get(url, timeout=5)
        news_data = response.json()
        if news_data["status"] == "ok":
            for i, article in enumerate(news_data["articles"][:5]):
                title = article["title"]
                print(f"News {i + 1}: {title}")
                speak(f"News number {i + 1}: {title}")
        else:
            speak("Sorry, I couldn't fetch the news.")
    except:
        speak("Please check your internet connection.")

def describe_image(image_path):
    try:
        img = Image.open(image_path)
        img.show()
        speak("Here's the image I displayed. Description is limited in this version.")
    except:
        speak("Couldn't open the image.")

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        if text.strip():
            print("Text from image:", text)
            speak("The image contains the following text.")
            speak(text)
        else:
            speak("No readable text found.")
    except Exception as e:
        print(e)
        speak("There was an error reading the image.")

def google_search(query):
    results = search(query, num_results=1)
    webbrowser.open(results[0])
    speak("Here is the result from Google.")

def listen_for_exit():
    while True:
        if keyboard.is_pressed("esc"):
            speak("Emergency exit activated. Goodbye!")
            exit()

def main():
    threading.Thread(target=listen_for_exit, daemon=True).start()
    speak("Hello, I am your voice assistant. How can I assist you today?")
    while True:
        command = listen()
        if not command:
            continue

        if 'time' in command or 'date' in command:
            get_time_and_date()
        elif 'weather' in command:
            get_weather()
        elif 'news' in command:
            get_news()
        elif 'mood' in command or 'sentiment' in command:
            predict_mood()
        elif 'describe image' in command:
            speak("Enter the image path:")
            path = input("Image path: ")
            describe_image(path)
        elif 'read text from image' in command:
            speak("Enter the image path:")
            path = input("Image path: ")
            extract_text_from_image(path)
        elif 'search' in command:
            speak("What do you want to search for?")
            query = listen()
            if query:
                google_search(query)
        elif 'exit' in command or 'bye' in command or 'quit' in command:
            speak("Goodbye! Have a nice day.")
            break

if __name__ == "__main__":
    main()
