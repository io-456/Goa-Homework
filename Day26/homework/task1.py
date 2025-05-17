def numbers():
    start = print(input("აირჩიე დაწყება:"))
    finish = print(input("აირჩიე დამთავრება:"))
    if int(start) > int(finish):
        print("არასწორი შუალედი")
    else:
        for numbers in range(start, finish + 1):
            print(numbers)    

numbers()            
        