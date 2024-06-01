import sys
import os
import hashlib

def hashFile(path,blockSize = 1024) :
    aFile  = open(path ,'rb')
    hasher = hashlib.md5()
    buf = aFile.read(blockSize)
    while  len(buf) > 0 :
        hasher.update(buf)
        buf = aFile.read(blockSize)
    aFile.close()    
    return hasher.hexdigest()


def DisplayCheckSum(path) :
   
   flag = os.path.isabs(path)
   if flag == False :
      path = os.path.abspath(path)
   exists = os.path.isdir(path)
   if(exists) :
    for folderName, subfoldername , filename in os.walk(path):
        for fname in filename :
           path = os.path.join(folderName,fname)
           fileHash = hashFile(path)
           print(path)
           print(fileHash)
           print('')
   else:
       print("Invalid Path")



def main() :
    print("----------------------------------------------------------------------")
    print("--------------Directory Watcher-------------------")
    print("-------------------------------------------------------")
    if(len(sys.argv) !=2):
      print("Invalid Argument")
      exit()
    if(sys.argv[1] == "--h" or sys.argv[1] == "--h") :
          print("To Display the checksum")
          exit()
        
    if(sys.argv[1] == "--u" or sys.argv[1] == "--U") :
           print("Usage of script:")
           print(" Applicationname Absolute_Path_Of_Directory Extension")
           exit()
          
    try:
        arr =   DisplayCheckSum(sys.argv[1])
    
    except ValueError as obj2 :
           print("Unable to perform due to",obj2)

    except Exception as obj2 :
           print("Unable to perform due to",obj2)
   

    print("----------------------------------------------------------------------")
    print("--------------Thank you for using script-------------------")
    print("--------------------Ajinkya-----------------------------------")
    print("--------------------------------------------------------------------")
             
if __name__ == "__main__" :
    main()