number = 0
digits=[]
def DisplaySum(digits):
    global number
    if len (digits) == 0 :
        return 0
    else:
         return digits[0] + DisplaySum(digits[1:])
       
        
def main():
    print("enter input number")
    value = int(input())
    while value > 0 :
        digits.append(value % 10)
        value = (value -value % 10)//10
    sum =  DisplaySum(digits)
    print(sum)
    
if __name__ == "__main__" :
    main()
