import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import pyqtSignal,QTimer
from mainpage_form import Ui_Form
from my_save_model import Save_demo
from myface_recognition import Face_recognition
from mylock import MyLock
from threading import Thread
from delete_model import DeletePage
from login_and_signincombine import CodeBox


# 注：如果不用QDialog的exec_方法，原镜头图像是可以动态一直更新的
class Demo(QWidget, Ui_Form):
    start_timer_signal = pyqtSignal()

    def __init__(self):
        super(Demo, self).__init__()
        self.setupUi(self)

        self.save_ui = Save_demo()
        self.code_box = CodeBox()
        self.myrecognition = Face_recognition()
        self.mylock = MyLock()
        self.activation_timer = QTimer()
        self.face_recognition_timer = QTimer()

        self.slot_init()

        self.current_photo = ''
        self.stop_camera_flag = False

        self.save_button_init()
        self.unlock_button_init()
        self.delete_button_init()
        self.activation_timer_init()

        # 人脸识别模块初始化
        self.myrecognition.turn_on_camera()
        self.myrecognition.get_known_face_from_dir()

        self.face_recognition_timer_init()


    def slot_init(self):
        # 信号和槽连接
        self.save_button.clicked.connect(self.savePhoto)
        self.activation_timer.timeout.connect(self.deactivate_button)
        self.start_timer_signal.connect(self.start_timer)
        self.delete_button.clicked.connect(self.go_delete_photo)
        self.unlock_button.clicked.connect(self.unlock_the_door)
        self.code_box_button.clicked.connect(self.run_code_box)
        self.code_box.login_successfully.connect(self.login_successfully)
        self.face_recognition_timer.timeout.connect(self.run_face_recognition)

    def save_button_init(self):
        # 如果没有保存人，则保存按键可以点击，否则不能点击
        if self.myrecognition.is_dir_empty():
            self.save_button.setEnabled(True)
        else:
            self.save_button.setEnabled(False)

    def unlock_button_init(self):
        self.unlock_button.setEnabled(False)

    def delete_button_init(self):
        self.delete_button.setEnabled(False)

    def activation_timer_init(self):
        self.activation_timer.setSingleShot(True)

    def face_recognition_timer_init(self):
        self.face_recognition_timer.start(50)

    def run_face_recognition(self):
        if not self.stop_camera_flag:
            self.myrecognition.face_recognition()
            # 检测是否有识别出的任务，有则运行按键按下
            self.count = self.myrecognition.found_known_people_number()
            if self.count != 0:
                self.activate_button()
                self.start_timer_signal.emit()
            # 拷贝没有作标记的图片准被保存用
            self.photo_to_save = self.myrecognition.frame.copy()
            self.myrecognition.add_mark()
            self.show = cv2.resize(self.myrecognition.frame, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)
            self.show = cv2.cvtColor(self.show, cv2.COLOR_BGR2RGB)
            self.showImage = QImage(self.show.data, self.show.shape[1], self.show.shape[0], QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(self.showImage))

    # 保存图片
    def savePhoto(self):
        self.save_ui.image = self.photo_to_save
        self.save_ui.show_picture()
        self.save_ui.exec_()
        # 刷新已经记录的人
        self.reload_people()
        self.stop_camera_flag = False

    def reload_people(self):
        # 刷新存的人的资料
        self.myrecognition.get_known_face_from_dir()

    def start_timer(self):
        self.activation_timer.start(4000)

    def activate_button(self):
        if not self.activation_timer.isActive():
            self.save_button.setEnabled(True)
            self.delete_button.setEnabled(True)
            self.unlock_button.setEnabled(True)
            self.message.setText("认证成功")

    def deactivate_button(self):
        if self.myrecognition.is_dir_empty():
            self.save_button.setEnabled(True)
        else:
            self.save_button.setEnabled(False)
        self.delete_button.setEnabled(False)
        self.unlock_button.setEnabled(False)
        self.message.setText("欢迎^_^")

    def go_delete_photo(self):
        self.stop_camera_flag = True
        delete_page = DeletePage()
        delete_page.exec_()
        # 刷新已经记录的人
        self.reload_people()
        # 检测人是否空了，如果空了，要允许保存
        if self.myrecognition.is_dir_empty():
            self.save_button.setEnabled(True)
        self.stop_camera_flag = False

    def unlock_the_door(self):
        self.mylock.unlock()

    def run_code_box(self):
        self.code_box.exec_()

    def login_successfully(self):
        self.activate_button()
        self.start_timer_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())