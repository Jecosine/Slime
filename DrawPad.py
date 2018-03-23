import Base_Input
from GameObject import Object,pixel
import Engine_Utils as utils
from time import time
from GameFlow import Game

class DrawPad(Game):

    def __init__(self):
        Game.__init__(self)
        global cursor
        global temp
        cursor = Object("cursor",[self.cols/2,self.rows/2])
        temp = Object('temp',[0,0])
        cursor.add_pixel([pixel([self.cols/2,self.rows/2])])
        self.add_object(cursor)
        self.add_object(temp)
        self.data = ''

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
            #temp = Object(' ',cursor.position)
            #if cursor.position not in [temp.pixels[i].positon for i in range(len(temp.pixels))]:
            if len(temp.pixels)>0:
                if cursor.position not in [temp.pixels[i].position for i in range(len(temp.pixels))]:
                    temp.add_pixel([pixel(cursor.position)])
            else:
                temp.add_pixel([pixel(cursor.position)])
                return 0
            #self.add_object(temp)
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
                self.data = str([temp.pixels[i].position for i in range(len(temp.pixels))])
    def get_command(self,s):
        if s == ":w":
            tempfile = open(str(int(time.time()),'wb'))
            tempfile.write(self.data)
            tempfile.close()
            print "\x1b[2J",
            return 0
        if s.split(' ')[0] == ":load":
            filename = s.split(' ')[1]
            try:
                newfile = open(filename,'rb')
                content = newfile.read()
            except:
                self.current_log = content
                pass
        print "\x1b[2K",
    def __del__(self):
        f = open("saved",'wb')
        f.write(self.data)
        f.close()
        Base_Input.restore()
        print "\x1b[2J\x1b[?25h"

if __name__ == "__main__":
    test = DrawPad()
    test.update()


