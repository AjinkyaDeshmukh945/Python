class Circle :
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self, rad):
        self.Radius = rad

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius


    def Display(self):
        print("Value of Radius is :",self.Radius)
        print("Value of Area is :",self.Area)
        print("Value of Circumference is :",self.Circumference)

def main():
    print("enter the value of radius")
    r = float(input())


    obj1 = Circle()
    obj1.Accept(r)
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    obj2 = Circle()
    obj2.Accept(4.5)
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()

if __name__ == "__main__" :
    main()





    
        