from math import*
class Geometry_m:
    def __init__(self, a= None, b=None, c=None, d=None, R=None) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.R = R
    def triangle(self):
        P = self.a + self.b + self.c
        p = (self.a + self.b + self.c)/2
        S = sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        return P,S
    def rectangle(self):
        P = self.a + self.b + 
        S = self.a * self.b
        return P, S
    def cricle(self):
        # l = 2 + pi* self.R
        return self.R