import keyboard
import time
import random

def type_string(text="Hello, World!"):
    time.sleep(5)
    for char in text:
        random_delay= random.uniform(0.05,0.2)
        print(random_delay)
        time.sleep(random_delay)
        keyboard.write(char)
        
