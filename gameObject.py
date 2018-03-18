import engine_utils as utils

#class Color():
#    def __init__(self):
#        self.white = "\x1b[7m"

class Object:
    def __init__(self,name,position = [0,0]):
        self.position = [0,0]
        self.is_empty = True
        self.pixels = []
        self.childs = []
        self.childs_count = len(self.childs)
        self.pixels_count = len(self.pixels)
        self.name = name
    def isEmpty(self):
        if self.pixels < 0:
            return True
        else:
            return False

    def add_child(self,obj):
        self.childs.append(obj)

    def move(self,vector):
        self.position = utils.vector_add(vector,self.position)
        for p in self.pixels:
            p.position = utils.vector_add(vector,self.position)
    def add_pixel(self,a):
        """Require a list"""
        for i in a: 
            self.pixels.append(i)

class pixel():
    def __init__(self):
        self.position = [0,0]
        #self.color = Color().white

    def move(self,vector):
        self.position = utils.vector_add(vector,self.position)