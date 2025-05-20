#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Yexi-UI 主程序入口
"""

import sys
import logging
from PySide6.QtWidgets import QApplication

from project import MyWindow
from project.config import WINDOW_TITLE
from project.exceptions import handle_exception

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@handle_exception
def main():
    """程序主入口"""
    # 创建应用实例
    app = QApplication(sys.argv)

    # 创建并配置主窗口
    window = MyWindow()
    window.setWindowTitle(WINDOW_TITLE)
    window.show()

    # 启动应用
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
