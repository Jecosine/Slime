import sys
from get_list import get_list
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
        if position in [snake.pixels[i].position for i in range(len(snake.pixels))]:
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
        #self.gameover = False
        self.direction = [-1,0]
        self.add_object(snake)
        self.isPause = False
        self.frame = 0.1 
    def get_command(self,s):
        if s == ":q":
            self.isrunning = False
        if s == ":r":
            self.__init__()
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
        if snake.judge(snake.position):
            snake.add_p(snake.position)
            snake.pixels.pop(-1)
        else:
            self.gameover()
        return 0
        
    def gameover(self):
        self.objects = []
        content = open('gameover','r').read()
        pos = get_list(content)
        gameover_obj = go.Object('gameover')
        gameover_obj.add_pixel([go.pixel(i) for i in pos])
        self.add_object(gameover_obj)
        self.fill_panel()
        self.render_once()
        self.set_pause()
        return 0

    def update(self):
        s = ''
        self.isrunning = True
        while(self.isrunning):

            c = bi.get_input()
            s = c
            self.canva = self.fill_panel()
            self.isrunning = True
            self.current_log = str(len(snake.pixels))
            self.update_log()
            if not self.isPause:
                self.Move(s)
                self.render_once()
        
        print "\x1b[1;1H\x1b[2J\x1b[0m",

if __name__== "__main__":
    test = SnakeGame()
test.update()
