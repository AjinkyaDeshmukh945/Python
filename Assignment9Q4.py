import os
import filecmp

def createFile(fname) :
         return open(fname ,"w")
    

def main():
    print("ennter the 1st File Name")
    fname1 = input()
    if not (os.path.exists(fname1)):
       return  print("file is not present in current directory.")
    
    print("enter the 2nd File Name")
    fname2 = input()
    if not (os.path.exists(fname2)):
       return  print("file is not present in current directory.")
    
    result = filecmp.cmp(fname1, fname2, shallow=False)
    if(result) :
         print("File content are same:")
    else:
         print("File content are different:")
    


if __name__ == "__main__" :
    main()