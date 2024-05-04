
def DisplayFact(len):
   if (len == 0):
       return 1
   return len * DisplayFact(len - 1)
      
             
def main():
    print("enter input number")
    value = int(input())
    fact =  DisplayFact(value)
    print(fact)
    
if __name__ == "__main__" :
    main()
