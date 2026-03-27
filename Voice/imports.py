import sys
import shutil 
import os
import contextlib
import speech_recognition as sr
import subprocess
import time
import logging
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
        print(f"❌ Voice error: {e}")


def say(text):
    print(f"\U0001f9d1‍⚕️ SimBot: {text}")
    # speak(text)  # Commented out for testing


def listen_for_input():
    # For testing, use text input instead of voice
    try:
        user_input = input("👩 Student (you): ").strip()
        return user_input.lower()
    except KeyboardInterrupt:
        return "quit"