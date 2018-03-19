from GameFlow import Game
import gameObject as go
import engine_utils as utils
import termios,fd


class Test(Game):
    def __init__(self):
        global obj 
        obj = go.Object('obj1',[1.1])
        Game.__init__(self)
        obj.add_pixel([go.pixel([1,1]),go.pixel([2,1]),go.pixel([3,1]),go.pixel([2,2]),go.pixel([2,3])])
        self.add_object(obj)
    def disable_output(self):
    
    def update(self):
        while (True):
            self.canva = self.fill_panel()
            self.is_running = True
            self.render_once()
            obj.move([1,0])
            if obj.position[0]>30:
                obj.position[0]=0

    def __del__(self):
        print "\x1b[?25h"

   # def draw_line(self,t):
        


if __name__=="__main__":
    test = Test()
    test.update()
