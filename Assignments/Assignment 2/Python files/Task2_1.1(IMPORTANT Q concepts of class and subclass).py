class SidesOFTriangle:
    def __init__(self, a=2, b=2, c=2):
        self.sideA = a
        self.sideB = b
        self.sideC = c


class AreaOfTriangle(SidesOFTriangle):
    def area(self):
        s = (self.sideA + self.sideB + self.sideC) / 2
        return (s * (s - self.sideA) * (s - self.sideB) * (s - self.sideC)) ** 0.5


x = int(input())
y = int(input())
z = int(input())
AreaOfTriangle_object = AreaOfTriangle(x, y, z)
result = AreaOfTriangle_object.area()

print(result)