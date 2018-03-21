import Engine_Utils as utils

#class Color():
#    def __init__(self):
#        self.white = "\x1b[7m"

class Object:
    def __init__(self,name,position = [0,0]):
        self.position = [0,0]
        self.is_empty = True
        self.velocity = []
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
    def get_pixels_count(self):
        return len(self.pixels)

    def get_objects_count(self):
        return len(self.objects)

    def add_child(self,obj):
        self.childs.append(obj)

    def set_velocity(self,velocity):
        """pixels per frame"""
        self.velocity = velocity
            
    def move(self,vector):
        self.position = utils.vector_add(vector,self.position)
        for p in self.pixels:
            p.position = utils.vector_add(vector,p.position)
    def add_pixel(self,a):
        """Require a list"""
        for i in a: 
            self.pixels.append(i)

class pixel():
    def __init__(self,position = [0,0]):
        self.position =position
        #self.color = Color().white

    def move(self,vector):
        self.position = utils.vector_add(vector,self.position)
