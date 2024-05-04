from functools import reduce
def prime(no):
  flag = False
  if no == 1:
   return False
  elif no > 1:
    for i in range(2, no):
        if (no % i) == 0:
            return False
    if flag:
      return False
    else :
        return True

def MaxF(a,b):
    if(a > b) :
        return a
    else :
     return b



def main() :
    print("enter number  of element to add into list")
    data =[]
    size = int(input())
    print("enter your elements")
    icnt = 0
    for icnt in range(0,size) :
         no = int(input())
         data.append(no)
    print(" Data from input list : " ,data)
    Fdata = list(filter(prime,data))
    print(" Data after filter activity : " ,Fdata)
   # Mdata = list(lambda a : (a * 2),Fdata)
    Mdata = list(map(lambda a : (a * 2),Fdata))
    print(" Data after map activity : " ,Mdata)
    Rdata = reduce(MaxF,Mdata)
    print(" Data after reduce activity : " ,Rdata)

if __name__ == "__main__" :
    main()