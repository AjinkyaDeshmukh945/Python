import os
import filecmp

def createFile(fname) :
         return open(fname ,"w")
    

def main():
    print("ennter the File Name")
    fname1 = input()
    if not (os.path.exists(fname1)):
       return  print("file is not present in current directory.")
    
    print("enter the input string to search")
    inputstring = input()
    if not (type( inputstring)  == str):
       return  print("Enter correct search term.")
    
    frequency = 0
    with open(fname1 ,"r") as file:
       lines = file.readlines()
       for row in lines:
           if row.find(inputstring) != -1:
               frequency = frequency +1
       print('Given input string present :',frequency , 'times')
    


if __name__ == "__main__" :
    main()