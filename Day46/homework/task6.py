def eror(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print(f"can't divide {a} by zero")
        return None
    

print(eror(3, 0))    