from cal_func import do_addition,do_subtraction, do_division
from cal_func import do_addition,do_subtraction, do_division
from area import calculate_are_rectangle
def main():
    print('Welcome to the Calculator App')
    print('''
\nselect the function from the given options
          1.Add
          2.Subtract
          3.Multiply
          4.Area
''')

    user_input = input("Select the function-->")
    a= int(input('Value of A: '))
    b= int(input('Value of B: '))

    if user_input == "1":
        result = do_addition(a,b)
    elif user_input =="2":
        result = do_subtraction(a,b)
    elif user_input =="4":
        result = do_division(a,b)



    print("Result:",result)

if __name__=="__main__":
    main()
