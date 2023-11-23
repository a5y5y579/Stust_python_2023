class Demo:
  
    def __init__(self, v1=55, v2=44, v3=33, v4=22, v5=11):
        self.__a = v1
        self.__b = v2
        self.__c = v3
        self.__d = v4
        self.__e = v5
   
    def addition(self):
        return self.__a + self.__b + self.__c + self.__d + self.__e

    def subtraction(self):
        return self.__a - self.__b - self.__c - self.__d - self.__e

    def multiplication(self):
        return self.__a * self.__b * self.__c * self.__d * self.__e

    def division(self):
        
        if self.__b == 0 or self.__c == 0 or self.__d == 0 or self.__e == 0:
            return "0."
        else:
            return self.__a / self.__b / self.__c / self.__d / self.__e
    def squareandaddition(self):
        return self.__a**2+self.__b**2+self.__c**2+self.__d**2+self.__e**2


d1 = Demo()

print("相加:", d1.addition())
print("相減:", d1.subtraction())
print("相乘:", d1.multiplication())
print("相除:", d1.division())
print("平方相加:", d1.squareandaddition())

