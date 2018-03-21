import Base_Input as bi
from GameFlow import Game
import GameObject as go
from get_size import get_size
import Engine_Utils as utils
#class Snake(go.Object):
#    def __init__(self,name):
#        go.Object.__init__(self,name)
#        self.pixels = []
#        self.add_pixel([go.pixel(),go.pixel(),go.pixel()])
#        self.direction = [-1,0]
#        self.rows,self.cols = get_size()
#        self.position = [self.cols/2,self.rows/2]
#    def __getitem__(self,index):
#        return self.pixels[index]
#    
#    def __add__(self,obj):
#        self.pixels.insert(0,obj)
        
        

class SnakeGame(Game):
    def __init__(self):
        global snake
        snake = go.Object("snake")
        Game.__init__(self)
        self.gameover = False
        self.direction = [-1,0]
        self.add_object(snake)
        self.isPause = False
    
    def Move(self,c):
        if c == "w":
            self.direction = [0,1]
        if c == "s":
            self.direction = [0,-1]
        if c == "d":
            self.direction = [1,0]
        if c == "a":
            self.direction = [-1,0]
        snake += go.pixel(self.direction)
        snake.pixels.pop(-1)
        return 0

    def update(self):
        s = ''
        
        while(True):

            c = bi.get_input()
            s = c
            self.canva = self.fill_panel()
            self.isrunning = True
            if not self.isPause:
                self.Move(s)
                self.render_once()

if __name__== "__main__":
    test = SnakeGame()
    test.update()
