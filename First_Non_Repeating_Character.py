string=str(input("Enter any Thing : ")).replace(" ","")

for i in string:
    if i not in string[string.index(i) + 1:]:
        print(i)
        break