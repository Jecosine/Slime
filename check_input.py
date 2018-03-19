import sys,termios,fcntl
from get_size import get_size

def close_input():
    fd = sys.stdin.fileno()
    term_old = term_new = termios.tcgetattr(0)
    term_new[3] &= ~termios.ECHO
    #termios.tcsetattr(fd,termios.TCSANOW,term_old)
    if sys.stdin.read()[-1] == '\x1b':
        termios.tcsetattr(fd,termios.TCSANOW,term_old)
