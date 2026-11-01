name = "abcabcbb"
s = ""
longest = ""
i = 0

while i < len(name):
    if name[i] not in s:
        s = s + name[i]
        if len(s) > len(longest):
            longest = s
    else:
        s = s[s.index(name[i]) + 1:] + name[i]
    i += 1

print("Longest substring:", longest)
print("Length:", len(longest))