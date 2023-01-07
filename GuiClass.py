from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_MainWindow(QMainWindow):
    ClickObjects = []
    ClickObjectsNum = 0

    clickMethodLocation = 2
    xLocation = 3
    yLocation = 4
    clicksLocation = 5

    def __init__(self, mainwindow, screenwidth, screenheight):
        super().__init__()
        self.MainWindow = mainwindow
        self.MainWindow.setWindowTitle("AutoClicker")
        self.screenWidth = screenwidth
        self.screenHeight = screenheight
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(802, 600)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(60, 40, 661, 491))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

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
            #Set Coordinates buttons
        self.setButtonGroup = QButtonGroup()
        self.setButtonGroup.setExclusive(True)
            #Up Buttons
        self.upButtonGroup = QButtonGroup()
        self.upButtonGroup.setExclusive(True)
        self.upButtonGroup.idClicked.connect(self.shiftUp)
            #Down Buttons
        self.downButtonGroup = QButtonGroup()
        self.downButtonGroup.setExclusive(True)
        self.downButtonGroup.idClicked.connect(self.shiftDown)

        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

            #Other Button Presses
        self.addClickObjectButton.clicked.connect(self.addClickObject)
        self.removeAllButton.clicked.connect(self.removeAllClickObject)

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

        self.clickMethod = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.clickMethod.addItems(("Left", "Right", "Middle"))
        self.clickObjectHorizontalCanvas.addWidget(self.clickMethod)

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

        self.numClicks = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.numClicks.setPrefix("Clicks:  ")
        self.numClicks.setMinimum(0)
        self.numClicks.setValue(1)
        self.numClicks.setObjectName("numClicks")
        self.clickObjectHorizontalCanvas.addWidget(self.numClicks)

        self.removeButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.removeButton.setObjectName("remove")
        self.removeButton.setText("Remove")
        self.removeButtonGroup.addButton(self.removeButton, self.ClickObjectsNum)
        self.clickObjectHorizontalCanvas.addWidget(self.removeButton)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.moveUp = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.moveUp.setArrowType(QtCore.Qt.UpArrow)
        self.moveUp.setObjectName("moveUp")
        self.upButtonGroup.addButton(self.moveUp, self.ClickObjectsNum)
        self.verticalLayout_3.addWidget(self.moveUp)
        self.moveDown = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.moveDown.setArrowType(QtCore.Qt.DownArrow)
        self.moveDown.setObjectName("moveDown")
        self.downButtonGroup.addButton(self.moveDown, self.ClickObjectsNum)
        self.verticalLayout_3.addWidget(self.moveDown)

        self.clickObjectHorizontalCanvas.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.clickObjectHorizontalCanvas)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.ClickObjects.append(self.clickObjectHorizontalCanvas)
        self.ClickObjectsNum = self.ClickObjectsNum + 1

        # TODO: create addKeyboardObject function
        # def addKeyboardObject(self):

    def removeClickObject(self, id_):
        if self.ClickObjectsNum > 0:
            print("removing click object")
            self.deleteItemsOfLayout(self.ClickObjects[id_])
            self.verticalLayout_2.removeItem(self.ClickObjects[id_])
            self.ClickObjects.pop(id_)
            self.ClickObjectsNum = self.ClickObjectsNum - 1
            for i in range(id_, self.ClickObjectsNum):
                self.removeButtonGroup.setId(self.removeButtonGroup.button(i + 1), i)
                self.setButtonGroup.setId(self.setButtonGroup.button(i + 1), i)
                self.ClickObjects[i].itemAt(0).widget().setText(str(i))

    def removeAllClickObject(self):
        print("remove all click objects")
        for clickObject in self.ClickObjects:
            self.deleteItemsOfLayout(clickObject)
            self.verticalLayout_2.removeItem(clickObject)
        self.ClickObjectsNum = 0
        self.ClickObjects.clear()

    # TODO: get shift up working by shifting entire layout
    def shiftUp(self, id_):
        if id_ > 0:
            temp = self.ClickObjects[id_]
            print(temp)
        # x = self.getXCoor(id_)
        # y = self.getYCoor(id_)
        # if id_ > 0:
        #     tempX = self.getXCoor(id_ - 1)
        #     tempY = self.getYCoor(id_ - 1)
        #     self.setXCoor(id_ - 1, x)
        #     self.setYCoor(id_ - 1, y)
        #     self.setXCoor(id_, tempX)
        #     self.setYCoor(id_, tempY)

    # TODO: get shift down working by shifting entire layout
    def shiftDown(self, id_):
        x = self.getXCoordinates(id_)
        y = self.getYCoordinates(id_)
        if id_ < self.ClickObjectsNum-1:
            tempX = self.getXCoordinates(id_ + 1)
            tempY = self.getYCoordinates(id_ + 1)
            self.setXCoordinates(id_ + 1, x)
            self.setYCoordinates(id_ + 1, y)
            self.setXCoordinates(id_, tempX)
            self.setYCoordinates(id_, tempY)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopKeyboardControl.setText(_translate("MainWindow", "Stop: Ctr+Alt+Z"))
        self.addClickObjectButton.setText(_translate("MainWindow", "+"))
        self.removeAllButton.setText(_translate("MainWindow", "Remove All"))
        self.setAllButton.setText(_translate("MainWindow", "Set All"))

    def deleteItemsOfLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

                else:
                    self.deleteItemsOfLayout(item.layout())

    def getXCoordinates(self, idnum):
        return self.ClickObjects[idnum].itemAt(self.xLocation).widget().value()

    def setXCoordinates(self, idnum, x):
        self.ClickObjects[idnum].itemAt(self.xLocation).widget().setValue(x)

    def getYCoordinates(self, idnum):
        return self.ClickObjects[idnum].itemAt(self.yLocation).widget().value()

    def setYCoordinates(self, idnum, y):
        self.ClickObjects[idnum].itemAt(self.yLocation).widget().setValue(y)

    def getNumClicks(self, idnum):
        return self.ClickObjects[idnum].itemAt(self.clicksLocation).widget().value()

    def getClickMethod(self, idnum):
        return self.ClickObjects[idnum].itemAt(self.clickMethodLocation).widget().currentText().lower()

    def setClickMethod(self, idnum, button):
        self.ClickObjects[idnum].itemAt(self.clickMethodLocation).widget().setCurrentText(button)

    def getLoop(self):
        return self.numLoop.value()

    def getLoopTime(self):
        return self.loopTime.value()

    def getClickTime(self):
        return self.clickTime.value()

    def setStartButton(self, function):
        self.startButton.clicked.connect(function)

    def setSetAllButton(self, function):
        self.setAllButton.clicked.connect(function)

    def setSetButton(self, function):
        self.setButtonGroup.idClicked.connect(function)
