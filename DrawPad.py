import Base_Input
from GameObject import Object,pixel
import Engine_Utils as utils
from GameFlow import Game
class DrawPad(Game):

    def __init__(self):
        Game.__init__(self)
        global cursor
        cursor = Object("cursor",[self.cols/2,self.rows/2])
        
        cursor.add_pixel([pixel([self.cols/2,self.rows/2])])
        self.add_object(cursor)

    def Move(self,c):
        if c == "w":
            cursor.move([0,1])
        if c == "s":
            cursor.move([0,-1])
        if c == "d":
            cursor.move([1,0])
        if c == "a":
            cursor.move([-1,0])
        if c == " ":
            temp = Object(' ',cursor.position)
            temp.add_pixel([pixel(cursor.position)])
            self.add_object(temp)
        if c == "\x1b":            
            self.set_pause()
            return 0
        return 0
    def update(self):
        self.isrunning = True
        self.isPause = False
        while (True):
            c = Base_Input.get_input()
            self.canva = self.fill_panel()
            self.update_log()
            self.current_log = str(cursor.position)
            if not self.isPause:
                self.Move(c)
                self.render_once()
    def __del__(self):
        f = open("saved",'wb')
        f.write(str(cursor.pixels))
        f.close()

if __name__ == "__main__":
    test = DrawPad()
    test.update()
