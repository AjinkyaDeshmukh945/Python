import os

def createFile(fname) :
         return open(fname ,"w")
    

def main():
    print("ennter the name of file you want to create")
    fname1 = input()
    fobj1 = createFile(fname1)
    print("enter the name of file from which you want to copy the content")
    fname2 = input()
    if(os.path.exists(fname2)):
        fobjcopy =  open(fname2,"r")
        Data = fobjcopy.read()
        fobj1.write(Data)
        print("copy operation done sucessfully..")
    else:
     print("file is not present in current directory.")


if __name__ == "__main__" :
    main()