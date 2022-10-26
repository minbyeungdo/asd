if __name__ == '__main__':
    from PySide2.QtCore import QCoreApplication
    QCoreApplication.setLibraryPaths(['/home/aa/바탕화면/asd/venv/lib/python3.6/site-packages/PySide2/Qt/plugins'])
# 경로를 찾는데 있어서 Visual studio Code에서 경로복사한 것과 미세하게 다른 부분이 있어서 경로 탐색에 상세해야한다.
# '/home/aa/바탕화면/asd/venv/lib/python3.6/site-packages/PySide2/Qt/plugins'
# 에서 PySide2/Qt/plugins중 Qt가 빠져있었음.
import PySide2
import PySide2.QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon

# print("PySide2 version: ", PySide2.__version__)
# print("QtCore version: ", PySide2.QtCore.qVersion())

from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    logon = QWidget()

    labelId = QLabel('&Id : ')
    labelId.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
    labelPW = QLabel("&Password:")

    lineEditId = QLineEdit()
    lineEditPW = QLineEdit()
    lineEditPW.setEchoMode(QLineEdit.Password)

    labelId.setBuddy(lineEditId)
    labelPW.setBuddy(lineEditPW)

    #       Id : [lineEditId]
    # Password : [lineEditPW]

    buttonOk = QPushButton("&Ok")
    # buttonOk.setIcon(QIcon(":/ok.png"))
    # buttonOk.setText("Ok")

    layout1 = QGridLayout()
    layout1.addWidget(labelId,0,0)
    layout1.addWidget(lineEditId,0,1)
    layout1.addWidget(labelPW,1,0)
    layout1.addWidget(lineEditPW,1,1)
    
    # |0,0|0,1|
    # |1,0|1,1|
    # |2,0|2,1|

    layout2 = QHBoxLayout()
    layout2.addStretch()
    layout2.addWidget(buttonOk)

    # | 0 | 1 | 2 |

    mainLayout = QVBoxLayout()
    mainLayout.addLayout(layout1)
    mainLayout.addLayout(layout2)

    # | 0 |
    # | 1 |
    # | 2 |

    logon.setLayout(mainLayout)
    logon.setWindowTitle('Log on')
    # window.setWindowIcon(QIcon(":/images/ok.png"))

    buttonOk.clicked.connect(app.quit)

    logon.show()
    app.exec_()
    # print("끝!")
