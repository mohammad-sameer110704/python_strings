string=str(input("Enter any Thing : "))
name=""
for i in string:
    if i not in name:
        name = name + i
    else:
        print(f"The first repeating charecter in your given string {string.upper()} is {i}")
        break
# print(f"There is no repeating charecter in your given string {string.upper()}")