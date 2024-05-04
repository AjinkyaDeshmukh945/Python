import threading
import os
def displayEven(num):
    print("pid of even process",os.getpid())
    print("tid of even process",threading.get_ident())
    print("list of even number")
    x=2
    for i in range(num):
       print(x)
       x= x+2
      
      
        
def displayOdd(num):
    print("pid of odd process",os.getpid())
    print("tid of odd process",threading.get_ident())
    print("list of odd number")
    x = 1
    for i in range(num):
       print(x)
       x= x+2 
       
      
   

def main():
    print("pid of main process",os.getpid())
    print("tid of main process",threading.get_ident())
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