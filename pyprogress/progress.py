from .progressbar import *

colors = {
        "black": "\u001b[30m",
        "red": "\u001b[31m",
        "green": "\u001b[32m",
        "yellow": "\u001b[33m",
        "blue": "\u001b[34m",
        "magenta": "\u001b[35m",
        "cyan": "\u001b[36m",
        "white": "\u001b[37m",
        "default": "\u001b[00m"
    }

class ProgressBar(object):

    def __init__(self, task: str, total: int, updateIntervalSeconds: float = 1.0, color: str = "default", style: object = ProgressBarStyle.UNICODE_BLOCK):
        self.__state = ProgressState(task, total)
        self.__thread = ProgressThread(self.__state, style, updateIntervalSeconds)
        self.color = color

    def start(self):
        self.__state.init()
        print(colors[self.color], end="")
        self.__thread.start()
        return self

    def step(self, chunk: int = 1):
        self.__state.step(chunk)

    def jump(seff, n: int):
        self.__state.jump(n)

    def stop(self):
        self.__thread.kill()
        try:
            self.__thread.join()
            print(colors[self.color], flush=True)
        except IOError as e:
            pass
