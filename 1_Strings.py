print("Ex1")
string1 = "This is a string. "
string2 = " This is another string."
print("Ex2")
print(string2 + string1)
print("Ex3")
print(len(string2))
print(string2.title())
print(string2.lower())
print(string1.upper() + string1)
print(string1.rstrip() + string1)
print(string2 + string2.lstrip())
print(string2.strip())
print(string2.strip('g.'))
print("Ex4")
d = "qwerty"
ch = d[2]  # извлекается символ ‘e’
print(ch)
chm = d[1:3]
print(chm)
chm = d[1:]
print(chm)
chm = d[:3]
print(chm)
chm = d[:]
print(chm)
chm = d[1:5:2]
print(chm)
#d[2]='o'