class ChatError(Exception):
    """聊天相关错误的基类"""
    pass


class NetworkError(ChatError):
    """网络相关错误"""
    pass


class ImageLoadError(ChatError):
    """图片加载错误"""
    pass


class ApiError(ChatError):
    """API调用错误"""
    pass


def handle_exception(func):
    """异常处理装饰器"""

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NetworkError as e:
            print(f"网络错误: {str(e)}")
        except ImageLoadError as e:
            print(f"图片加载错误: {str(e)}")
        except ApiError as e:
            print(f"API调用错误: {str(e)}")
        except Exception as e:
            print(f"未知错误: {str(e)}")

    return wrapper
