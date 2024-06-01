import os
LogFileName = "Log.txt"
def CheckFileExtensionType(type) :
    extensionTypes = (".img", ".txt", ".docx", ".zip")
    for item in extensionTypes:
      if (item == type):
          return True
      
    return False

        
def DirectoryFileSearch(dName, extType) :
     FileArr = []
     for folderName, subfoldername , filename in os.walk(dName):
        for fname in filename :
            if fname.endswith(extType):
                 FileArr.append(fname)
     if  (os.path.exists(LogFileName)):
        
         fobj =  open(os.path.join(folderName,fname),"a")
         #fobj =  open(LogFileName,"a")
         fobj.write('\n'.join(FileArr))
         fobj.close()
        

            
def main():
    print("Enter the name of directory")
    dName =input()
    if not (type(dName)  == str):
       return  print("Enter Directory name in correct format.")
    
    print("enter the file extention type")
    extType = str(input())
    if not CheckFileExtensionType(extType):
       return  print("Enter correct file extension type.")

    DirectoryFileSearch(dName,extType)


if __name__ == "__main__" :
    main()