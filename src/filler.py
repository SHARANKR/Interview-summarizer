import random
import time

fillers = [
    "That's an interesting point.",
    "Let me think about that.",
    "That's a great question.",
    "Give me a moment to process that."
]

last_speech_time = time.time()

def detect_pause():

    global last_speech_time

    if time.time() - last_speech_time > 3:
        return random.choice(fillers)

    return None


def update_time():
    global last_speech_time
    last_speech_time = time.time()