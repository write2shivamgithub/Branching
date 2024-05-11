#addition

def do_addition(a,b):
    return a+b

#subtract

def do_subtraction(a,b):
    return a-b

#division

def do_division(a,b):
    try:
        return a/b
    except ZeroDivisiomError as e:
        return 'Cannot divide by zero'