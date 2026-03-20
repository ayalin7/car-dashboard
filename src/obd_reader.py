import random
import time

class OBDReader:
    def __init__(self):
        self.connected = True

    def read_data(self):
        return {
            "rpm":random.randint(700, 3000)
            "speed": random.randint(0,120)
            "temp": random.randint(70,100)
        }