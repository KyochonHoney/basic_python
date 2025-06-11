#notepad 만들기
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QTextCursor
from PyQt5 import QtCore
# https://www.youtube.com/watch?v=N3soDgqvb28&list=PLnIaYcDMsScwsKo1rQ18cLHvBdjou-kb5&index=12
form_class = uic.loadUiType("C:\\Users\\tideflo\\Desktop\\신은서\\python\\basic_python\\pyqt\\day03.ui")[0]

class findWindow(QDialog):
    def __init__(self, parent):
        super(findWindow, self).__init__(parent)
        uic.loadUi("C:\\Users\\tideflo\\Desktop\\신은서\\python\\basic_python\\pyqt\\findStr.ui", self)
        self.show()

        self.parent = parent
        self.pe = parent.plainTextEdit
        self.cursor = self.pe.textCursor()

        self.up_down = "down"
        self.radioButton_up.clicked.connect(self.updown_radio_button)
        self.radioButton_down.clicked.connect(self.updown_radio_button)
        self.pushButton_findNext.clicked.connect(self.findNext)
        self.pushButton_cancel.clicked.connect(self.close)

    def updown_radio_button(self):
        if self.radioButton_up.isChecked():
            self.up_down = "up"
        elif self.radioButton_down.isChecked():
            self.up_down = "down"

    def setCursor(self, start, end):
        self.cursor.setPosition(start) # 앞에 커서를 찍고
        self.cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, end-start) # 뒤로 커서를 움직인다.
        self.pe.setTextCursor(self.cursor)
        self.pe.ensureCursorVisible()

    def findNext(self):
        self.cursor = self.pe.textCursor()
        pattern = self.lineEdit.text()
        text = self.pe.toPlainText()
        reg = QtCore.QRegExp(pattern)

        if self.checkBox_CaseSensitive.isChecked():
            cs = QtCore.Qt.CaseSensitive
        else:
            cs = QtCore.Qt.CaseInsensitive  

        reg.setCaseSensitivity(cs)
        pos = self.cursor.position() # 현재 커서 위치
        if self.up_down == "down":
            index = reg.indexIn(text, pos)
        elif self.up_down == "up":
            pos -= len(pattern) + 1
            index = reg.lastIndexIn(text, pos)

        if index == -1:
            QMessageBox.information(self, "찾기", "찾는 문자열이 없습니다.")
            return
        elif index != -1:
            self.setCursor(index, len(pattern) + index)

    def keyReleaseEvent(self, event):
        data = self.lineEdit.text()
        self.pushButton_findNext.setEnabled(not (data == ""))

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

    # 내용이 변경되었는지
    def is_changed(self):
        data1 = self.plainTextEdit.toPlainText()
        if not self.opened:
            if data1.strip():
                return False
            return True
        with open(self.opened_file_path, encoding='utf-8') as f:
            data2 = f.read()
        return data1 == data2

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
        if self.is_changed():
            event.accept()
            return
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
