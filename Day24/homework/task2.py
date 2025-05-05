languges = ["html", "CSS", "C++", "python", "C#", "JavaScript", "TypeScript", "Tsql", "Php", "Perl", "visualbasic"]

def isEven(number):
    if (number % 2) == 0:
        return True
    else:
        return False  

for word in languges:
    index = languges.index(word)

    if isEven(index):
        print("even")
    else:
        print("odd")    


