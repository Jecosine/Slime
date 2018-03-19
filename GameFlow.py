"""
This script define a base game class.You should import this script,and hersitate from "Game",customize game configuring should override function "update":
    class Test(Game):
        def __init__(self):
            Game.init(self)
            ...
        def update(self):
            ...

"""

import gameObject as Object
import engine_utils as utils
from get_size import get_size
import time
import threading
class Game:
    def __init__(self):
        self.object_count = 0
        self.pixel_count = 0
        self.is_runing = False
        self.canva = []
        self.objects = []
        self.rows,self.cols = get_size()
    def add_object(self,obj):
        self.objects.append(obj)

    def flush_screen(self):
        print "\x1b[3J\x1b[0m"
    
    def init_figure(self,a,b):
        panel = []
    def fill_panel(self):
        self.canva = []
        if len(self.objects)<>0:
            for obj in self.objects:
                for p in obj.pixels:
                    temp = utils.transform(p.position)
                    if temp not in self.canva and (temp[1]<=self.cols and temp[0]<=self.rows):
                        self.canva.append(temp)
        print self.canva
        return self.canva
        #check whether pixel is overdraw
    def render_once(self):
        #render
        print "\x1b[2J\x1b[?25l\x1b[0m"
        for p in self.canva:
            print "\x1b[0m\x1b[%d;%dH\x1b[7m \x1b[0m" % (p[0],p[1])
        time.sleep(0.1)
    def render(self):
        while(True):
            print "\x1b[2J\x1b[?25l\x1b[0m"
            for p in self.canva:
                print "\x1b[0m\x1b[%d;%dH\x1b[7m \x1b[0m" % (p[0],p[1])
            time.sleep(0.05)
    def run(self,canva):
        threading._start_new_thread(self.render,(canva,))
        
    def update(self):
        #self.canva =  self.fill_panel()
        self.is_running = True
        #self.render_once()


