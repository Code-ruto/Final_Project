# Where the voice recognition happens. The speaking and listening functions are defined here as well. 
# The say function uses the edge-tts library to convert text to speech and play it back using mpg321. 
# The listen_for_input function uses the SpeechRecognition library to capture audio from the microphone and convert it to text using Google's speech recognition service. 
# Both functions include error handling to manage potential issues with voice input and output.

# !! Be sure edge-tts is updated to the latest version to avoid any issues with the Microsoft TTS API. You can update it using pip install --upgrade edge-tts !!

import sys
import shutil 
import os
import contextlib
import speech_recognition as sr
import subprocess
import time
import asyncio
from edge_tts import Communicate



@contextlib.contextmanager
def suppress_all_stderr():
    with open(os.devnull, 'w') as devnull:
        old_stderr_fd = os.dup(2)
        os.dup2(devnull.fileno(), 2)
        try:
            yield
        finally:
            os.dup2(old_stderr_fd, 2)


async def _speak_async(text: str, voice: str, filename: str):
    communicate = Communicate(text=text, voice=voice)
    await communicate.save(filename)




def speak(text, voice="en-US-JennyNeural"):
    timestamp = int(time.time())
    filename = f"/tmp/simbot_{timestamp}.mp3"

    try:
        asyncio.run(_speak_async(text, voice, filename))
        subprocess.run(
            ["mpg321", filename],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
        os.remove(filename)
    except Exception as e:
        print(f"Voice error: {e}")


def say(text):
    print(f"SimBot: {text}")
    speak(text)


def listen_for_input():
    recognizer = sr.Recognizer()
    with suppress_all_stderr():
        try:
            with sr.Microphone() as source:
                print("Listening... (say 'quit' to end)")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)

            input_text = recognizer.recognize_google(audio)
            print(f"Student (you): {input_text}")
            return input_text.lower()

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Try again.")
            return ""

        except sr.RequestError:
            print("Could not request results. Check your internet connection.")
            return ""

        except sr.WaitTimeoutError:
            print("Timeout: No speech detected. Please try again.")
            return ""

        except Exception:
            print("An unexpected error occurred during voice input.")
            return ""