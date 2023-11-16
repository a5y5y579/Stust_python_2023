class MyShape:
    
    def __init__(self, side, length, width, radius):
        self.side = side
        self.length = length 
        self.width = width
        self.radius = radius
    
    def rectangle(self):
        area = self.length * self.width
        print(f"The area is {area}")

    def square(self):
        area = self.side ** 2
        print(f"The area is {area}")

    def circle(self):
        area = 3.14 * (self.radius ** 2)
        print(f"The area is {area}")

p1 = MyShape(5, 10, 15, 20)
p1.rectangle()
p1.square()
p1.circle()
