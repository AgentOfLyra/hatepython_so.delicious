import win32gui
import win32con
import win32api
import time
from ctypes import *

class EventsImitater():
    def mouse_leftclick(self):#单击
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        # 在当前位置按下鼠标左键
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        # 在当前位置松开鼠标左键
    def mouse_rightclick(self):#右键
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
    def double_click(self):#双击
        i = 0
        while i <= 1:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            i += 1
            time.sleep(0.05)
    def wheel_down(self):#下拉
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 1)
    def wheel_up(self):#上滚
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 1)
    def read_mouseposition(self):
        i = c_int(3)
        pi = pointer(i)
        win32api.MessageBox(0,str(pi[0])+"秒后读取鼠标位置！", "注意！", win32con.MB_ICONASTERISK)
        for n in range(3, 0, -1):
            pi[0] -= 1
            print(pi[0])
            time.sleep(1)
        pos = win32api.GetCursorPos()
        win32api.MessageBox(0, str(pos[0])+","+str(pos[1]), "鼠标位置", win32con.MB_OK)
        return pos
    def move_mouse(self,new_x ,new_y):
        if new_y is not None and new_x is not None:
            point = (new_x, new_y)
            win32api.SetCursorPos(point)
            self.x = new_x
            self.y = new_y
    def key_input(self,input_words):
        for word in input_words:
            win32api.keybd_event(VK_CODE[word], 0, 0, 0)
            win32api.keybd_event(VK_CODE[word], 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.05)
    def key_event(self,input_key):
        win32api.keybd_event(VK_CODE[word], 0, 0, 0)
        win32api.keybd_event(VK_CODE[word], 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)
# testcode
# test = EventsImitater()
# pos = test.read_mouseposition()
# i = 10
# while i:
#     test.move_mouse(pos[0],pos[1])
#     i -= 1
#     time.sleep(1)

