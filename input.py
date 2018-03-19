import termios
import sys
termIn_old = termios.tcgetsttr(0)
termOut_old = termios.tcgerattr(1)

termIn_new = termios.tcgetsttr(0)
termOut_new = termios.tcgetsttr(0)
#Set attributes
termIn_new &= ~(termios.ECHO|termios.ICANON)
termOut_new &= ~(termios.ECHO|termios.ICANON)

def get_input():
    s = sys.stdin.read(1)
    return s

def getKey(c):
    if c == get_input():
        return True

def close_iodisplay():
    termios.tcsetattr(0,termios.TCSANOW,termIn_new)
    termios.tcsetattr(1,termios.TCSANOW,termOut_new)

def restore():
    termios.tcsetattr(0,termios.TCSANOW,termIn_old)
    termios.tcsetattr(0,termios.TCSANOW,termOut_old)

