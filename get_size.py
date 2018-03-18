import sys
import os
import termios,fcntl,struct
def get_size():
    fd = sys.stdin.fileno()
    term = termios
    size = struct.unpack("hh",fcntl.ioctl(fd,termios.TIOCGWINSZ,'xxxx'))
    return size
