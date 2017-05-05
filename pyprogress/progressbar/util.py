class Util(object):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        pass

    @staticmethod
    def repeat(c: str, n: int):
        if n <= 0:
            return ""
        else:
            sb = [c for _ in range(n)]
            return "".join(sb)

    @staticmethod
    def formatDuration(d: float):
        if d > 3600.0:
            t = "{0:.1f}h".format(d/3600.0)
        elif d > 60.0:
            t = "{0:.1f}m".format(d/60.0)
        else:
            t = "{0:.1f}s".format(d)
        return t
