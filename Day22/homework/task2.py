vegetables = ["კიტრი", "პომიდორი", "ნიორი", "ხახვი", "წიწაკა"]
try:
    user_in = input("enter a number from 0 to 4:")
    user_choise = int(user_in)
    print("you chose:", vegetables[user_choise])
except ValueError: 
     print("the entered data isn't number")
except IndexError:
     print("the number entered isn't between 0 and 4")