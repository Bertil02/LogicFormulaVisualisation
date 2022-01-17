import sys

from PyQt5.QtGui import QPixmap

import graph1
import graph2

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QGridLayout, QPushButton, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

global filename


def main():
    global resultTextFrame
    global picture

    style = """
    QWidget{
        background:  #DEDEDE;
    }
    QPushButton{
        box-shadow:inset 0px 1px 0px 0px #ffffff;
	    background-color:#ffffff;
	    border-radius:6px;
	    border:1px solid #dcdcdc;
	    display:inline-block;
	    cursor:pointer;
	    color:#666666;
	    font-family:Arial;
	    font-size:15px;
	    font-weight:bold;
	    padding:6px 24px;
	    text-decoration:none;
	    text-shadow:0px 1px 0px #ffffff;
    }
    QLabel{
        box-shadow:inset 0px 1px 0px 0px #ffffff;
	    background-color:#ffffff;
	    border-radius:6px;
	    border:1px solid #dcdcdc;
	    display:inline-block;
	    cursor:pointer;
	    color:#666666;
	    font-family:Arial;
	    font-size:22px;
	    font-weight:bold;
	    padding:24px 24px;
	    text-decoration:none;
	    text-shadow:0px 1px 0px #ffffff;
    }
    """

    app = QApplication(sys.argv)
    app.setStyleSheet(style)
    window = QWidget()

    window.setGeometry(0, 0, 1280, 720)
    window.setWindowTitle("Logical Formula Visualization")
    grid = QGridLayout()

    graph1VisualizeButton = QPushButton("Wizualizacja nr 1")
    graph1VisualizeButton.setFixedSize(300, 70)
    graph1VisualizeButton.clicked.connect(setFile)
    graph1VisualizeButton.clicked.connect(visualizeGraph1)

    graph2VisualizeButton = QPushButton("Wizualizacja nr 2")
    graph2VisualizeButton.setFixedSize(300, 70)
    graph2VisualizeButton.clicked.connect(setFile)
    # graph2VisualizeButton.clicked.connect(visualizeGraph2)

    visualizeHistogramButton = QPushButton("Wizualizacja histogram")
    visualizeHistogramButton.setFixedSize(300, 70)
    visualizeHistogramButton.clicked.connect(setFile)
    # visualiseButton.clicked.connect(visualizeHistogram)

    closeButton = QPushButton('Zamknij Aplikację')
    closeButton.setFixedSize(300, 170)
    closeButton.clicked.connect(closeApp)

    # Display result text frame
    resultTextFrame = QTextEdit("Wybierz plik DIMACS")
    resultTextFrame.setReadOnly(True)

    # Picture widget
    picture = QLabel()
    picture.setFixedSize(950, 695)
    picture.setScaledContents(True)

    buttonsLayout = QVBoxLayout()
    buttonsLayout.addWidget(graph1VisualizeButton)
    buttonsLayout.addWidget(graph2VisualizeButton)
    buttonsLayout.addWidget(visualizeHistogramButton)
    buttonsLayout.addWidget(closeButton)

    grid.addLayout(buttonsLayout, 0, 0)
    grid.addWidget(picture, 0, 1)

    window.setLayout(grid)
    window.show()
    sys.exit(app.exec_())


def visualizeCNFFile():
    global filename
    global picture
    graph1.draw(filename[0])
    picture.setPixmap(QPixmap("result/random_rough.png"))


def visualizeGraph1():
    global filename
    global picture
    graph1.draw(filename[0])
    picture.setPixmap(QPixmap("result/random_rough.png"))


def visualizeGraph2():
    global filename
    global picture
    graph2.draw(filename[0])
    picture.setPixmap(QPixmap("result/random_rough.png"))


def setFile():
    global filename
    global resultTextFrame
    dlg = QFileDialog()
    fname = dlg.getOpenFileName()
    filename = fname
    print(fname)
    resultTextFrame.clear()
    return fname


def closeApp():
    sys.exit()


if __name__ == '__main__':
    main()
