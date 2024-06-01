import os
import sys
import shutil

def CheckFileExtensionType(type) :
    extensionTypes = (".img", ".txt", ".docx", ".zip")
    for item in extensionTypes:
      if (item == type):
          return True
      
    return False


def copyDirectory(dName1, dNam2,fileType) :
   
    flag = os.path.isabs(dName1)
    if flag == False :
      print("Path is not Abs path ")
      dName1 = os.path.abspath(dName1)
      print(dName1)
    
    flag = os.path.isabs(dNam2)
    if flag == False :
      print("Path is not Abs path ")
    # dNam2 = os.path.abspath(dNam2)
      print(dNam2)
    if CheckFileExtensionType(fileType) == True :
      os.mkdir(os.path.join(os.path.dirname(dName1),dNam2))
      for folderName, subfoldername , filename in os.walk(dName1):
        for fname in filename :
           if(fname.lower().endswith(fileType)) :
              shutil.copy(fname, os.path.join(os.path.dirname(dName1),dNam2))
      print("Task completed Successfully..")
          
    
    else :
        print("Please enter correct file type")
           


def main() :
    print("----------------------------------------------------------------------")
    print("--------------Directory Watcher-------------------")
    print("-------------------------------------------------------")
    if(len(sys.argv) ==2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--h") :
          print("This Script is used to copy files from one folder to another")
          exit()
        
        if(sys.argv[1] == "--u" or sys.argv[1] == "--U") :
           print("Usage of script:")
           print("Name_of_File  Name_Of_Folder Name_Of_CopyToFolder")
           exit()
          
      
    if(len(sys.argv) ==3):
        print("Invalid Option")
        print("Use --u to get the usage of application")
    if(len(sys.argv) ==4):
          try:
           copyDirectory(sys.argv[1], sys.argv[2] , sys.argv[3])

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