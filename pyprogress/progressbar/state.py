import time
from threading import Lock

class ProgressState(object):

    def __init__(self, task: str, total: int):
        self.task = task
        self.total = total
        self.current = 0
        self.startTime = 0.0
        self.__lock = Lock()

        assert total > 0, "require progress max above 0"

    def init(self):
        with self.__lock:
            self.startTime = time.time()

    def step(self, n: int):
        with self.__lock:
            self.current += n
            if (self.current > self.total): self.current = self.max

    def jump(self, n: int):
        with self.__lock:
            self.current += n
            if (self.current > self.total): self.current = self.max
