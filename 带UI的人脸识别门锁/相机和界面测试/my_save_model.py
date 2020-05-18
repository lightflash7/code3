import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit, QPushButton, \
    QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox
from my_save_form import Save_ui_Form



class Save_demo(QDialog, Save_ui_Form):
    def __init__(self):
        super(Save_demo, self).__init__()
        self.setupUi(self)
        self.slot_init()


    def slot_init(self):
        # 信号和槽连接
        self.save_button.clicked.connect(self.savePhoto)
        self.return_button.clicked.connect(self.myreturn)

    def savePhoto(self):
        try:
            QMessageBox.information(self, '^_^', '保存成功！')
        except:
            QMessageBox.critical(self, '@_@', '抱歉，保存失败，清稍后再试')

    def myreturn(self):
        self.close()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Save_demo()
    demo.show()
    sys.exit(app.exec_())
