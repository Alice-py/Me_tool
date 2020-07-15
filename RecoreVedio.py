"""
@Time       ：2020-7-15
@Author     ：Honeypot
@GitHub     : Alice-py
@e-mail     ：1104389956@qq.com
@version    : 1.0   正常实现录制功能，工作问题存在的问题后续有时间会修复
@ USE       : 现版本直接启用，命名规则是时间，使用_隔开，avi格式的视频，停止需要点击图片窗口按“ESC”键
"""
import numpy as np
import cv2
from PIL import ImageGrab
import pyautogui as pyag
import time


class RecoreVedio:
    """  原理：捕抓屏幕（图），平凑成视频"""

    def vidio_object(self):
        """ 视频录制对象 """
        img_object = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')  # 图片转视频对象
        file_name = time.strftime("%H_%M_%S", time.localtime())  # 生成文件名
        vedio_object = cv2.VideoWriter('{0}.avi'.format(file_name), img_object, 30, pyag.size())  # 文件名，解码方式，帧数，全屏录制
        return vedio_object

    def get_img(self, vedio_object):
        """  图片获取与处理 """
        while (True):
            """ 循环录制（图片转视频） """
            img = ImageGrab.grab()  # 返回的颜色是GBR排序
            img_np = np.array(img)  # 使用numpy生成数组，比起"list"使用numpy.array生成的数据运算时占用的资源（内容、cpu）更少
            frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)  # 再将gbr排序的数组转换为RGB
            vedio_object.write(frame)  # 写入文件
            cv2.imshow('screen', frame)
            if cv2.waitKey(1) == 27:  # 点击ESC退出
                break

    def start(self):
        vedio_object = self.vidio_object()
        self.get_img(vedio_object)


if __name__ == '__main__':
    RecoreVedio().start()
