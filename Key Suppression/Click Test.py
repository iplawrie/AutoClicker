from pynput import mouse
from pynput import keyboard
from threading import Event

waiting = Event()

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))



#keyList = [0x01, 0x02, 0x04, 0x05, 0x06]

def win32_event_filter(msg, data):
    print(msg)
    keyList = [513, 514, 516, 517, 519, 520]
    for key in keyList:
        if msg == key:
            # Suppress x
            waiting.set()
            listener.suppress_event()
        else:
            listener._suppress = False
    return True



# Collect events until released
listener = mouse.Listener(
        on_click=on_click,
        on_scroll=on_scroll,
        win32_event_filter=win32_event_filter,
        suppress=False)
listener.start()
waiting.wait()