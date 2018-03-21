import termios
import sys
termIn_old = termios.tcgetattr(0)
termOut_old = termios.tcgetattr(1)


#termOut = termios.tcgetattr(1)
#termIn = termios.tcgetattr(0)


termIn_new = termios.tcgetattr(0)
termOut_new = termios.tcgetattr(1)
#Set attributes
termIn_new[3] &= ~(termios.ECHO|termios.ICANON)
termOut_new[3] &= ~(termios.ECHO|termios.ICANON)

termIn_new[6][termios.VMIN] = 0
termIn_new[6][termios.VTIME] = 1
termOut_new[6][termios.VMIN] = 0
#termOut_new[6][termios.VTIME] = 1
#termIn[6][termios.VTIME] = 1
#termIn[6][termios.VTMIN] = 1
#termOut[6][termios.VMIN] = 0
#termIn[3] &= ~termios.ICANON
#termOut[3] &= ~termios.ICANON

def get_input():
    #close_iodisplay()
    c = sys.stdin.read(1)
    s = ''
    while (c):
        s = c
        c = sys.stdin.read(1)
    return s

def getKey(c):
    if c == get_input():
        return True

def close_iodisplay():
    termios.tcsetattr(0,termios.TCSANOW,termIn_new)
    termios.tcsetattr(1,termios.TCSANOW,termOut_new)

def test():
    termios.tcsetattr(0,termios.TCSANOW,termIn_new)
    termios.tcsetattr(1,termios.TCSANOW,termOut_new)
    print "sadad"
    #restore()

def restore():
    termios.tcsetattr(0,termios.TCSANOW,termIn_old)
    termios.tcsetattr(1,termios.TCSANOW,termOut_old)

