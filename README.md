# AI Voice Assistant

A Python-based AI Voice Assistant that enables users to interact through voice commands. The assistant can provide weather updates, fetch the latest news, perform sentiment analysis, extract text from images using OCR, conduct Google searches, and respond using text-to-speech technology.

## Features

* Voice Recognition using Google Speech Recognition API
* Text-to-Speech Responses
* Current Time and Date Retrieval
* Real-Time Weather Updates using OpenWeatherMap API
* Latest News Headlines using NewsAPI
* Mood Detection through Sentiment Analysis (TextBlob)
* OCR-Based Text Extraction from Images using Tesseract OCR
* Google Search Automation
* Emergency Exit using the ESC Key
* Interactive Voice-Controlled User Experience

## Technologies Used

* Python
* SpeechRecognition
* pyttsx3
* Requests
* TextBlob
* Pillow (PIL)
* pytesseract
* keyboard
* threading
* Google Search API

## Project Structure

```text
voice_assistant_project/
├── main.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd voice_assistant_project
```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR

Download and install Tesseract OCR from:

https://github.com/tesseract-ocr/tesseract

After installation, ensure Tesseract is added to your system PATH.

### 4. Configure API Keys

Open `main.py` and replace:

```python
YOUR_OPENWEATHERMAP_API_KEY
YOUR_NEWSAPI_KEY
```

with your own API keys.

## Running the Project

```bash
python main.py
```

## Available Commands

You can ask the assistant to:

* Tell the current time or date
* Provide weather updates
* Read the latest news headlines
* Analyze your mood based on speech
* Search Google
* Extract text from images
* Exit the application

## Future Enhancements

* Graphical User Interface (GUI)
* Wake Word Detection
* Multi-language Support
* Integration with Large Language Models (LLMs)
* Smart Home Automation Features

## Author

**Hrishita Bhatt**

Computer Science Student | Python Developer | AI & Machine Learning Enthusiast
