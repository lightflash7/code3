import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from myform import Ui_Form



class Demo(QWidget, Ui_Form):
    def __init__(self):
        super(Demo, self).__init__()
        self.setupUi(self)
        self.timer_camera = QTimer() #初始化定时器
        self.cap = cv2.VideoCapture() #初始化摄像头
        self.CAM_NUM = 0
        self.slot_init()
        self.save_photo_flag = False


    def slot_init(self):
        self.timer_camera.timeout.connect(self.show_camera)
        # 信号和槽连接
        self.enable_camera_button.clicked.connect(self.slotCameraButton)
        self.save_button.clicked.connect(self.savePhoto)

    # 在Label显示图片的核心方法
    def show_camera(self):
        flag, self.image = self.cap.read()
        if self.save_photo_flag:
            cv2.imwrite("myphoto.jpg", self.image)
            QMessageBox.information(self, ' ', '图片保存成功!')
            self.save_photo_flag = False
        show = cv2.resize(self.image, None, fx=1.3, fy=1.3, interpolation=cv2.INTER_CUBIC)
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(showImage))

    # 打开关闭摄像头控制
    def slotCameraButton(self):
        if self.timer_camera.isActive() == False:
            # 打开摄像头并显示图像信息
            self.openCamera()
        else:
            # 关闭摄像头并清空显示信息
            self.closeCamera()

    # 打开摄像头
    def openCamera(self):
        flag = self.cap.open(self.CAM_NUM)
        if flag == False:
            msg = QMessageBox.Warning(self, u'Warning', u'请检测相机与电脑是否连接正确',
                                      buttons=QMessageBox.Ok,
                                      defaultButton=QMessageBox.Ok)
        else:
            self.timer_camera.start(30) # 30ms调用一次show_camera
            self.enable_camera_button.setText('关闭摄像头')

    # 关闭摄像头
    def closeCamera(self):
        self.timer_camera.stop()
        self.cap.release()
        self.label.clear()
        self.enable_camera_button.setText('打开摄像头')

    # 保存图片
    def savePhoto(self):
        self.save_photo_flag = True







if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())