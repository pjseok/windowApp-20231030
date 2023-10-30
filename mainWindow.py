import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyWin(QWidget): # Qwidget 클래스를 상속받는 자식클래스를 선언
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("파이썬계산기")
        self.setWindowIcon(QIcon("google.png"))
        self.move(300, 300) # 윈도우창이 시작되는 위치 x, y
        self.resize(400, 400) # 윈도우의 크기
        self.show() # 윈도우창을 스크린에 보여줌

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWin()
    sys.exit(app.exec_())

