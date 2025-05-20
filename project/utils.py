import os
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

def load_and_scale_image(image_path, width, height):
    """加载并缩放图片"""
    if not os.path.exists(image_path):
        return create_default_image(width, height)
        
    pixmap = QPixmap(image_path)
    if pixmap.isNull():
        return create_default_image(width, height)
        
    return pixmap.scaled(
        width, 
        height,
        Qt.KeepAspectRatio,
        Qt.SmoothTransformation
    )

def create_default_image(width, height, color=Qt.gray):
    """创建默认图片"""
    pixmap = QPixmap(width, height)
    pixmap.fill(color)
    return pixmap

def get_resource_path(relative_path):
    """获取资源文件的绝对路径"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, relative_path)

def format_markdown_html(text, font_size=19):
    """格式化Markdown文本为HTML"""
    import markdown
    html = markdown.markdown(text)
    return f'<span style="font-size: {font_size}px;">{html}</span>'
