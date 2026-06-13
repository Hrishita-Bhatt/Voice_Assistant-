# Voice Assistant Project

### Features:
- Voice recognition (Google API)
- Text-to-speech
- Weather updates using OpenWeatherMap
- News headlines using NewsAPI
- Mood detection using sentiment analysis (TextBlob)
- Image text reading (OCR via Tesseract)
- Google search
- Emergency exit via ESC key

### Setup Instructions:
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install Tesseract OCR (for image-to-text):
Download and install from: https://github.com/tesseract-ocr/tesseract

3. Replace API keys:
Edit `main.py` and replace:
- `"YOUR_OPENWEATHERMAP_API_KEY"`
- `"YOUR_NEWSAPI_KEY"`

4. Run the assistant:
```bash
python main.py
```

Press `ESC` anytime to exit immediately.

---

Enjoy your personal voice assistant! 🎙️
