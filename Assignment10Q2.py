import os
LogFileName = "Log.txt"
def CheckFileExtensionType(type) :
    extensionTypes = (".img", ".txt", ".docx", ".zip")
    for item in extensionTypes:
      if (item == type):
          return True
      
    return False


def change_extension(file_path, new_extension):
    base_name, _ = os.path.splitext(file_path)
    print(base_name)
    new_file_path = base_name  + new_extension
    print(new_file_path)
    os.rename(file_path, new_file_path)

def RenameDocumentType(dName, extType, new_extension) :
     FileArr = []
     for folderName, subfoldername , filename in os.walk(dName):
        for fname in filename :
            if fname.endswith(extType):
                change_extension(fname,new_extension)
                FileArr.append(fname)
               
     
        
        

            
def main():
    print("Enter the name of directory")
    dName =input()
    if not (type(dName)  == str):
       return  print("Enter Directory name in correct format.")
    
    print("enter the file extention type")
    extType = str(input())
    if not CheckFileExtensionType(extType):
       return  print("Enter correct file extension type.")

    print("enter the file extention type")
    extToType = str(input())
    if not CheckFileExtensionType(extType):
       return  print("Enter correct file extension type.")

    RenameDocumentType(dName,extType,extToType)


if __name__ == "__main__" :
    main()