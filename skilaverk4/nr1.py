from math import sqrt, acos, degrees
class Vigur:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def prenta(self):
        print("(%s, %s)" % (self.x, self.y))

    def lengd(self):
        return sqrt(self.x**2+self.y**2)

    def halli(self):
        return self.y/self.x

    def þvervigur(self):
        return Vigur(-(self.y), self.x)

    def horn(self, v):
        return degrees(acos((self.x*v.x+self.y*v.y)/(self.lengd()*v.lengd())))

    def stefnuhorn(self):
        return self.horn(Vigur(1,0))

    def summa(self,v):
        return Vigur(self.x+v.x, self.y+v.y)

# Keyrsluforrit
v1 = Vigur(1,3)
v1.prenta()
print("Lengd: ",v1.lengd())
print("Halli: ",v1.halli())
vþ = v1.þvervigur()
print("Þvervigur: ",end=" ")
vþ.prenta()
print("Stefnuhorn: ",v1.stefnuhorn())
v2 = Vigur(-3,1)
print("Horn milli vigra: ",v2.horn(v1))
v3 = v1.summa(v2)
print("Summa: ",end=" ")
v3.prenta()
