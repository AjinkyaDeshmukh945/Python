
import sys
import os
import time
def DirectoryWatcher(Dname) :
    flag = os.path.isabs(Dname)
    if flag == False :
        print("Path is not Abs path ")
        Dname = os.path.abspath(Dname)
        print("converted Abs path is ", Dname)

    exists = os.path.isdir(Dname)
    if(exists == True) :
       for folderName, subfoldername , filename in os.walk(Dname):
              print("current folder is ",folderName)
              for subfolderName in subfoldername :
                 print("Subfolder is ",subfolderName)

              for fname in filename :
                   print("FileName is",fname)
    else:
        print("There is no such directory")


def main() :
    print("----------------------------------------------------------------------")
    print("--------------Directory Watcher-------------------")
    print("-------------------------------------------------------")
    if(len(sys.argv) ==2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--h") :
          print("This Script is used to perform directory Traversal")
          exit()
        
        if(sys.argv[1] == "--u" or sys.argv[1] == "--U") :
           print("Usage of script:")
           print("Name_of_File  Name_Of_Directory")
           exit()
          
        try:
           StartTime  = time.time()
           DirectoryWatcher(sys.argv[1])
           endTime  = time.time()
           print("time required is ",endTime - StartTime)

        except Exception as obj2 :
           print("Unable to perform due to",obj2)

    else :
        print("Invalid Option")
        print("Use --u to get the usage of application")
        exit()

    print("----------------------------------------------------------------------")
    print("--------------Thank you for using script-------------------")
    print("--------------------Ajinkya-----------------------------------")
    print("--------------------------------------------------------------------")


if __name__ == "__main__" :
    main()