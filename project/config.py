import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 资源文件目录
IMAGES_DIR = os.path.join(BASE_DIR, 'images')
ICONS_DIR = os.path.join(IMAGES_DIR, 'icons')
AVATARS_DIR = os.path.join(IMAGES_DIR, 'images')

# UI配置
WINDOW_MIN_SIZE = (980, 575)
WINDOW_TITLE = "Yexi-ui"

# 聊天界面配置
CHAT_STYLES = {
    "USER_MSG_STYLE": """
        QTextEdit {
            background-color:#d5d8dc;
            margin-left: 45px;
            margin-right:5px;
            border:1px solid #abb2b9;
            border-radius:5px;
        }
    """,
    "REPLY_MSG_STYLE": """
        QTextEdit {
            background-color:#d6eaf8;
            margin-right: 45px;
            margin-left:5px;
            border:1px solid #85c1e9;
            border-radius:5px;
        }
    """
}

# 字体配置
FONT_CONFIGS = {
    "TITLE": {
        "family": "STCaiyun",
        "size": 20,
        "weight": "bold"
    },
    "CHAT": {
        "size": 19
    }
}

# 图标配置
ICON_CONFIGS = {
    "size": (16, 16),
    "maximize": ":/icons/images/icons/cil-media-stop.png",
    "restore": ":/icons/images/icons/cil-clone.png",
    "minimize": ":/icons/images/icons/cil-minus.png",
    "close": ":/icons/images/icons/cil-x.png",
    "home": ":/icons/images/icons/cil-home.png",
    "settings": ":/icons/images/icons/cil-settings.png"
}

# 窗口样式
WINDOW_STYLE = """
#bgApp {	
    border-radius:5px;
}
#contentBox {
    border-bottom-left-radius:5px;
    background-color:#212327;
}
#topBar {
    background-color:#17202a;
}
#barRightBox {
    background-color:transparent;
}
#mainContent {
    border: 2px solid #822e9d;
}
#maximizeButton, #minimizeButton, #quitButton {
    background-color:#17202a;
}
#topBarTitle {
    color:white;
}
#logo {
    background-color:transparent;
}
#logoLabel {
    border-radius: 15px;
    background-image: url(:/logo/images/images/hutao-logo.png);
    border: 2px solid #822e9d;
}
#leftMenu {
    background-color:#212327;
}
#leftMenuTop, #spaceFrame {
    background-color:transparent;
}
#rightBox {
    background-color:#212327;
}
#stackedWidget {
    background-color:#566573;
}
#scroll_area {
    border:2px solid #212f3c;
}
#textEdit_input {
    border:1px solid #212f3c;
    background-color:rgb(255, 255, 255);
    border-radius:10px;
}
QPushButton {
    background-color:#212327;
}
QPushButton:hover {
    background-color:rgb(85, 255, 0);
}
"""
