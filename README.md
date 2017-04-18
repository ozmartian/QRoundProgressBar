This is a port of QRoundProgressBar (https://sourceforge.net/projects/qroundprogressbar) to Python 3 PyQt5.

#### A Simple Example

Install via PyPi:

```
sudo pip install qroundprogressbar
```

Install via Git clone:

```
git clone git@github.com:ozmartian/QRoundProgressBar.git
cd QRoundProgressBar
sudo pip install .
```

Now you can use the module:  
*(e.g. copy/paste this snippet of code into a demo.py file and run with 'python3 demo.py')*

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QPalette
from PyQt5.QtWidgets import QApplication, qApp

from qroundprogressbar import QRoundProgressBar


app = QApplication(sys.argv)

progress = QRoundProgressBar()
progress.setBarStyle(QRoundProgressBar.BarStyle.DONUT)

# style accordingly via palette
palette = QPalette()
brush = QBrush(QColor(0, 0, 255))
brush.setStyle(Qt.SolidPattern)
palette.setBrush(QPalette.Active, QPalette.Highlight, brush)

progress.setPalette(palette)
progress.show()

# simulate delayed time that a process may take to execute
# from demonstration purposes only
for i in range(0, 100, 20):
    progress.setValue(i)
    qApp.processEvents()
    time.sleep(3)

sys.exit(app.exec_())
```

#### A More Thorough Demo

Run TestWidget.py to see a more detailed example of the module at work.

![Demo](https://a.fsdn.com/con/app/proj/qroundprogressbar/screenshots/RoundBars.png/1)

I've also included the original C++ project's documentation in the docs folder which you should easily be
able to follow and apply to PyQt5 as per usual.
