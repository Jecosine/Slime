import sys,termios,fcntl
from get_size import get_size

def close_input():
    fd = sys.stdin.fileno()
    termIn_old = termios.tcgetattr(0)
    termIn_new = termios.tcgetattr(0)
    termOut_old = termios.tcgetattr(1)
    termOut_new = termios.tcgetattr(1)
    termIn_new[3] &= ~(termios.ECHO|termios.ICANON)
    termOut_new[3] &= ~(termios.ECHO|termios.ICANON)
    termios.tcsetattr(0,termios.TCSANOW,termIn_new)
    termios.tcsetattr(1,termios.TCSANOW,termOut_new)
    #if len(sys.stdin.read())>1:
    #    #termios.tcsetattr(fd,termios.TCSANOW,term_old)
    #    return "end"
    while (sys.stdin.read(1)!="\x1b"):
        print "233"
    termIn_old[3] |= termios.ECHO|termios.ICANON
    termOut_old[3] |= termios.ECHO|termios.ICANON
    termios.tcsetattr(0,termios.TCSANOW,termIn_old);
    termios.tcsetattr(1,termios.TCSANOW,termOut_old);

close_input ()
