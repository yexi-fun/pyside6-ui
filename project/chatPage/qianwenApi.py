from openai import OpenAI, APIError
from PySide6.QtCore import QThread, Signal

# API密钥和URL
api_key = 'sk-39451eb748534ad6becde59e919cdaa0'
base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"

# 创建OpenAI客户端
client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)


class ApiThread(QThread):
    response_signal = Signal(str)
    complete_signal = Signal()

    def __init__(self, user_input):
        super().__init__()
        self.user_input = user_input

    def run(self):
        data = {
            "model": "qwen-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": self.user_input}
            ],
            "stream": True  # 启用流式传输
        }

        try:
            # 发送POST请求
            completion = client.chat.completions.create(
                model=data["model"],
                messages=data["messages"],
                stream=data["stream"]
            )

            # 逐行处理流式响应
            for chunk in completion:
                if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    if content:
                        self.response_signal.emit(content)
                        print(content, end='', flush=True)

        except APIError as e:
            print(f"API Error: {e}")
            self.response_signal.emit(f"API请求失败: {str(e)}")
        except Exception as e:
            print(f"请求异常: {e}")
            self.response_signal.emit(f"请求异常: {str(e)}")
        finally:
            self.complete_signal.emit()
