my_list = [5, 10, 15]

def len_eror(list,index):
    try:
        print(list[index])
        return True
    except IndexError:
        print("not existed index")
        return None
    
print(len_eror(my_list, 4)) 
    