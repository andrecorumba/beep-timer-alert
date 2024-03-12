# Beep Timer Alert

The Beep Timer Alert is a handy Python script designed to assist you during timed tests or activities by audibly notifying you to move on to the next question. This is particularly useful in settings where you're required to answer numerous questions within a limited timeframe, ensuring you allocate your time effectively across all questions.

The script works by voicing the word "next" at specified intervals, helping you keep track of time without constantly checking the clock. This tool is specifically tailored for MacOS users.

## Usage

Running the script is straightforward. For instance, to have the script say "next" every 10 seconds, you would execute the following command in your terminal:

```bash
python beep.py 10
```

## Installation

No installation is required beyond having Python installed on your MacOS machine. Simply download the `beep.py` script, and you're ready to go.

## Script Code

Below is the Python code for the Beep Timer Alert. You can customize the `time_to_beep` parameter to change the interval between alerts.

```python
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
```

## Requirements

- Python
- MacOS

This script leverages the MacOS `say` command for auditory output and does not support other operating systems.