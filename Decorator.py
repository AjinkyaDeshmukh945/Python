def sub(a,b):
   print(a - b) 

def SmartSub(funptr) :
    def inner(a,b) :
        if a < b :
            a,b = b,a
        return funptr(a,b)
    return inner


sub = SmartSub(sub)

def main():
   val1 = int(input("eneter value of no1")) 
   val2 = int(input("eneter value of no2")) 
   sub(val1,val2)




    
if __name__ == "__main__":
    main()