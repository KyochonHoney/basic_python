#notepad 만들기
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
# https://www.youtube.com/watch?v=N3soDgqvb28&list=PLnIaYcDMsScwsKo1rQ18cLHvBdjou-kb5&index=12
form_class = uic.loadUiType("C:\Users\tideflo\Desktop\신은서\python\basic_python\pyqt\day03.ui")[0]

class findWindow(QDialog):
    def __init__(self, parent):
        super(findWindow, self).__init__(parent)
        uic.loadUi("C:\Users\tideflo\Desktop\신은서\python\basic_python\pyqt\findStr.ui", self)
        self.show()

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_open.triggered.connect(self.openFunction)
        self.action_save.triggered.connect(self.saveFunction)
        self.action_save_as.triggered.connect(self.saveAsFunction)
        self.action_close.triggered.connect(self.closeEvent)

        self.action_undo.triggered.connect(self.undoFunction)
        self.action_cut.triggered.connect(self.cutFunction)
        self.action_copy.triggered.connect(self.copyFunction)
        self.action_paste.triggered.connect(self.pasteFunction)

        self.action_find.triggered.connect(self.findFunction)

        self.opened = False
        self.opened_file_path = ""

    def findFunction(self):
        self.findWindow = findWindow(self)
        self.findWindow.show()

    def undoFunction(self):
        self.plainTextEdit.undo()

    def cutFunction(self):
        self.plainTextEdit.cut()

    def copyFunction(self):
        self.plainTextEdit.copy()

    def pasteFunction(self):
        self.plainTextEdit.paste()

    #닫혔을 때 함수 호출
    def save_changed_data(self):
        msgBox = QMessageBox()
        msgBox.setText("변경 내용을 {}에 저장하시겠습니까?".format(self.opened_file_path))
        msgBox.addButton('저장', QMessageBox.YesRole) # 0
        msgBox.addButton('저장안함', QMessageBox.NoRole) # 1
        msgBox.addButton('취소', QMessageBox.RejectRole) # 2
        answer = msgBox.exec_()
        return answer

    #끝내기, 종료이벤트
    def closeEvent(self, event):
        result = self.save_changed_data()
        if result == 0:
            if self.opened:
                self.save_file(self.opened_file_path)
            else:
                self.saveAsFunction()
        elif result == 1:
            event.accept()
        else:
            event.ignore()

    # 파일 저장
    def save_file(self, fname):
        data = self.plainTextEdit.toPlainText()

        with open(fname, 'w', encoding='utf-8') as f:
            f.write(data)
        self.opened = True
        self.opened_file_path = fname    

    # 파일 열기
    def open_file(self, fname):
        
        with open(fname, encoding='utf-8') as f:
            data = f.read()
        
        self.plainTextEdit.setPlainText(data)
        self.opened = True
        self.opened_file_path = fname    

    def openFunction(self):
        fname = QFileDialog.getOpenFileName(self)[0]
        if fname:
            self.open_file(fname)

    def saveFunction(self):
        if self.opened:
            self.save_file(self.opened_file_path)
        else:
            self.saveAsFunction()

    def saveAsFunction(self):
        fname = QFileDialog.getSaveFileName(self)[0]
        if fname:
            self.save_file(fname[0])

app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()
