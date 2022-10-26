if __name__ == '__main__':
    from PySide2.QtCore import QCoreApplication
    QCoreApplication.setLibraryPaths(['/home/aa/바탕화면/asd/venv/lib/python3.6/site-packages/PySide2/Qt/plugins'])
# 경로를 찾는데 있어서 Visual studio Code에서 경로복사한 것과 미세하게 다른 부분이 있어서 경로 탐색에 상세해야한다.
# '/home/aa/바탕화면/asd/venv/lib/python3.6/site-packages/PySide2/Qt/plugins'
# 에서 PySide2/Qt/plugins중 Qt가 빠져있었음.
import PySide2
import PySide2.QtCore

# print("PySide2 version: ", PySide2.__version__)
# print("QtCore version: ", PySide2.QtCore.qVersion())

from PySide2.QtWidgets import QApplication, QWidget, QLabel
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(289, 170)
    # window.resize(760, 630)
    window.setWindowTitle("이것은 나의 첫 QT어플리케이션")

    label = QLabel("Hello World", window)
    label.move(110, 80)

    window.show()
    app.exec_()
    # print("끝!")
