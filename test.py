from time import sleep
from pyprogress.progress import ProgressBar

if __name__ == "__main__":
    p = ProgressBar("Loading", 10).start()
    for i in range(10):
        sleep(1)
        p.step()
    p.stop()
