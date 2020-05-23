import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit, QPushButton, \
    QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox
from my_save_form import Save_ui_Form
import cv2
from PyQt5.QtGui import QImage, QPixmap



class Save_demo(QDialog, Save_ui_Form):
    image = ''

    def __init__(self):
        super(Save_demo, self).__init__()
        self.setupUi(self)
        self.slot_init()
        self.save_button_init()
        self.name_edit_init()


    def slot_init(self):
        # 信号和槽连接
        self.save_button.clicked.connect(self.savePhoto)
        self.return_button.clicked.connect(self.myreturn)
        self.name_editor.textChanged.connect(self.check_enter_name_func)

    def save_button_init(self):
        self.save_button.setEnabled(False)

    def name_edit_init(self):
        self.name_editor.setPlaceholderText('请于此输入您的名字')

    def check_enter_name_func(self):
        if self.name_editor.text():
            self.save_button.setEnabled(True)
        else:
            self.save_button.setEnabled(False)

    def savePhoto(self):
        try:
            filename = self.name_editor.text()
            # cv2.imwrite("photos_of_people/"+filename+".jpg", self.image)
            # windows有GBK的问题
            cv2.imencode('.jpg', self.image)[1].tofile("photos_of_people/"+filename+'.jpg')
            QMessageBox.information(self, '^_^', '保存成功！')
            self.name_editor.clear()
            self.close()
        except:
            QMessageBox.critical(self, '@_@', '抱歉，保存失败，清稍后再试')

    def myreturn(self):
        self.name_editor.clear()
        self.close()


    def show_picture(self):
        show = cv2.resize(self.image, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(showImage))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Save_demo()
    demo.show()
    sys.exit(app.exec_())
