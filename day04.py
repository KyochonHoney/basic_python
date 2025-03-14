#클래스

class Cookie:
    pass

a = Cookie()
b = Cookie()
print(type(a), type(b))

class Fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def abstract(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second  
        return result

a = Fourcal()
a.setdata(4, 2)
print(a.add())