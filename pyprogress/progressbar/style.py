class AbstractProgressBarStyle(object):

    def __init__(self, leftBracket: str, rightBracket: str, block: str, space: str, fractionSymbols: str):
        self.leftBracket = leftBracket
        self.rightBracket = rightBracket
        self.block = block
        self.space = space
        self.fractionSymbols = fractionSymbols


class ProgressBarStyle(AbstractProgressBarStyle):

    UNICODE_BLOCK = AbstractProgressBarStyle("│", "│", '█', ' ', " ▏▎▍▌▋▊▉")
    ASCII = AbstractProgressBarStyle("[", "]", '=', ' ', ">")

    def __init__(self, leftBracket: str, rightBracket: str, block: str, space: str, fractionSymbols: str):
        super(self).__init__(leftBracket, rightBracket, block, space, fractionSymbols)
