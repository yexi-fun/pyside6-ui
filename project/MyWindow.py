import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout

from .chatPage.chat_function import ChatBings
from .model.button_function import Bindings
from .model.step import Ui_MainWindow
from .model.resize_window import WindowResizer


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._init_window_properties()
        self._init_chat_area()
        self._init_components()

    def _init_window_properties(self):
        """初始化窗口属性"""
        # 初始化变量用于窗口拖动
        self.dragging = False
        self.MainWindow = self  # 将当前实例赋值给 MainWindow 属性
        # 设置窗口标志
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # 去掉系统顶栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗口背景透明

    def _init_chat_area(self):
        """初始化聊天区域"""
        self.scroll_area.setWidgetResizable(True)  # 设置滚动区域可缩放
        self.chat_layout = QVBoxLayout(self.chat_widget)  # 创建垂直布局
        self.chat_layout.setAlignment(Qt.AlignTop)  # 将聊天布局设置为顶部对齐

    def _init_components(self):
        """初始化组件"""
        self.bindings = Bindings(self)
        self.bindings.bind()
        self.chat_bings = ChatBings(self)
        self.resizer = WindowResizer(self)

        # 设置信号连接
        self.pushButton_Submit.clicked.connect(self.chat_bings.send_message)  # 直接连接到 ChatBings 的方法
        self.textEdit_input.installEventFilter(self.chat_bings)  # 安装 ChatBings 的事件过滤器

    def toggle_maximize(self):
        self.bindings.toggle_maximize()

    def change_page(self, page):
        self.bindings.change_page(page)

    def mouseMoveEvent(self, event):
        self.bindings.mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.bindings.mouseReleaseEvent(event)

    def mousePressEvent(self, event):
        self.bindings.mousePressEvent(event)

    def resizeEvent(self, event):
        # 调用 WindowResizer 的 resizeEvent 方法
        self.resizer.resizeEvent(event)
        # 调用 ChatBings 的 resizeEvent 方法
        self.chat_bings.resizeEvent()
        return super().resizeEvent(event)


if __name__ == "__main__":
    print("Please run main.py instead of this file directly.")
