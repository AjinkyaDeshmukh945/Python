number = 0

def DisplayNumbers(len):
    global number
    if(len > number):
        len = len - number
        print(len  ,end=" ")
        len = len - 1
        DisplayNumbers(len)
        
    
        
def main():
    print("enter input number")
    value = int(input())
    DisplayNumbers(value)
    
if __name__ == "__main__" :
    main()
