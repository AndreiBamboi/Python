try:
    import msvcrt
    def getkey():
        """Asteapta tasta si returneaza un carnatz"""
        return msvcrt.getch()

except ImportError:
    import sys
    import tty
    import termios
    def getkey():
        fd = sys.stdin.fileno()
        original_at = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_at)
        return ch
import glob
import os

os.stat(p).st_size