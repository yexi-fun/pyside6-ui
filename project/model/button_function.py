# button_function.py
from PySide6.QtCore import Qt, QPoint, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication


class Bindings:
    """窗口按钮和事件绑定处理类"""

    # 图标常量
    ICON_MAXIMIZE = ":/icons/images/icons/cil-clone.png"
    ICON_RESTORE = ":/icons/images/icons/cil-media-stop.png"
    ICON_SIZE = QSize(16, 16)

    def __init__(self, window):
        self.window = window
        self.window.offset = QPoint(0, 0)
        self._setup_maximize_button()

    def _setup_maximize_button(self):
        """设置最大化按钮初始状态"""
        icon = QIcon()
        icon.addFile(self.ICON_RESTORE, self.ICON_SIZE, QIcon.Mode.Normal, QIcon.State.Off)
        self.window.maximizeButton.setIcon(icon)
        self.window.maximizeButton.setIconSize(self.ICON_SIZE)

    def bind(self):
        """绑定所有按钮事件"""
        self._bind_page_buttons()
        self._bind_window_controls()

    def _bind_page_buttons(self):
        """绑定页面切换按钮"""
        page_bindings = {
            self.window.pushButton: self.window.home,
            self.window.pushButton_2: self.window.page,
            self.window.pushButton_3: self.window.page_2
        }
        for button, page in page_bindings.items():
            button.clicked.connect(lambda checked, p=page: self.change_page(p))

    def _bind_window_controls(self):
        """绑定窗口控制按钮"""
        self.window.maximizeButton.clicked.connect(self.toggle_maximize)
        self.window.minimizeButton.clicked.connect(self.window.showMinimized)
        self.window.quitButton.clicked.connect(self.window.close)

    def toggle_maximize(self):
        """切换窗口最大化状态"""
        is_maximized = self.window.isMaximized()
        icon = QIcon()

        if is_maximized:
            self.window.showNormal()
            icon.addFile(self.ICON_RESTORE, self.ICON_SIZE, QIcon.Mode.Normal, QIcon.State.Off)
        else:
            self.window.showMaximized()
            icon.addFile(self.ICON_MAXIMIZE, self.ICON_SIZE, QIcon.Mode.Normal, QIcon.State.Off)

        self.window.maximizeButton.setIcon(icon)
        self.window.maximizeButton.setIconSize(self.ICON_SIZE)

    def change_page(self, page):
        """切换页面"""
        self.window.stackedWidget.setCurrentWidget(page)

    def mousePressEvent(self, event):
        """处理鼠标按下事件"""
        if not (event.button() == Qt.LeftButton and self.window.topBar.underMouse()):
            return

        if self.window.isMaximized():
            self._handle_maximized_window_drag(event)
        else:
            self._start_window_drag(event)

    def _handle_maximized_window_drag(self, event):
        """处理最大化状态下的窗口拖动"""
        self.window.showNormal()

        # 计算新窗口位置
        screen_geo = QApplication.primaryScreen().availableGeometry()
        window_width = self.window.width()
        window_height = self.window.height()

        # 确保鼠标位置在新窗口中心
        x = event.globalPosition().x() - window_width // 2
        y = event.globalPosition().y() - self.window.offset.y()

        # 确保窗口在屏幕范围内
        x = max(0, min(x, screen_geo.width() - window_width))
        y = max(0, min(y, screen_geo.height() - window_height))

        self.window.move(int(x), int(y))
        self._start_window_drag(event)

    def _start_window_drag(self, event):
        """开始窗口拖动"""
        self.window.dragging = True
        self.window.offset = event.position().toPoint()

    def mouseMoveEvent(self, event):
        """处理鼠标移动事件"""
        if self.window.dragging:
            global_pos = event.position().toPoint() - self.window.offset
            self.window.move(self.window.mapToGlobal(global_pos))

    def mouseReleaseEvent(self, event):
        """处理鼠标释放事件"""
        if event.button() == Qt.LeftButton:
            self.window.dragging = False
