
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rough.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import matplotlib
import pyqtgraph
from pyqtgraph.widgets import MatplotlibWidget
from uiCallBacks import UICallBacks
from remotePAWDataAcquisition import *


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_c(object):

    #uiCB = UICallBacks()

    def updateGraphData(self, plotHandle, lineHandle, newXData, newYData):
        lineHandle.set_xdata(newXData)
        lineHandle.set_ydata(newYData)
        plotHandle.draw()

    def setupUi(self, c):
        c.setObjectName(_fromUtf8("c"))
        c.resize(925, 780)
        self.widget = QtGui.QWidget(c)
        self.widget.setGeometry(QtCore.QRect(10, 10, 760, 760))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout.setContentsMargins(0,0,0,0)
        self.gridLayout.setSpacing(0)

        self.xAccPlot = MatplotlibWidget.MatplotlibWidget()
        self.xAccFig = self.xAccPlot.getFigure()
        self.xAccFig.tight_layout(pad=0.3)
        self.xAccFig.set_dpi(750)
        self.xAccFig.set_size_inches(0.33, 0.33)
        self.xAccPlot.setObjectName(_fromUtf8("xAccPlot"))
        self.gridLayout.addWidget(self.xAccPlot, 0, 0, 1, 1)

        self.xAccPlotArea = self.xAccFig.add_subplot(111)
        self.xAccLines = {}
        self.xAccLines['leftWheel'],  = self.xAccPlotArea.plot([0,1,2,3],[0,1,2,3])
        #self.xAccLines['rightWheel'], = self.xAccPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        #self.xAccLines['frame'], = self.xAccPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])

        self.xAccPlot.draw()
        self.xAccFig.subplots_adjust(bottom=0.15)
        self.updateGraphData(self.xAccPlot, self.xAccLines['leftWheel'], [0, 1, 2, 3],[1, 2, 3, 4])

        self.yAccPlot = MatplotlibWidget.MatplotlibWidget()
        self.yAccFig = self.yAccPlot.getFigure()
        self.yAccFig.tight_layout(pad=0.1)
        self.yAccFig.set_dpi(750)
        self.yAccFig.set_size_inches(0.33,0.33)
        self.yAccPlot.setObjectName(_fromUtf8("yAccPlot"))
        self.gridLayout.addWidget(self.yAccPlot, 0, 1, 1, 1)
        self.yAccPlotArea = self.yAccFig.add_subplot(111)
        self.yAccLines = {}
        self.yAccLines['leftWheel'], = self.yAccPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        #self.yAccLines['rightWheel'], = self.yAccPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        #self.yAccLines['frame'], = self.yAccPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        self.yAccPlot.draw()
        self.yAccFig.subplots_adjust(bottom=0.15)
        self.updateGraphData(self.yAccPlot, self.yAccLines['leftWheel'], [0, 1, 2, 3], [1, 2, 3, 4])

        self.zAccPlot = MatplotlibWidget.MatplotlibWidget()
        self.zAccFig = self.zAccPlot.getFigure()
        self.zAccFig.tight_layout(pad=0.1)
        self.zAccFig.set_dpi(750)
        self.zAccFig.set_size_inches(0.33,0.33)
        self.zAccPlot.draw()
        self.zAccPlot.setObjectName(_fromUtf8("zAccPlot"))
        self.gridLayout.addWidget(self.zAccPlot, 0, 2, 1, 1)
        self.zAccPlotArea = self.zAccFig.add_subplot(111)
        self.zAccLines = {}
        self.zAccLines['leftWheel'], = self.zAccPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        #self.zAccLines['rightWheel'], = self.zAccPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        #self.zAccLines['frame'], = self.zAccPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        self.zAccPlot.draw()
        self.zAccFig.subplots_adjust(bottom=0.15)
        self.updateGraphData(self.zAccPlot, self.zAccLines['leftWheel'], [0, 1, 2, 3], [1, 2, 3, 4])

        self.xGyrPlot = MatplotlibWidget.MatplotlibWidget()
        self.xGyrFig = self.xGyrPlot.getFigure()
        self.xGyrFig.set_dpi(750)
        self.xGyrFig.set_size_inches(0.33, 0.33)
        self.xGyrPlot.setObjectName(_fromUtf8("xGyrPlot"))
        self.gridLayout.addWidget(self.xGyrPlot, 1, 0, 1, 1)
        self.xGyrPlotArea = self.xGyrFig.add_subplot(111)
        self.xGyrLines = {}
        self.xGyrLines['leftWheel'], = self.xGyrPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        # self.xGyrLines['rightWheel'], = self.xGyrPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        # self.xGyrLines['frame'], = self.xGyrPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        self.xGyrPlot.draw()
        self.xGyrFig.subplots_adjust(bottom=0.15)
        self.updateGraphData(self.xGyrPlot, self.xGyrLines['leftWheel'], [0, 1, 2, 3], [1, 2, 3, 4])

        self.yGyrPlot = MatplotlibWidget.MatplotlibWidget()
        self.yGyrFig = self.yGyrPlot.getFigure()
        self.yGyrFig.set_dpi(750)
        self.yGyrFig.set_size_inches(0.33, 0.33)
        self.yGyrPlot.setObjectName(_fromUtf8("yGyrPlot"))
        self.gridLayout.addWidget(self.yGyrPlot, 1, 1, 1, 1)
        self.yGyrPlotArea = self.yGyrFig.add_subplot(111)
        self.yGyrLines = {}
        self.yGyrLines['leftWheel'], = self.yGyrPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        # self.yGyrLines['rightWheel'], = self.yGyrPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        # self.yGyrLines['frame'], = self.yGyrPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        self.yGyrPlot.draw()
        self.yGyrFig.subplots_adjust(bottom=0.15)
        self.updateGraphData(self.yGyrPlot, self.yGyrLines['leftWheel'], [0, 1, 2, 3], [1, 2, 3, 4])

        self.zGyrPlot = MatplotlibWidget.MatplotlibWidget()
        self.zGyrFig = self.zGyrPlot.getFigure()
        self.zGyrFig.set_dpi(750)
        self.zGyrFig.set_size_inches(0.33, 0.33)
        self.zGyrPlot.setObjectName(_fromUtf8("zGyrPlot"))
        self.gridLayout.addWidget(self.zGyrPlot, 1, 2, 1, 1)
        self.zGyrPlotArea = self.zGyrFig.add_subplot(111)
        self.zGyrLines = {}
        self.zGyrLines['leftWheel'], = self.zGyrPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        # self.zGyrLines['rightWheel'], = self.zGyrPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        # self.zGyrLines['frame'], = self.zGyrPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        self.zGyrPlot.draw()
        self.zGyrFig.subplots_adjust(bottom=0.15)
        self.updateGraphData(self.zGyrPlot, self.zGyrLines['leftWheel'], [0, 1, 2, 3], [1, 2, 3, 4])

        self.orientationPlot = MatplotlibWidget.MatplotlibWidget()
        self.orientationFig = self.orientationPlot.getFigure()
        self.orientationFig.tight_layout(pad=0.1)
        self.orientationFig.set_dpi(750)
        self.orientationFig.set_size_inches(0.33,0.33)
        self.orientationPlot.setObjectName(_fromUtf8("orientationPlot"))
        self.gridLayout.addWidget(self.orientationPlot, 2, 0, 1, 1)
        self.orientationPlotArea = self.orientationFig.add_subplot(111)
        self.orientationLines = {}
        self.orientationLines['pitch'], = self.orientationPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        # self.orientationLines['roll'], = self.orientationPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        # self.orientationLines['yaw'], = self.orientationPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        self.orientationPlot.draw()
        self.orientationFig.subplots_adjust(bottom=0.15)
        self.updateGraphData(self.orientationPlot, self.orientationLines['pitch'], [0, 1, 2, 3], [1, 2, 3, 4])

        self.ultrasonicPlot = MatplotlibWidget.MatplotlibWidget()
        self.ultrasonicFig = self.ultrasonicPlot.getFigure()
        self.ultrasonicFig.tight_layout(pad=0.1)
        self.ultrasonicFig.set_dpi(750)
        self.ultrasonicFig.set_size_inches(0.33,0.33)
        self.ultrasonicPlot.setObjectName(_fromUtf8("ultrasonicPlot"))
        self.gridLayout.addWidget(self.ultrasonicPlot, 2, 1, 1, 1)
        self.ultrasonicPlotArea = self.ultrasonicFig.add_subplot(111)
        self.ultrasonicLines = {}
        self.ultrasonicLines['front'], = self.ultrasonicPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        # self.ultrasonicLines['down'], = self.ultrasonicPlotArea.plot([0, 1, 2, 3], [0, 1, 2, 3])
        self.ultrasonicPlot.draw()
        self.ultrasonicFig.subplots_adjust(bottom=0.15)
        self.updateGraphData(self.ultrasonicPlot, self.ultrasonicLines['front'], [0, 1, 2, 3], [1, 2, 3, 4])

        self.cameraPlot = MatplotlibWidget.MatplotlibWidget()
        cameraFig = self.cameraPlot.getFigure()
        cameraFig.tight_layout(pad=0.1)
        cameraFig.set_dpi(750)
        cameraFig.set_size_inches(0.33,0.33)
        self.cameraPlot.setObjectName(_fromUtf8("cameraPlot"))
        self.gridLayout.addWidget(self.cameraPlot, 2, 2, 1, 1)

        self.widget1 = QtGui.QWidget(c)
        self.widget1.setGeometry(QtCore.QRect(770, 10, 133, 192))
        self.widget1.setObjectName(_fromUtf8("widget1"))

        self.verticalLayout = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.connectBtn = QtGui.QPushButton(self.widget1)
        self.connectBtn.setObjectName(_fromUtf8("connectBtn"))
        self.verticalLayout.addWidget(self.connectBtn)

        self.startBtn = QtGui.QPushButton(self.widget1)
        self.startBtn.setObjectName(_fromUtf8("startBtn"))
        self.verticalLayout.addWidget(self.startBtn)

        self.saveBtn = QtGui.QPushButton(self.widget1)
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        self.verticalLayout.addWidget(self.saveBtn)

        self.resetBtn = QtGui.QPushButton(self.widget1)
        self.resetBtn.setObjectName(_fromUtf8("resetBtn"))
        self.verticalLayout.addWidget(self.resetBtn)

        self.retranslateUi(c)
        QtCore.QMetaObject.connectSlotsByName(c)

        #Sets up button callbacks 
        #self.setUpCallBacks()

    def rightHC05PlotXAxis(self,x,y):
        # self.xAxisPlotArea.plot(x,y)
        self.xAxisPlotArea.plot(y, 'r-')

        self.xAccPlot.draw()


    # def leftHC05PlotYAxis(self, x, y):
    #     self.yAccPlot.plot()



    def setUpCallBacks(self):
        #Connect to the server.
        # self.connectBtn.clicked.connect(self.uiCB.onConnectButton)
        pass


    def retranslateUi(self, c):
        c.setWindowTitle(_translate("c", "WheelSense Data Collection", None))
        self.connectBtn.setText(_translate("c", "Connect", None))
        self.startBtn.setText(_translate("c", "Start/Stop", None))
        self.saveBtn.setText(_translate("c", "Save Data", None))
        self.resetBtn.setText(_translate("c", "Clear", None))




if __name__ == "__main__":



    import sys
    app = QtGui.QApplication(sys.argv)
    c = QtGui.QDialog()
    ui = Ui_c()
    ui.setupUi(c)

    
    # for i in range(4):
    #     print(i)
    #     ui.plotXAxis(i, i)

    # ui.plotXAxis([0,1,2,3],[0,1,2,4.5])
    c.show()
    _mainDataAcquisition = remotePAWDataAcquisition(ui)
    _mainDataAcquisition.start()
    sys.exit(app.exec_())
