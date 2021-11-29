import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QGridLayout, QPushButton, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

from pysat.formula import CNF
from pysat.solvers import Solver

global filename

def main():
    global resultTextFrame

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
    QTextEdit{
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
    window= QWidget()
    window.setFixedSize(1280,720)
    window.setWindowTitle("Logical Formula Visualization")

    grid = QGridLayout()

    #display buttons
    selectFileButton = QPushButton("Wybierz Plik")
    selectFileButton.setFixedSize(300,170)
    checkSatisfactionButton = QPushButton("Sprawdź spełnialność")
    checkSatisfactionButton.setFixedSize(300,170)
    visualiseButton = QPushButton("Wizualizuj formułę")
    visualiseButton.setFixedSize(300,170)
    closeButton = QPushButton('Zamknij Aplikację')
    closeButton.setFixedSize(300,170)

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

        if s.get_status():
            resultTextFrame.setText("Formuła jest spełnialna!\n\n")
        else:
            resultTextFrame.setText("Formuła nie jest spełnialna!\n\n")

        resultTextFrame.append("Wynik algorytmu minsat:")
        result =s.get_model()

        resultTextFrame.append(str(result))


    return s




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