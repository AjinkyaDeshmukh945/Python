
def main():
    Ans = 0
    try:
      print("enter first number")
      val1 =int(input())
      print("enter second number")
      val2 =int(input())
      Ans = val1 / val2
    except ZeroDivisionError as zobj :
           print("exception occured :",zobj)
    except ValueError as verr :
        print("exception occured")
    except Exception as ex :
        print("exception occured")
    finally:
      print("Inside finally block")
    print("Division is :",Ans)


if __name__ == "__main__" :
    main()