# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UICreator.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from time import sleep
from pynput import mouse as msListener    #Mouse Listener
from pynput import keyboard as kb   #Keyboard Listener
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import pyautogui as msController  #Mouse Controller
from threading import Thread
from threading import Event

event = Event()

class Ui_MainWindow(QMainWindow):
    ClickObjects = []
    ClickObjectsNum = 0

    def setupUi(self, MainWindow, screenWidth, screenHeight):
        self.MainWindow = MainWindow
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(802, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(60, 40, 661, 491))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # Radio Buttons
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leftClick = QtWidgets.QRadioButton(self.horizontalWidget)
        self.leftClick.setObjectName("leftClick")
        self.leftClick.setChecked(True)
        self.horizontalLayout_2.addWidget(self.leftClick)
        self.rightClick = QtWidgets.QRadioButton(self.horizontalWidget)
        self.rightClick.setObjectName("rightClick")
        self.horizontalLayout_2.addWidget(self.rightClick)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # Start Stop
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.startButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.startButton.setObjectName("start")
        self.horizontalLayout_3.addWidget(self.startButton)
        self.stopKeyboardControl = QtWidgets.QLabel(self.horizontalWidget)
        self.stopKeyboardControl.setAlignment(QtCore.Qt.AlignCenter)
        self.stopKeyboardControl.setObjectName("stop")
        self.horizontalLayout_3.addWidget(self.stopKeyboardControl)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        # Sleep and loops count
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.clickTime = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.clickTime.setPrefix("Time Between Clicks:  ")
        self.clickTime.setMinimum(0.1)
        self.clickTime.setSingleStep(0.10)
        self.clickTime.setObjectName("clickTime")
        self.horizontalLayout_4.addWidget(self.clickTime)
        self.loopTime = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.loopTime.setPrefix("Time Between Loops:  ")
        self.loopTime.setMinimum(0.1)
        self.loopTime.setSingleStep(0.10)
        self.loopTime.setObjectName("loopTime")
        self.horizontalLayout_4.addWidget(self.loopTime)
        self.numLoop = QtWidgets.QSpinBox(self.horizontalWidget)
        self.numLoop.setPrefix("Loop Count:  ")
        self.numLoop.setValue(1)
        self.numLoop.setMinimum(0)
        self.numLoop.setObjectName("numLoop")
        self.horizontalLayout_4.addWidget(self.numLoop)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        # Scrollable click objects header
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.addClickObjectButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.addClickObjectButton.setObjectName("add")
        self.horizontalLayout_5.addWidget(self.addClickObjectButton)
        self.removeAllButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.removeAllButton.setObjectName("removeAll")
        self.horizontalLayout_5.addWidget(self.removeAllButton)
        self.setAllButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.setAllButton.setObjectName("setAll")
        self.horizontalLayout_5.addWidget(self.setAllButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        # Scroll Area
        self.scrollArea = QtWidgets.QScrollArea(self.horizontalWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 639, 74))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.removeButtonGroup = QButtonGroup()
        self.removeButtonGroup.setExclusive(True)
        self.removeButtonGroup.idClicked.connect(self.removeClickObject)
        self.setButtonGroup = QButtonGroup()
        self.setButtonGroup.setExclusive(True)
        self.setButtonGroup.idClicked.connect(self.setClickCoor)
        self.upButtonGroup = QButtonGroup()
        self.upButtonGroup.setExclusive(True)
        self.upButtonGroup.idClicked.connect(self.shiftUp)
        self.downButtonGroup = QButtonGroup()
        self.downButtonGroup.setExclusive(True)
        self.downButtonGroup.idClicked.connect(self.shiftDown)
        self.addClickObject()

        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Button Presses
        self.addClickObjectButton.clicked.connect(self.addClickObject)
        self.removeAllButton.clicked.connect(self.removeAllClickObject)
        self.setAllButton.clicked.connect(self.setAllClickCoor)
        self.startButton.clicked.connect(self.Start)

    def addClickObject(self):
        print("adding click object")
        self.clickObjectHorizontalCanvas = QtWidgets.QHBoxLayout()
        self.clickObjectHorizontalCanvas.setSpacing(5)
        self.clickObjectHorizontalCanvas.setObjectName("horizontalLayout_6")
        self.numLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.numLabel.setFont(font)
        self.numLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.numLabel.setObjectName("Number")
        self.numLabel.setText(str(self.ClickObjectsNum))
        self.clickObjectHorizontalCanvas.addWidget(self.numLabel)
        self.setButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.setButton.setObjectName("setCoor")
        self.setButton.setText("Set")
        self.setButtonGroup.addButton(self.setButton, self.ClickObjectsNum)
        self.clickObjectHorizontalCanvas.addWidget(self.setButton)
        self.xCoor = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.xCoor.setObjectName("xCoor")
        self.xCoor.setPrefix("X:  ")
        self.xCoor.setRange(1, self.screenWidth)
        self.clickObjectHorizontalCanvas.addWidget(self.xCoor)
        self.yCoor = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.yCoor.setObjectName("yCoor")
        self.yCoor.setPrefix("Y:  ")
        self.yCoor.setRange(1, self.screenHeight)
        self.clickObjectHorizontalCanvas.addWidget(self.yCoor)
        self.removeButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.removeButton.setObjectName("remove")
        self.removeButton.setText("Remove")
        self.removeButtonGroup.addButton(self.removeButton, self.ClickObjectsNum)
        self.clickObjectHorizontalCanvas.addWidget(self.removeButton)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.moveUp = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.moveUp.setObjectName("moveUp")
        self.moveUp.setText("Up")
        self.upButtonGroup.addButton(self.moveUp, self.ClickObjectsNum)
        self.verticalLayout_3.addWidget(self.moveUp)
        self.moveDown = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.moveDown.setObjectName("moveDown")
        self.moveDown.setText("Down")
        self.downButtonGroup.addButton(self.moveDown, self.ClickObjectsNum)
        self.verticalLayout_3.addWidget(self.moveDown)

        self.clickObjectHorizontalCanvas.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.clickObjectHorizontalCanvas)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.ClickObjects.append(self.clickObjectHorizontalCanvas)
        self.ClickObjectsNum = self.ClickObjectsNum + 1

    def removeClickObject(self, id_):
        print("removing click object")
        if self.ClickObjectsNum > 1:
            deleteItemsOfLayout(self.ClickObjects[id_])
            self.ClickObjects.pop(id_)
            self.ClickObjectsNum = self.ClickObjectsNum - 1
            for i in range(id_, self.ClickObjectsNum):
                self.removeButtonGroup.setId(self.removeButtonGroup.button(i + 1), i)
                self.setButtonGroup.setId(self.setButtonGroup.button(i + 1), i)
                self.ClickObjects[i].itemAt(0).widget().setText(str(i))

    def removeAllClickObject(self):
        print("remove all click objects")
        for clickObjects in self.ClickObjects:
            deleteItemsOfLayout(clickObjects)
        self.ClickObjectsNum = 0
        self.ClickObjects.clear()
        self.addClickObject()

    def setClickCoor(self, id_):
        self.id = id_
        print("setting click coordinates")
        self.MainWindow.showMinimized()
        with msListener.Listener(on_click=self.setCordinates) as listener:
            listener.join()
        self.MainWindow.showNormal()

    def setAllClickCoor(self):
        print("setting all click coordinate")
        self.MainWindow.showMinimized()
        for i in range(0, self.ClickObjectsNum):
            self.id = i
            with msListener.Listener(on_click=self.setCordinates) as listener:
                listener.join()
        self.MainWindow.showNormal()

    def setCordinates(self, x, y, button, pressed):
        if pressed:
            self.ClickObjects[self.id].itemAt(2).widget().setValue(x)
            self.ClickObjects[self.id].itemAt(3).widget().setValue(y)
        if not pressed:
            return False

    def shiftUp(self, id_):
        x = self.ClickObjects[id_].itemAt(2).widget().value()
        y = self.ClickObjects[id_].itemAt(3).widget().value()
        if id_ > 0:
            tempX = self.ClickObjects[id_ - 1].itemAt(2).widget().value()
            tempY = self.ClickObjects[id_ - 1].itemAt(3).widget().value()
            self.ClickObjects[id_ - 1].itemAt(2).widget().setValue(x)
            self.ClickObjects[id_ - 1].itemAt(3).widget().setValue(y)
            self.ClickObjects[id_].itemAt(2).widget().setValue(tempX)
            self.ClickObjects[id_].itemAt(3).widget().setValue(tempY)

    def shiftDown(self, id_):
        x = self.ClickObjects[id_].itemAt(2).widget().value()
        y = self.ClickObjects[id_].itemAt(3).widget().value()
        if id_ < self.ClickObjectsNum-1:
            tempX = self.ClickObjects[id_ + 1].itemAt(2).widget().value()
            tempY = self.ClickObjects[id_ + 1].itemAt(3).widget().value()
            self.ClickObjects[id_ + 1].itemAt(2).widget().setValue(x)
            self.ClickObjects[id_ + 1].itemAt(3).widget().setValue(y)
            self.ClickObjects[id_].itemAt(2).widget().setValue(tempX)
            self.ClickObjects[id_].itemAt(3).widget().setValue(tempY)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.leftClick.setText(_translate("MainWindow", "Left Click"))
        self.rightClick.setText(_translate("MainWindow", "Right Click"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopKeyboardControl.setText(_translate("MainWindow", "Stop: Ctr+Alt+Z"))
        self.addClickObjectButton.setText(_translate("MainWindow", "+"))
        self.removeAllButton.setText(_translate("MainWindow", "Remove All"))
        self.setAllButton.setText(_translate("MainWindow", "Set All"))
        self.setButton.setText(_translate("MainWindow", "Set"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.moveUp.setText(_translate("MainWindow", "Up"))
        self.moveDown.setText(_translate("MainWindow", "Down"))

    def Start(self):
        print("Started Auto Clicker")
        self.MainWindow.showMinimized()
        loop = self.numLoop.value()
        loopTime = self.loopTime.value()
        clickTime = self.clickTime.value()
        try:
            event.clear()
            hotkey = kb.HotKey(kb.HotKey.parse('<ctrl>+<alt>+z'), on_press)
            listener = kb.Listener(
                on_press=lambda k: hotkey.press(listener.canonical(k)))
            thread = Thread(target=threadClickFunction, daemon=True, args=(loop, clickTime, loopTime))
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
            self.MainWindow.showNormal()

    def getRadio(self):
        if self.leftClick.isChecked():
            return 'left'
        else:
            return 'right'


def deleteItemsOfLayout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)

            else:
                deleteItemsOfLayout(item.layout())


def on_press():
    event.set()


def threadClickFunction(loop, clickTime, loopTime):
    for i in range(0, loop):
        for clickObject in ui.ClickObjects:
            if event.is_set():
                break
            x = clickObject.itemAt(2).widget().value()
            y = clickObject.itemAt(3).widget().value()
            msController.click(x=x, y=y, button=ui.getRadio())
            for wait in range(0, int(clickTime * 100)):
                if event.is_set():
                    break
                sleep(0.01)
            if event.is_set():
                break
        if i < loop - 1:
            for wait in range(0, int(loopTime * 100)):
                if event.is_set():
                    break
                sleep(0.01)
        if event.is_set():
            break

app = QApplication(sys.argv)
screenWidth = app.primaryScreen().size().width()
screenHeight = app.primaryScreen().size().height()
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window, screenWidth, screenHeight)
window.setWindowTitle("AutoClicker")
window.show()
sys.exit(app.exec_())
