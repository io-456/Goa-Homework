basket = ["მსხალი", "ვაშლი", "ატამი", "ალუბალი", "ბალი", "ლეღვი", "კომში"]
your_fruit = input("აირჩიე შენი საყვარელი ხილი:")
fruit_inbasket = False

for item in basket:
    if item == your_fruit:
        fruit_inbasket = True
        
    
if fruit_inbasket:
    print("კარგი არჩევანი")
else:
    print("არ არის ხილი კალათაში")    