from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QTextEdit
from project.utils import load_and_scale_image, format_markdown_html
from project.config import CHAT_STYLES


class MessageWidget(QWidget):
    """基础消息组件"""

    def __init__(self, text, msg_type="user", parent=None):
        super().__init__(parent)
        self.msg_type = msg_type
        self.text = text
        self._setup_ui()

    def _setup_ui(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # 创建头像
        self.avatar = self._create_avatar()
        # 创建文本框
        self.text_edit = self._create_text_edit()
        # 创建占位组件
        self.spacer = QWidget()

        # 根据消息类型布局组件
        if self.msg_type == "user":
            self.layout.addWidget(self.spacer, alignment=Qt.AlignTop)
            self.layout.addWidget(self.text_edit, alignment=Qt.AlignTop)
            self.layout.addWidget(self.avatar, alignment=Qt.AlignTop)
        else:
            self.layout.addWidget(self.avatar, alignment=Qt.AlignTop)
            self.layout.addWidget(self.text_edit, alignment=Qt.AlignTop)
            self.layout.addWidget(self.spacer, alignment=Qt.AlignTop)

    def _create_avatar(self):
        avatar = QLabel()
        avatar.setFixedSize(40, 40)

        # 根据消息类型加载不同头像
        image_path = "images/images/user.jpg" if self.msg_type == "user" else "images/images/ai-pic.jpg"
        pixmap = load_and_scale_image(image_path, 40, 40)
        avatar.setPixmap(pixmap)
        return avatar

    def _create_text_edit(self):
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 设置样式
        style = CHAT_STYLES["USER_MSG_STYLE" if self.msg_type == "user" else "REPLY_MSG_STYLE"]
        text_edit.setStyleSheet(style)
        text_edit.setViewportMargins(0, 2, 0, 0)

        # 设置HTML内容
        text_edit.setHtml(format_markdown_html(self.text))
        return text_edit

    def update_text(self, text):
        """更新消息内容"""
        self.text = text
        self.text_edit.setHtml(format_markdown_html(text))

    def set_size(self, width=None, height=None):
        """设置消息组件大小"""
        if width:
            self.text_edit.setMaximumWidth(width)
        if height:
            self.text_edit.setFixedHeight(height)
