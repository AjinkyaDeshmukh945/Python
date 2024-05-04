from functools import reduce

def main() :
    print("enter number  of element to add into list")
    data =[]
    size = int(input())
    print("enter your elements")
    icnt = 0
    for icnt in range(0,size) :
         no = int(input())
         data.append(no)
    print(" Data from input list : " ,data)
    Fdata = list(filter(lambda a: (a % 2 == 0),data))
    print(" Data after filter activity : " ,Fdata)
    Mdata = list(map(lambda a : (a * a),Fdata))
    print(" Data after map activity : " ,Mdata)
    Rdata = reduce((lambda A, B :(A + B)),Mdata)
    print(" Data after reduce activity : " ,Rdata)

if __name__ == "__main__" :
    main()