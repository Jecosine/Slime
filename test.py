from canvas import Game
import gameObject as go
import engine_utils as utils
class Test(Game):
    def __init__(self):
        global obj 
        obj = go.Object('obj1')
        Game.__init__(self)
        obj.add_pixel([go.pixel()])
        self.add_object(obj)
        
    def update(self):
        while (True):
            self.canva = self.fill_panel()
            self.is_running = True
            self.render_once()
            obj.move([1,0])
            if obj.position[0]>30:
                obj.position[0]=0

    def __del__(self):
        print "die"
test = Test()
test.update()
