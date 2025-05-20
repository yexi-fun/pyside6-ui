# test2.py
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QWidget

class WindowResizer:
    """窗口大小调整器"""
    
    GRIP_SIZE = 10
    MIN_WINDOW_SIZE = 50
    
    def __init__(self, parent):
        self.parent = parent
        self.grips = self._create_grips()
        
    def _create_grips(self):
        """创建所有调整大小的手柄"""
        positions = [
            Qt.TopEdge, Qt.BottomEdge, Qt.LeftEdge, Qt.RightEdge,
            Qt.TopLeftCorner, Qt.TopRightCorner, Qt.BottomLeftCorner, Qt.BottomRightCorner
        ]
        return [CustomGrip(self.parent, position) for position in positions]

    def resizeEvent(self, event):
        """处理窗口大小改变事件"""
        for grip in self.grips:
            grip.update_geometry()
            
class CustomGrip(QWidget):
    """自定义窗口大小调整手柄"""
    
    # 光标映射
    CURSOR_MAP = {
        Qt.TopEdge: Qt.SizeVerCursor,
        Qt.BottomEdge: Qt.SizeVerCursor,
        Qt.LeftEdge: Qt.SizeHorCursor,
        Qt.RightEdge: Qt.SizeHorCursor,
        Qt.TopLeftCorner: Qt.SizeFDiagCursor,
        Qt.TopRightCorner: Qt.SizeBDiagCursor,
        Qt.BottomLeftCorner: Qt.SizeBDiagCursor,
        Qt.BottomRightCorner: Qt.SizeFDiagCursor
    }
    
    def __init__(self, parent, position):
        super().__init__(parent)
        self.parent = parent
        self.position = position
        self._setup_grip()
        
    def _setup_grip(self):
        """设置手柄的属性和事件处理"""
        self.setCursor(QCursor(self.CURSOR_MAP[self.position]))
        self._init_geometry()
        self.mouseMoveEvent = self._get_resize_function()
        
    def _init_geometry(self):
        """初始化手柄的几何形状"""
        grip_size = WindowResizer.GRIP_SIZE
        if self.position in (Qt.TopEdge, Qt.BottomEdge):
            self.setGeometry(0, 0, self.parent.width(), grip_size)
            self.setMaximumHeight(grip_size)
        elif self.position in (Qt.LeftEdge, Qt.RightEdge):
            self.setGeometry(0, grip_size, grip_size, self.parent.height() - 2 * grip_size)
            self.setMaximumWidth(grip_size)
        else:  # Corner grips
            self.setFixedSize(grip_size, grip_size)
            
    def _get_resize_function(self):
        """获取对应位置的大小调整函数"""
        resize_functions = {
            Qt.TopEdge: self._resize_top,
            Qt.BottomEdge: self._resize_bottom,
            Qt.LeftEdge: self._resize_left,
            Qt.RightEdge: self._resize_right,
            Qt.TopLeftCorner: self._resize_top_left,
            Qt.TopRightCorner: self._resize_top_right,
            Qt.BottomLeftCorner: self._resize_bottom_left,
            Qt.BottomRightCorner: self._resize_bottom_right
        }
        return resize_functions.get(self.position, lambda _: None)
        
    def _resize_top(self, event):
        """调整顶部边缘"""
        delta = event.position().toPoint()
        height = max(self.parent.minimumHeight(), self.parent.height() - delta.y())
        geo = self.parent.geometry()
        geo.setTop(geo.bottom() - height)
        self.parent.setGeometry(geo)
        self.update_geometry()
        event.accept()
        
    def _resize_bottom(self, event):
        """调整底部边缘"""
        delta = event.position().toPoint()
        height = max(self.parent.minimumHeight(), self.parent.height() + delta.y())
        self.parent.resize(self.parent.width(), height)
        self.update_geometry()
        event.accept()
        
    def _resize_left(self, event):
        """调整左侧边缘"""
        delta = event.position().toPoint()
        width = max(self.parent.minimumWidth(), self.parent.width() - delta.x())
        geo = self.parent.geometry()
        geo.setLeft(geo.right() - width)
        self.parent.setGeometry(geo)
        self.update_geometry()
        event.accept()
        
    def _resize_right(self, event):
        """调整右侧边缘"""
        delta = event.position().toPoint()
        width = max(self.parent.minimumWidth(), self.parent.width() + delta.x())
        self.parent.resize(width, self.parent.height())
        self.update_geometry()
        event.accept()
        
    def _resize_top_left(self, event):
        """调整左上角"""
        delta = event.globalPosition().toPoint() - self.parent.geometry().topLeft()
        width = max(self.parent.minimumWidth(), self.parent.width() - delta.x())
        height = max(self.parent.minimumHeight(), self.parent.height() - delta.y())
        geo = self.parent.geometry()
        geo.setTopLeft(geo.bottomRight() - QPoint(width, height))
        self.parent.setGeometry(geo)
        self.update_geometry()
        event.accept()
        
    def _resize_top_right(self, event):
        """调整右上角"""
        delta = event.globalPosition().toPoint() - self.parent.geometry().topRight()
        width = max(self.parent.minimumWidth(), self.parent.width() + delta.x())
        height = max(self.parent.minimumHeight(), self.parent.height() - delta.y())
        geo = self.parent.geometry()
        geo.setTopRight(geo.bottomLeft() + QPoint(width, -height))
        self.parent.setGeometry(geo)
        self.update_geometry()
        event.accept()
        
    def _resize_bottom_left(self, event):
        """调整左下角"""
        delta = event.globalPosition().toPoint() - self.parent.geometry().bottomLeft()
        width = max(self.parent.minimumWidth(), self.parent.width() - delta.x())
        height = max(self.parent.minimumHeight(), self.parent.height() + delta.y())
        geo = self.parent.geometry()
        geo.setBottomLeft(geo.topRight() - QPoint(width, -height))
        self.parent.setGeometry(geo)
        self.update_geometry()
        event.accept()
        
    def _resize_bottom_right(self, event):
        """调整右下角"""
        delta = event.globalPosition().toPoint() - self.parent.geometry().bottomRight()
        width = max(self.parent.minimumWidth(), self.parent.width() + delta.x())
        height = max(self.parent.minimumHeight(), self.parent.height() + delta.y())
        self.parent.resize(width, height)
        self.update_geometry()
        event.accept()
        
    def update_geometry(self):
        """更新手柄的几何形状"""
        grip_size = WindowResizer.GRIP_SIZE
        parent_width = self.parent.width()
        parent_height = self.parent.height()
        
        positions = {
            Qt.TopEdge: (0, 0, parent_width, grip_size),
            Qt.BottomEdge: (0, parent_height - grip_size, parent_width, grip_size),
            Qt.LeftEdge: (0, grip_size, grip_size, parent_height - 2 * grip_size),
            Qt.RightEdge: (parent_width - grip_size, grip_size, grip_size, parent_height - 2 * grip_size),
            Qt.TopLeftCorner: (0, 0, grip_size, grip_size),
            Qt.TopRightCorner: (parent_width - grip_size, 0, grip_size, grip_size),
            Qt.BottomLeftCorner: (0, parent_height - grip_size, grip_size, grip_size),
            Qt.BottomRightCorner: (parent_width - grip_size, parent_height - grip_size, grip_size, grip_size)
        }
        
        if position := positions.get(self.position):
            self.setGeometry(*position)