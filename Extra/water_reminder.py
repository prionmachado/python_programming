import time
import pyttsx3 

REPEAT_INTERVAL = 10  # seconds
REMINDER_COUNT = 10

engine = pyttsx3.init()

for _ in range(REMINDER_COUNT):
    # Voice alert
    engine.say("Hey Ian, time to drink water")
    engine.runAndWait()

    time.sleep(REPEAT_INTERVAL)  