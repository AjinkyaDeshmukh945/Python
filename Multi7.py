import threading
import os
def displayEven(num):
   
    print("list of even number")
    x=2
    for i in range(num):
       print("even",x)
       x= x+2
      
      
        
def displayOdd(num):
   
    print("list of odd number")
    x = 1
    for i in range(num):
       print("odd ",x)
       x= x+2 
       
      
   

def main():
   
    print("enter number")
    value  = int(input())
    p1 =threading.Thread(target=displayEven,args=(value,))
    p2 =threading.Thread(target=displayOdd,args=(value,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("end of main process")

if __name__ == "__main__":
    main()