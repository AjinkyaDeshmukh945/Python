pattern = 0

def DisplayPattern(len):
    global pattern
    if(pattern < len):
        pattern = pattern + 1
        DisplayPattern(len)
        print('*'  ,end=" ")
    
        
def main():
    print("enter input number")
    value = int(input())
    DisplayPattern(value)
    
if __name__ == "__main__" :
    main()
