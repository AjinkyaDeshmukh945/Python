
import sys

import sys
def Addition(a,b) :
    return a + b

def main() :
    if(len(sys.argv) ==2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--h") :
          print("This Script is used to perform addition of two integer")
          exit()
        
        if(sys.argv[1] == "--u" or sys.argv[1] == "--U") :
           print("Usage of script:")
           print("Name of file  First Argument Second Argument")
           print("Both argument should be in integer")
           exit()
        else :
           print("Invalid Option")
           print("Use --u to get the usage of application  use --h to get the help")
           exit()
    
    if(len(sys.argv) ==3):
      try:
          ret = Addition(int(sys.argv[1]) , int(sys.argv[2]))
          print("Addition is :",ret)

      except ValueError as obj1 :
          print("Invalid object:",obj1)
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