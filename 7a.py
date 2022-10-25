import math

class shape:

    def __init__(self):
        self.calc_area = 0
        
    
class triangle(shape):

    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c

    def area(self):
        s=(self.a+self.b+self.c)/2
        calc_area=math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        return calc_area

class circle(shape):

    def __init__(self,r):
        self.r = r

    def area(self):
        self.calc_area = math.pi * self.r**2
        return self.calc_area

class rectangle(shape):

    def __init__(self,b,h):
        self.b = b
        self.h = h

    def area(self):
        self.calc_area = self.b*self.h
        return self.calc_area

def function_main():

    t1=triangle(4,13,15)
    c1=circle(5)
    r1=rectangle(5,6)
    print("Area of rectangle is",t1.area())
    print("Area of circle is",c1.area())
    print("Area of rectangle is",r1.area())

if __name__=='__main__':
    print(__doc__)
    function_main()


