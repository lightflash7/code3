import sys
from threading import Thread
from PyQt5.QtCore import QThread
from my_save_model import Save_demo


# 待解决
# 好像用Thread有问题，用QThread没有
class Save_demo_multithread(Save_demo, Thread):
    def __init__(self):
        super(Save_demo_multithread, self).__init__()
        # Save_demo.__init__(self)
        # QThread.__init__(self)

    def run(self):
        self.exec_()
