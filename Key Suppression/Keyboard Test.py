from pynput import keyboard as kb
import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == kb.Key.esc:
        # Stop listener
        return False

#for i in range(150):
#    keyboard.block_key(i)
listener = kb.Listener(
    on_press=on_press,
    on_release=on_release,
    suppress=True)
listener.start()
listener.join()
#keyboard.unhook_all()