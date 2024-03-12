import time
import os
import sys

def beep(time_to_beep: int = 15):
    """Function to audibly say 'next' at specified intervals on MacOS."""
    while True:
        os.system('say next')
        time.sleep(time_to_beep)

if __name__ == '__main__':
    # Set the time interval for the beep; default is 15 seconds.
    time_to_beep = int(sys.argv[1]) if len(sys.argv) > 1 else 15
    print(f"Beeping every {time_to_beep} seconds. Press Ctrl+C to stop.")
    beep(time_to_beep)