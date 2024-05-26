import os
def main() :
    print("enter the file name to check")
    fname = input()
    if os.path.exists(fname):
        print("file exists..")
    else:
     print("file is not present in current directory.")

if __name__ == "__main__":
    main()