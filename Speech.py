import speech_recognition as sr
from googletrans import Translator
import pyttsx3
import sys

# forcing system to use utf-8 encoding because it was giving error while printing hindi text
sys.stdout.reconfigure(encoding='utf-8')

# Initialize recognizer, translator and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
translator = Translator()

# Capture the audio input
with sr.Microphone() as source:
    print('Clearing background noise...')
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print('Waiting for message..')

    try:
        audio = recognizer.listen(source, timeout=5)
        print('Done recording..')
    except Exception as e:
        print("Error capturing audio: ", e)
        exit()

# Recognize the audio
try:
    print('Recognizing..')
    result = recognizer.recognize_google(audio, language='en')
    print(f"You said: {result}")
except Exception as ex:
    print("Error recognizing audio: ", ex)
    exit()

# Function to translate text
def trans():
    lang_input = input('Type the language code you want to convert to : ')
    
    # Translate the recognized text
    translate_text = translator.translate(result, dest=lang_input).text
    
    print(f"✅ Translated text: {translate_text}")
    
    # Convert the text to speech
    engine.say(translate_text)
    engine.runAndWait()
trans()
