number = 0

def DisplayNumbers(len):
    global number
    if(number < len):
        number = number + 1
        print(number  ,end=" ")
        DisplayNumbers(len)
        
    
        
def main():
    print("enter input number")
    value = int(input())
    DisplayNumbers(value)
    
if __name__ == "__main__" :
    main()
