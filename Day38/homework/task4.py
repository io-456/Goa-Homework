def original_element(my_list):
    count = []
    for i in my_list:
        if i not in count:
            counted = 0
            for item in my_list:
                if i == item:
                    counted +=1
            print(f"{i} - {counted}")
            count.append(i)
                    