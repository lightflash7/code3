import RPi.GPIO as GPIO
import time


class MyLock:
    def __init__(self):
        # 选引脚编码类型
        GPIO.setmode(GPIO.BOARD)

        # 如果RPi.GPIO检测到引脚已被配置为默认（输入）以外的其他引脚，则在尝试配置脚本时会收到警告。要禁用这些警告
        GPIO.setwarnings(False)

        # 下面是选lock的控制引脚编号
        self.lock = 11
        GPIO.setup(self.lock, GPIO.OUT, initial=GPIO.LOW)

    # 开锁
    def unlock(self):
        GPIO.output(self.lock, GPIO.HIGH)
        time.sleep(1.7)
        GPIO.output(self.lock, GPIO.LOW)
        GPIO.cleanup()


if __name__ == '__main__':
    mylock1 = MyLock()
    time.sleep(3)
    mylock1.unlock()
