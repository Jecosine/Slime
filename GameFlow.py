"""
This script define a base game class.You should import this script,and hersitate from "Game",customize game configuring should override function "update":
    class Test(Game):
        def __init__(self):
            Game.init(self)
            ...
        def update(self):
            ...

Of course you should implete render or render_once in update.Specific usage can be accessed by checking example scripts.
"""

import gameObject as Object
import engine_utils as utils
from get_size import get_size
import time
import threading
class Game:
    """This class must be instance as a 'game' object if you want to run the game"""
    def __init__(self):
        self.object_count = 0
        self.pixel_count = 0
        self.is_runing = False
        self.canva = []
        self.frame = 0.05
        self.objects = []
        self.rows,self.cols = get_size()
    def add_object(self,obj):
        self.objects.append(obj)

    def set_frame(self,frame):
        self.frame = frame
    def flush_screen(self):
        print "\x1b[3J\x1b[0m"
    
    def init_figure(self,a,b):
        panel = []
    def fill_panel(self):
        """This function set up for filling pixels in the canva,by the way check whether the pixel is in canva"""
        self.canva = []
        if len(self.objects)<>0:
            for obj in self.objects:
                for p in obj.pixels:
                    temp = utils.transform(p.position)
                    if temp not in self.canva and 
                        (temp[1]<=self.cols and temp[0]<=self.rows 
                                and temp[1] > 0 and temp[0] > 0):
                        self.canva.append(temp)
        return self.canva
    def render_once(self):
        """Render for only once"""
        print "\x1b[2J\x1b[?25l\x1b[0m"
        for p in self.canva:
            print "\x1b[0m\x1b[%d;%dH\x1b[7m \x1b[0m" % (p[0],p[1])
        time.sleep(self.frame)
    def render(self):
        """Render forever"""
        while(True):
            print "\x1b[2J\x1b[?25l\x1b[0m"
            for p in self.canva:
                print "\x1b[0m\x1b[%d;%dH\x1b[7m \x1b[0m" % (p[0],p[1])
            time.sleep(self.frame)
        
    def update(self):
        """This function should be override outside"""
        self.is_running = True


