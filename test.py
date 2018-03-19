import threading
import base_input
from GameFlow import Game
import gameObject as go
import engine_utils as utils
import termios
import time

class Test(Game):
    def __init__(self):
        global obj 
        obj = go.Object('obj1',[1,1])
        Game.__init__(self)
        obj.add_pixel([go.pixel([1,1]),go.pixel([2,1]),go.pixel([3,1]),go.pixel([2,2]),go.pixel([2,3])])
        self.add_object(obj)
    def Move(self):
        c = base_input.get_input()
        if c == "w":
            obj.move([0,1])
            return 0
        if c == "s":
            obj.move([0,-1])
            return 0
        if c == "a":
            obj.move([-1,0])
            return 0
        if c == "d":
            obj.move([1,0])
            return 0
    
    def update(self):
        #threading._start_new_thread(self.render,())
        while (True):
            self.canva = self.fill_panel()
            self.is_running = True
            self.Move()
            self.current_log=str(self.canva+[obj.pixels[i].position for i in range(5)])
            self.render_once()
#            self.update_log()

           

    def __del__(self):
        base_input.restore()
        print "\x1b[?25h"

   # def draw_line(self,t):
        


if __name__=="__main__":
    test = Test()
    test.update()
