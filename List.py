list1 = [82,8,23,97,92,44,17,39,11,12]
print(dir(list1))
help(list1.insert)
help(list1.append)
help(list1.sort)
help(list1.remove)
help(list1.reverse)
list1[2]=0
print(list1)
list1.append(10)
print(list1)
list1.insert(3,1)
print(list1)
del list1[2]
print(list1)
list1.pop()
print(list1)
list1.sort(reverse = True)
print(list1)
list2 = [3,5,6,2,33,6,11]
lis = sorted(list2)
print(lis)