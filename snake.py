import Base_Input as bi
from GameFlow import Game
import GameObject as go
from get_size import get_size
import Engine_Utils as utils
class Snake(go.Object):
    def __init__(self,name):
        go.Object.__init__(self,name)

        self.direction = [-1,0]
        self.rows,self.cols = get_size()
        self.position = [self.cols/2,self.rows/2]
        self.add_pixel([go.pixel(self.position),go.pixel([self.position[0]+1,self.position[1]]),go.pixel([self.position[0]+2,self.position[1]]),go.pixel([self.position[0]+3,self.position[1]]),go.pixel([self.position[0]+4,self.position[1]])])
    
    def judge(self,position):
        if position in snake.pixels:
            return False
        else:
            return True

    def add_p(self,position):
        self.pixels.insert(0,go.pixel(position))
        return 0
        

class SnakeGame(Game):
    def __init__(self):
        snake = Snake("snake")
        global snake
        Game.__init__(self)
        self.gameover = False
        self.direction = [-1,0]
        self.add_object(snake)
        self.isPause = False
        self.frame = 0.1 
    def Move(self,c):
        if c == "w":
            self.direction = [0,1]
        if c == "s":
            self.direction = [0,-1]
        if c == "d":
            self.direction = [1,0]
        if c == "a":
            self.direction = [-1,0]
        if c == "\x1b":
            self.set_pause()
            return 0
        snake.position = utils.vector_add(snake.position,self.direction)
        snake.add_p(snake.position)
        snake.pixels.pop(-1)
        return 0

    def update(self):
        s = ''
        
        while(True):

            c = bi.get_input()
            s = c
            self.canva = self.fill_panel()
            self.isrunning = True
            self.current_log = str(len(snake.pixels))
            self.update_log()
            if not self.isPause:
                self.Move(s)
                self.render_once()

if __name__== "__main__":
    test = SnakeGame()
    test.update()
