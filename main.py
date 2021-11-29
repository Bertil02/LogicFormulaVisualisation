import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

from pysat.formula import CNF
from pysat.solvers import Solver

global filename
global resultTextFrame

def main():

    app = QApplication(sys.argv)
    window= QWidget()
    window.setWindowTitle("Logical Formula Visualization")

    grid = QGridLayout()

    #display buttons
    selectFileButton = QPushButton("Wybierz Plik")
    checkSatisfactionButton = QPushButton("Sprawdź spełnialność")
    visualiseButton = QPushButton("Wizualizuj formułę")
    closeButton = QPushButton('Zamknij Aplikację')

    selectFileButton.clicked.connect(setFile)
    checkSatisfactionButton.clicked.connect(evaluateFormula)
    closeButton.clicked.connect(closeApp)

    #Display result text frame
    resultTextFrame = QTextEdit("Wybierz plik DIMACS")
    resultTextFrame.setReadOnly(True)

    buttonsLayout = QVBoxLayout()
    buttonsLayout.addWidget(selectFileButton)
    buttonsLayout.addWidget(checkSatisfactionButton)
    buttonsLayout.addWidget(visualiseButton)
    buttonsLayout.addWidget(closeButton)

    grid.addLayout(buttonsLayout,0,0)
    grid.addWidget(resultTextFrame,0,1)



    window.setLayout(grid)
    window.show()
    sys.exit(app.exec_())

def evaluateFormula():
    global filename
    global resultTextFrame
    with open(filename[0],'r') as fp:
        cnf = CNF(from_fp=fp)
        print(cnf)
        s = Solver(name="minisat22")
        s.append_formula(cnf.clauses, no_return=False)
        s.solve()

        #Sprawdza czy formuła jest spełnialna
        print(s.get_status())

        #Zwraca wynik algorytmu MiniSat
        print(s.get_model())

    return s




def setFile():
    global filename
    dlg = QFileDialog()
    fname = dlg.getOpenFileName()
    filename = fname
    print(fname)
    return fname

def closeApp():
    sys.exit()

if __name__ == '__main__':
    main()