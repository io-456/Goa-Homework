while True:
    user_input = input("enter number: ")
    try:
        num = int(user_input)
        break
    except ValueError:
        print(f"{user_input} is not valid. enter only numbers")
        
print(num)        
        