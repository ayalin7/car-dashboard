from obd_reader import OBDReader
import time
from dashboard import display

reader = OBDReader()

while True:
    data = reader.read_data()
    print(data)
    time.sleep(1)