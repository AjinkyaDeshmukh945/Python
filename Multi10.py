import multiprocessing
import os
import time

def fun(no):
    sum = 0
    print("Pid is :", os.getpid())
    for i in range(no) :
     sum  = sum +  (no * no * no)
    return sum
       
def main():
     starttime =time.time()
     Arr = [100000, 200000 ,300000, 400000,500000, 600000, 700000, 800000, 900000, 1000000,1100000, 1200000, 1300000, 1400000]
     result =[]
     p =multiprocessing.Pool()
     result = p.map(fun,Arr)
     p.close()
     p.join()
     print(result)
     endtime = time.time()
     timetaken = endtime - starttime
     print("Time required for execuation is :", timetaken)

if __name__ == "__main__":
    main()