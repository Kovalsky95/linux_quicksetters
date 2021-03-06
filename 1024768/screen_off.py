# https://habr.com/ru/post/118625/
# http://manpages.ubuntu.com/manpages/trusty/man1/gnome-screensaver-command.1.html
# sudo apt-get install python python-xlib
# sudo apt-get install python python3-xlib
# sudo apt install gnome-screensaver -y
import time
import subprocess
from Xlib import X
from Xlib.display import Display

display = Display(':0')
root = display.screen().root
root.grab_pointer(True,
                  X.ButtonPressMask | X.ButtonReleaseMask | X.PointerMotionMask,
                  X.GrabModeAsync, X.GrabModeAsync, 0, 0, X.CurrentTime)
root.grab_keyboard(True,
                   X.GrabModeAsync, X.GrabModeAsync, X.CurrentTime)

subprocess.call('xset dpms force off'.split())
# p = subprocess.Popen('gnome-screensaver-command --deactivate'.split())#gnome-screensaver-command --lock
time.sleep(1)

# while True:
#     display.next_event()
#     # p.terminate()
#     break