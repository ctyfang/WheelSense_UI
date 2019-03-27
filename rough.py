
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

    uiCB = UICallBacks()

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
        xAccFig = self.xAccPlot.getFigure()
        xAccFig.tight_layout(pad=0.3)
        xAccFig.set_dpi(750)
        xAccFig.set_size_inches(0.33, 0.33)
        self.xAccPlot.setObjectName(_fromUtf8("xAccPlot"))
        self.gridLayout.addWidget(self.xAccPlot, 0, 0, 1, 1)
        plotArea = xAccFig.add_subplot(111)

        plotArea.plot([0,1,2,3],[0,1,2,3])
        plotArea.plot([0, 1, 2, 3], [1, 2, 3, 4])
        xAccFig.subplots_adjust(bottom=0.15)
        self.xAccPlot.draw()


        self.zAccPlot = MatplotlibWidget.MatplotlibWidget()
        zAccFig = self.zAccPlot.getFigure()
        zAccFig.tight_layout(pad=0.1)
        zAccFig.set_dpi(750)
        zAccFig.set_size_inches(0.33,0.33)
        self.zAccPlot.draw()
        #self.zAccPlot.setObjectName(_fromUtf8("zAccPlot"))
        self.gridLayout.addWidget(self.zAccPlot, 0, 2, 1, 1)
        #self.zAccPlot.setRange(xRange=[0, 100], yRange=[0, 100])

        self.yAccPlot = MatplotlibWidget.MatplotlibWidget()
        yAccFig = self.yAccPlot.getFigure()
        yAccFig.tight_layout(pad=0.1)
        yAccFig.set_dpi(750)
        yAccFig.set_size_inches(0.33,0.33)
        self.yAccPlot.setObjectName(_fromUtf8("yAccPlot"))
        self.gridLayout.addWidget(self.yAccPlot, 0, 1, 1, 1)

        self.xGyrPlot = MatplotlibWidget.MatplotlibWidget()
        xGyrFig = self.xGyrPlot.getFigure()
        xGyrFig.set_dpi(750)
        xGyrFig.set_size_inches(0.33, 0.33)
        self.xGyrPlot.setObjectName(_fromUtf8("xGyrPlot"))
        self.gridLayout.addWidget(self.xGyrPlot, 1, 0, 1, 1)

        self.yGyrPlot = MatplotlibWidget.MatplotlibWidget()
        yGyrFig = self.yGyrPlot.getFigure()
        yGyrFig.set_dpi(750)
        yGyrFig.set_size_inches(0.33, 0.33)
        self.yGyrPlot.setObjectName(_fromUtf8("yGyrPlot"))
        self.gridLayout.addWidget(self.yGyrPlot, 1, 1, 1, 1)

        self.zGyrPlot = MatplotlibWidget.MatplotlibWidget()
        zGyrFig = self.zGyrPlot.getFigure()
        zGyrFig.set_dpi(750)
        zGyrFig.set_size_inches(0.33, 0.33)
        self.zGyrPlot.setObjectName(_fromUtf8("zGyrPlot"))
        self.gridLayout.addWidget(self.zGyrPlot, 1, 2, 1, 1)

        self.orientationPlot = MatplotlibWidget.MatplotlibWidget()
        orientationFig = self.orientationPlot.getFigure()
        orientationFig.tight_layout(pad=0.1)
        orientationFig.set_dpi(750)
        orientationFig.set_size_inches(0.33,0.33)
        self.orientationPlot.setObjectName(_fromUtf8("orientationPlot"))
        self.gridLayout.addWidget(self.orientationPlot, 2, 0, 1, 1)

        self.ultrasonicPlot = MatplotlibWidget.MatplotlibWidget()
        ultrasonicFig = self.ultrasonicPlot.getFigure()
        ultrasonicFig.tight_layout(pad=0.1)
        ultrasonicFig.set_dpi(750)
        ultrasonicFig.set_size_inches(0.33,0.33)
        self.ultrasonicPlot.setObjectName(_fromUtf8("ultrasonicPlot"))
        self.gridLayout.addWidget(self.ultrasonicPlot, 2, 1, 1, 1)

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
        self.setUpCallBacks()

    def setUpCallBacks(self):
        self.connectBtn.clicked.connect(self.uiCB.onConnectButton)

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
    c.show()
    sys.exit(app.exec_())
