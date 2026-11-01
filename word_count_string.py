string=str(input("Enter any Thing : "))
words=0
for i in string:
    if i == " ":
        words += 1
print(f"There are {words+1} in your given string {string.upper()}")


