import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit, QPushButton, \
    QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox,QCheckBox
import os


class DeletePage(QDialog):
    def __init__(self):
        super(DeletePage, self).__init__()
        self.setWindowTitle("选择删除")

        self.mycheckbox = {}
        self.photo_to_delete = []

        # 取得目录下的人
        self.dir = './photos_of_people'
        suffix = '.jpg'
        people_name = []
        for root, directory, files in os.walk(self.dir):  # 当前目录下的文件
            for filename in files:
                name, suf = os.path.splitext(filename)  # 文件名,文件后缀
                if suf == suffix:
                    people_name.append(filename.split(".")[0])

        # 创建选项
        for person in people_name:
            self.mycheckbox[person] = QCheckBox(person, self)

        # 确认,返回按钮
        self.confirm_button = QPushButton('删除', self)
        self.return_button = QPushButton('返回', self)

        # 横向排好按键
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.confirm_button)
        self.h_layout.addWidget(self.return_button)

        # 纵向排好
        self.v_layout = QVBoxLayout()
        for value in self.mycheckbox.values():
            self.v_layout.addWidget(value)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

        self.slot_init()


    def slot_init(self):
        self.confirm_button.clicked.connect(self.delete_fuc)
        self.return_button.clicked.connect(self.return_fuc)

    def delete_fuc(self):
        for value in self.mycheckbox.values():
            if value.checkState() != 0:
                os.remove(self.dir+"/"+value.text()+".jpg")
        QMessageBox.information(self, '^_^', '删除成功！')
        self.close()

    def return_fuc(self):
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DeletePage()
    demo.show()
    sys.exit(app.exec_())
