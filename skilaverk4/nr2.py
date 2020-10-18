class Thing:
    def __init__(self, func, num=None, x=None, veldi=None):
        if num != None:
            self.sign = func
            self.num = num
            self.x = x
            self.veldi = veldi
        elif num == None:
            if func[0]=="-":
                self.sign = "-"
                func = func[1:]
            elif func[0] == "+":
                self.sign = "+"
                func = func[1:]
            else:
                self.sign = "+"

            temp = [ ]
            temp = func.split("x")
            if "x" in func:
                self.x = "x"
                if func[-1].isnumeric():
                    self.veldi = int(temp[1])
                else:
                    self.veldi = 1
                if temp[0] != '':
                    self.num=int(temp[0])
                else:
                    self.num = 1
            elif "x" not in func:
                self.x="x"
                self.veldi=0
                if func[0]== "-" or func[0]=="+":
                    self.num = int(func[1:])
                else:
                    self.num = int(func)

    def heilda(self):
        p = self.sign
        v = self.veldi+1
        n = self.num/v
        return Thing(p,n,"x",v)
    def calculate(self, x):
        if self.sign == "-":
            return -(self.num*x**self.veldi)
        elif self.sign == "+":
            return (self.num*x**self.veldi)

    def __str__(self):
        return "%s%s%s%s"%(self.sign, self.num, self.x, self.veldi)


class Function:
    def __init__(self, func):
        if type(func) == list:
            self.main = func
        elif type(func) == str:
            start = 0
            li = []
            for i in range(len(func)):
                if func[i] == "-" or func[i] == "+":
                    if func[start:i] != '':
                        li.append(Thing(func[start:i]))
                    start = i
                if i == len(func) - 1:
                    li.append(Thing(func[start:i + 1]))
            self.main = li

    def flatarmal(self,a,b):
        new = []
        total = 0
        for i in self.main:
            new.append(i.heilda())
        for i in new:
            total += i.calculate(b)
        for i in new:
            total -= i.calculate(a)
        return total




print("settu inn fall. \nDæmi:\n-2x2+2")
li = Function(input("> "))
print("Flatarmálið er", li.flatarmal(int(input("settu inn neðri mörk: ")), int(input("settu inn efri mörk: "))))

