'''
    Auto-clicker script.
    Starts and stops auto-clicking when the letter 's'
    is pressed, and ends the script once the letter 'q'
    is pressed.
'''

# Import Modules
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Declare Variables
delay = 0.001
button = Button.left
run_key = KeyCode(char = "s")
exit_key = KeyCode(char = "q")

# Clicker CLass
class ClickMouse(threading.Thread):
  # Initializer
  def __init__(self, delay, button):
    super(ClickMouse, self).__init__()
    self.delay = delay
    self.button = button
    self.clicking = False
    self.running = True
  # Start
  def start_click(self):
    self.clicking = True
  # Stop
  def stop_click(self):
    self.clicking = False
  # Exit
  def exit(self):
    self.stop_click()
    self.running = False
  # Run
  def run(self):
    while self.running:
      while self.clicking:
        mouse.click(self.button)
        time.sleep(self.delay)
      time.sleep(0.1)

# Declare Class
mouse = Controller()
clickThread = ClickMouse(delay, button)
clickThread.start()

# Process Loop
print("Clicker running")
def onPress(key):
  if key == run_key:
    if clickThread.clicking:
      clickThread.stop_click()
    else:
      clickThread.start_click()
  elif key == exit_key:
    clickThread.exit()
    listener.stop()

with Listener(on_press = onPress) as listener:
  listener.join()