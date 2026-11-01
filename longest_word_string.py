string=str(input("Enter any Thing : ")).replace(" ","")
word = ""
longest_word = ""

for i in string:
    if i != " ":
        word = word+i
        if len(word) > len(longest_word):
            longest_word=word
    else :
        word =""
print(longest_word)