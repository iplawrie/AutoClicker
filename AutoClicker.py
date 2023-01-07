import sys
from time import sleep
from GuiClass import *
import pyautogui as msController
from pynput import mouse, keyboard
from threading import Thread, Event

event = Event()
global idNum
#global listener


def setClickCoordinates(id_):
    print("setting click coordinates")
    global idNum
    idNum = id_
    window.showMinimized()
    listener = mouse.Listener(on_click=setCoordinates)
    listener.start()
    listener.join()
    window.showNormal()


def setAllClickCoordinates():
    print("setting all click coordinate")
    window.showMinimized()
    for i in range(0, ui.ClickObjectsNum):
        global idNum
        idNum = i
        with mouse.Listener(on_click=setCoordinates) as listener:
            listener.join()
    window.showNormal()


def getButtonText(button):
    return str(button).split('.')[1].capitalize()


def setCoordinates(x, y, button, pressed):
    if pressed:
        ui.setXCoordinates(idNum, x)
        ui.setYCoordinates(idNum, y)
        ui.setClickMethod(idNum, getButtonText(button))
        return True
    if not pressed:
        return False


def on_press():
    event.set()


def Start():
    if ui.ClickObjectsNum == 0:
        print("No Objects Detected")
        return
    print("Started Auto Clicker")
    window.showMinimized()
    loop = ui.getLoop()
    loopTime = ui.getLoopTime()
    clickTime = ui.getClickTime()
    try:
        event.clear()
        hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<alt>+z'), on_press)
        listener = keyboard.Listener(
            on_press=lambda k: hotkey.press(listener.canonical(k)))
        thread = Thread(target=threadFunction, daemon=True, args=(loop, clickTime, loopTime))
        listener.start()
        thread.start()
        while True:
            if not thread.is_alive():
                break
        listener.stop()
        print("Finished Clicking")
    except KeyboardInterrupt:
        print("Auto Click Interrupted")
    except Exception as e:
        print(e)
    finally:
        window.showNormal()


def threadFunction(loop, clicktime, looptime):
    # TODO: Allow for infinite looping
    for i in range(0, loop):
        for j in range(0, ui.ClickObjectsNum):
            if event.is_set():
                break
            x = ui.getXCoordinates(j)
            y = ui.getYCoordinates(j)
            clicks = ui.getNumClicks(j)
            # TODO: Allow for keyboard press object
            msController.click(x=x, y=y, button=ui.getClickMethod(j), clicks=clicks)
            if j < ui.ClickObjectsNum-1:
                for wait in range(0, int(clicktime * 100)):
                    if event.is_set():
                        break
                    sleep(0.01)
                if event.is_set():
                    break
        if i < loop - 1:
            for wait in range(0, int(looptime * 100)):
                if event.is_set():
                    break
                sleep(0.01)
        if event.is_set():
            break


def setButtons():
    ui.setSetButton(setClickCoordinates)
    ui.setSetAllButton(setAllClickCoordinates)
    ui.setStartButton(Start)


app = QApplication(sys.argv)
screenWidth = app.primaryScreen().size().width()
screenHeight = app.primaryScreen().size().height()
window = QMainWindow()
ui = Ui_MainWindow(window, screenWidth, screenHeight)
setButtons()
window.show()
sys.exit(app.exec_())
