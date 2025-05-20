import time
import os
import markdown
from PySide6.QtCore import Qt, QPointF, QTimer, QEvent, QObject, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QTextEdit
from functools import lru_cache
from project.chatPage.qianwenApi import ApiThread

# 定义样式常量
USER_MSG_STYLE = """
    QTextEdit {
        background-color:#d5d8dc;
        margin-left: 45px;
        margin-right:5px;
        border:1px solid #abb2b9;
        border-radius:5px;
    }
"""

REPLY_MSG_STYLE = """
    QTextEdit {
        background-color:#d6eaf8 ;
        margin-right: 45px;
        margin-left:5px;
        border:1px solid #85c1e9;
        border-radius:5px;
    }
"""

class ChatBings(QObject):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.reply_text = ""
        self.reply_text_edit = None
        self._setup_avatars()
        
    def _setup_avatars(self):
        """预加载和缓存头像"""
        # 获取正确的图片路径
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.user_avatar = QPixmap(os.path.join(base_path, "images", "images", "user.jpg"))
        self.ai_avatar = QPixmap(os.path.join(base_path, "images", "images", "ai-pic.jpg"))

        # 预先缩放头像
        if not self.user_avatar.isNull() and not self.ai_avatar.isNull():
            self.scaled_user_avatar = self.user_avatar.scaled(
                40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            self.scaled_ai_avatar = self.ai_avatar.scaled(
                40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        else:
            print("Warning: Failed to load avatar images")
            # 创建一个默认的纯色图片作为备用
            self.scaled_user_avatar = self._create_default_avatar(Qt.blue)
            self.scaled_ai_avatar = self._create_default_avatar(Qt.green)

    def _create_default_avatar(self, color):
        """创建默认头像"""
        pixmap = QPixmap(40, 40)
        pixmap.fill(color)
        return pixmap

    def send_message(self):
        text = self.window.textEdit_input.toPlainText().strip()
        if not text:
            return
            
        # 发送用户消息
        user_msg_widget = self.create_message_widget(text, USER_MSG_STYLE, "user")
        self.window.chat_layout.addWidget(user_msg_widget)
        
        # 清空输入并滚动到底部
        self.window.textEdit_input.clear()
        self._scroll_to_bottom()
        
        # 获取AI回复
        self.get_api_reply(text)

    def eventFilter(self, obj, event):
        if obj == self.window.textEdit_input and event.type() == QEvent.KeyPress:
            if event.key() in (Qt.Key_Enter, Qt.Key_Return):
                if event.modifiers() & Qt.ShiftModifier:
                    # Shift+Enter 插入换行
                    cursor = self.window.textEdit_input.textCursor()
                    cursor.insertText("\n")
                    return True
                else:
                    # Enter 发送消息
                    self.send_message()
                    return True
        return super().eventFilter(obj, event)

    def get_api_reply(self, user_input):
        self.reply_text = ""
        # 创建回复消息组件
        reply_msg_widget = self.create_message_widget("", REPLY_MSG_STYLE, "agent")
        self.reply_text_edit = reply_msg_widget.findChild(QTextEdit)
        self.window.chat_layout.addWidget(reply_msg_widget)
        
        # 启动API线程
        self.api_thread = ApiThread(user_input)
        self.api_thread.response_signal.connect(self._update_reply)
        self.api_thread.complete_signal.connect(self._complete_reply)
        self.api_thread.start()

    def _update_reply(self, content):
        """更新回复内容"""
        self.reply_text += content
        self._set_html_content(self.reply_text_edit, self.reply_text)
        self._scroll_to_bottom()

    def _complete_reply(self):
        """完成回复"""
        self._set_html_content(self.reply_text_edit, self.reply_text)

    @staticmethod
    def _set_html_content(text_edit, text):
        """设置HTML内容并更新大小"""
        html = markdown.markdown(text)
        html = f'<span style="font-size: 19px;">{html}</span>'
        text_edit.setHtml(html)
        QTimer.singleShot(10, lambda: ChatBings.update_text_edit_size(text_edit))

    def create_message_widget(self, text, style_sheet, msg_type):
        """创建消息组件"""
        msg = QWidget()
        msg_layout = QHBoxLayout(msg)
        msg_layout.setContentsMargins(0, 0, 0, 0)
        msg_layout.setSpacing(0)

        # 创建头像标签
        avatar = self._create_avatar_label(msg_type)
        
        # 创建时间标签
        time_label = self._create_time_label()
        self.window.chat_layout.addWidget(time_label, alignment=Qt.AlignTop | Qt.AlignCenter)

        # 创建文本编辑器
        text_edit = self._create_text_edit(text, style_sheet)
        
        # 创建占位组件
        spacer = QWidget()

        # 根据消息类型布局组件
        self._layout_message_components(msg_layout, avatar, text_edit, spacer, msg_type)
        
        return msg

    def _create_avatar_label(self, msg_type):
        """创建头像标签"""
        avatar = QLabel()
        avatar.setFixedSize(40, 40)
        avatar.setPixmap(
            self.scaled_user_avatar if msg_type == "user" else self.scaled_ai_avatar
        )
        return avatar

    @staticmethod
    def _create_time_label():
        """创建时间标签"""
        time_label = QLabel(time.strftime("%Y-%m-%d %H:%M:%S"))
        return time_label

    def _create_text_edit(self, text, style_sheet):
        """创建文本编辑器"""
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        text_edit.setStyleSheet(style_sheet)
        text_edit.setViewportMargins(0, 2, 0, 0)
        
        self._set_html_content(text_edit, text)
        return text_edit

    @staticmethod
    def _layout_message_components(layout, avatar, text_edit, spacer, msg_type):
        """布局消息组件"""
        if msg_type == "user":
            layout.addWidget(spacer, alignment=Qt.AlignTop)
            layout.addWidget(text_edit, alignment=Qt.AlignTop)
            layout.addWidget(avatar, alignment=Qt.AlignTop)
        else:
            layout.addWidget(avatar, alignment=Qt.AlignTop)
            layout.addWidget(text_edit, alignment=Qt.AlignTop)
            layout.addWidget(spacer, alignment=Qt.AlignTop)

    def _scroll_to_bottom(self):
        """滚动到底部"""
        scrollbar = self.window.scroll_area.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    @staticmethod
    @lru_cache(maxsize=100)
    def _calculate_text_width(word_count):
        """计算文本宽度（使用缓存优化）"""
        return 79 + 19 * (word_count - 1)

    @staticmethod
    def update_text_edit_size(text_edit):
        """更新文本编辑器大小"""
        # 获取文本文档
        doc = text_edit.document()
        
        # 设置最大宽度
        word_count = len(text_edit.toPlainText())
        text_edit.setMaximumWidth(ChatBings._calculate_text_width(word_count))
        
        # 设置高度
        margins = text_edit.contentsMargins()
        height = doc.size().height() + margins.top() + margins.bottom() + 5
        text_edit.setFixedHeight(height)

    def resizeEvent(self):
        """处理窗口大小改变事件"""
        for i in range(self.window.chat_layout.count()):
            if widget := self.window.chat_layout.itemAt(i).widget():
                if text_edit := widget.findChild(QTextEdit):
                    self.update_text_edit_size(text_edit)