class Arithmetic :
    
    Add = 0
    sub = 0
    mul = 0
    div = 0
    def __init__(self,A,B):
        self.value1 = A
        self.value2 = B
        

    def Accept(self, A,B):
        self.value1 = A
        self.value2 = B

    def Addition(self):
         Arithmetic.Add = self.value1 +  self.value2 
         return  Arithmetic.Add

    def Substraction(self):
          Arithmetic.sub = self.value1 - self.value2 
          return  Arithmetic.sub
    
    def Multiplication(self):
          Arithmetic.mul = self.value1 *  self.value2 
          return  Arithmetic.mul

    def Division(self):
          Arithmetic.div = self.value1 /  self.value2 
          return  Arithmetic.div


    def Display(self):
        print("Addition is :",self.Radius)
        print("Substraction is :",self.Area)
        print("Multiplication is :",self.Circumference)
        print("Division is :",self.Circumference)

print("enter the value of value1")
val1 = int(input())
print("enter the value of value2")
val2 = int(input())



obj1 = Arithmetic(0,0)
obj1.Accept(val1,val2)
#obj1.Addition()
print("Addition is",obj1.Addition())

#obj1.Substraction()
print("Substraction is",obj1.Substraction())
#obj1.Multiplication()
print("Multiplication is",obj1.Multiplication())
#obj1.Division()
print("Division is",obj1.Division())

obj2 = Arithmetic(30,5)
obj2.Accept(30,5)
print("Addition is",obj2.Addition())
#obj2.Addition()
print("Substraction is",obj2.Substraction())
#obj2.Substraction()
print("Multiplication is",obj2.Multiplication())
#obj2.Multiplication()
print("Division is",obj2.Division())
#obj2.Division()








    
        