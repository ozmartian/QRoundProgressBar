#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#######################################################
#
# Copyright 2017 Pete Alexandrou
#
# Ported to Python from the original works in C++ by:
#
#     Sintegrial Technologies (c) 2015
#     https://sourceforge.net/projects/qroundprogressbar
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#######################################################

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QWidget

from qroundprogressbar import QRoundProgressBar
from ui_TestWidget import Ui_TestWidget


class TestWidget(QWidget, Ui_TestWidget):
    def __init__(self, parent=None):
        super(TestWidget, self).__init__(parent)
        self.setupUi(self)

        self.RoundBar1.setFormat('%v')
        self.RoundBar1.setDecimals(0)
        self.connectToSlider(self.RoundBar1)

        self.RoundBar2.setNullPosition(QRoundProgressBar.PositionRight)
        self.RoundBar2.setBarStyle(QRoundProgressBar.BarStyle.PIE)
        self.connectToSlider(self.RoundBar2)

        self.RoundBar3.setFormat('%m')
        self.RoundBar3.setBarStyle(QRoundProgressBar.BarStyle.LINE)
        self.connectToSlider(self.RoundBar3)

        p1 = QPalette()
        p1.setBrush(QPalette.AlternateBase, Qt.black)
        p1.setColor(QPalette.Text, Qt.yellow)
        self.RoundBar4.setPalette(p1)
        self.RoundBar4.setNullPosition(QRoundProgressBar.PositionLeft)
        self.RoundBar4.setDecimals(0)
        gradientPoints = [(0, Qt.green), (0.5, Qt.yellow), (1, Qt.red)]
        self.RoundBar4.setDataColors(gradientPoints)
        self.connectToSlider(self.RoundBar4)

        p2 = QPalette(p1)
        p2.setBrush(QPalette.Base, Qt.lightGray)
        p2.setColor(QPalette.Text, Qt.magenta)
        p2.setColor(QPalette.Shadow, Qt.green)
        self.RoundBar5.setPalette(p2)
        self.RoundBar5.setNullPosition(QRoundProgressBar.PositionRight)
        self.RoundBar5.setBarStyle(QRoundProgressBar.BarStyle.PIE)
        self.RoundBar5.setDataColors(gradientPoints)
        self.connectToSlider(self.RoundBar5)

        self.RoundBar6.setDecimals(2)
        self.RoundBar6.setBarStyle(QRoundProgressBar.BarStyle.LINE)
        self.RoundBar6.setOutlinePenWidth(18)
        self.RoundBar6.setDataPenWidth(10)
        self.connectToSlider(self.RoundBar6)

        self.connectToSlider(self.RoundBar7)

    def connectToSlider(self, bar: QRoundProgressBar):
        bar.setRange(self.Slider.minimum(), self.Slider.maximum())
        bar.setValue(self.Slider.value())
        self.Slider.valueChanged.connect(bar.setValue)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = TestWidget()
    widget.show()
    sys.exit(app.exec_())
