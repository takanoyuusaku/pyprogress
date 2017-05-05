from .util import Util

import os
import math
import time
from threading import Thread

class ProgressThread(Thread):

    def __init__(self, state: object, style: object, updateInterval: int):
        super(ProgressThread, self).__init__()
        self.__state = state
        self.__style = style
        self.__updateInterval = updateInterval
        self.__running = True
        self.__length = 0

    def progress(self):
        return self.__state.current / self.__state.total

    def progressIntegralPart(self):
        return int(self.progress() * self.__length)

    def progressFractionalPart(self):
        p = self.progress() * self.__length
        fraction = (p - math.floor(p)) * len(self.__style.fractionSymbols)
        return math.floor(fraction)

    def eta(self, elapsed: float):
        et = 0.0 if self.__state.current == 0 else (elapsed / self.__state.current) * self.__state.total
        t = Util.formatDuration(et)
        return Util.repeat(" ", 6 - len(t)) + t

    def percentage(self):
        ep = round(self.__state.current*100 / self.__state.total)
        p = "{0:d}%".format(ep)
        return Util.repeat(" ", 4 - len(p)) + p

    def ratio(self):
        v0 = str(self.__state.current)
        v1 = str(self.__state.total)
        return Util.repeat(" ", len(v1) - len(v0)) + v0 + "/" + v1

    def consoleWidth(self):
        t_size = os.get_terminal_size()
        return t_size.columns

    def refresh(self):
        print("\r", end="")

        elapsed = time.time() - self.__state.startTime

        prefix = self.__state.task + " " + self.ratio() + " " + self.__style.leftBracket
        suffix = self.__style.rightBracket + " " + self.percentage() + " (" + Util.formatDuration(elapsed) + " / " + self.eta(elapsed)+ ") "
        maxSuffixLength = self.consoleWidth() - len(prefix) - 10
        if len(suffix) > maxSuffixLength: suffix = suffix[:maxSuffixLength]

        self.__length = self.consoleWidth() - len(prefix) - len(suffix)
        line = prefix
        line += Util.repeat(self.__style.block, self.progressIntegralPart())
        if self.__state.current < self.__state.total:
            line += self.__style.fractionSymbols[self.progressFractionalPart()]
            line += Util.repeat(self.__style.space, self.__length - self.progressIntegralPart() - 1)
        line += suffix

        print(line, end="")

    def kill(self):
        self.__running = False

    def run(self):
        self.__running = True
        try:
            while self.__running:
                self.refresh()
                time.sleep(self.__updateInterval)
            self.refresh()
        except IOError as e:
            passe
