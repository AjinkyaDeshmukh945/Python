import os
def main():
    print("ennter the name of file")
    fname = input()
    if(os.path.exists(fname)):
        fobj =  open(fname,"r")
        Data = fobj.read()
        print(Data)
    else:
     print("file is not present in current directory.")


if __name__ == "__main__" :
    main()