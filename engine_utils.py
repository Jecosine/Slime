from get_size import get_size
import math

def vector_add(a,b):
    if len(a) == len(b):
        length = len(a)
    else:
        return None
    return [a[i]+b[i] for i in range(length)]

def vector_pmultiply(t,a):
    return [a[i] * t for i in range(len(a))]

def zero(self):
    return [0,0]

def magnitude(a):
    return math.sqrt(a[0]**2,a[1]**2)

def transform(a):
    #transform the position to render position
    rows,cols = get_size()
    return [rows-a[1],a[0]]
