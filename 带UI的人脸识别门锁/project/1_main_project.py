import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import pyqtSignal
from mainpage_form import Ui_Form
from my_save_model import Save_demo
from myface_recognition import Face_recognition
# from mylock import MyLock
from threading import Thread


# 注：如果不用QDialog的exec_方法，原镜头图像是可以动态一直更新的
class Demo(QWidget, Ui_Form):
    recognition_ready_signal = pyqtSignal()

    def __init__(self):
        super(Demo, self).__init__()
        self.setupUi(self)
        self.slot_init()
        self.save_button.setEnabled(False)
        self.save_ui = Save_demo()
        self.myrecognition = Face_recognition()
        # self.lock = MyLock()
        self.customphoto = ''
        self.save_photo_flag = False


        self.recognition_thread = Thread(target=self.run_face_recognition)
        self.recognition_thread.start()

    def slot_init(self):
        # 信号和槽连接
        self.recognition_ready_signal.connect(self.show_picture)
        self.save_button.clicked.connect(self.savePhoto)

    def run_face_recognition(self):
        self.myrecognition.turn_on_camera()
        self.myrecognition.get_known_face_from_dir()
        self.save_button.setEnabled(True)  # 现在可以运行点增加成员了
        while True:
            self.myrecognition.face_recognition()
            if self.save_photo_flag:
                self.photo_to_save = self.myrecognition.frame.copy()
                self.save_photo_flag = False
            self.myrecognition.add_mark()
            self.customphoto = self.myrecognition.frame
            self.recognition_ready_signal.emit()

    def show_picture(self):
        show = cv2.resize(self.customphoto, None, fx=1.3, fy=1.3, interpolation=cv2.INTER_CUBIC)
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(showImage))


    # 保存图片
    def savePhoto(self):
        self.save_photo_flag = True
        while self.save_photo_flag:
            pass
        self.save_ui.image = self.photo_to_save
        self.save_ui.show_picture()
        self.save_ui.exec_()
        self.reload_people()

    def reload_people(self):
        # 刷新存的人的资料
        self.myrecognition.get_known_face_from_dir()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())