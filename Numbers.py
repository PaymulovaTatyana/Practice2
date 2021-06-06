a: int=10
b: int=5
print(a/b)
print(a % 3)
print(b ** 3)
#param = "string" + 15
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", n3)
print("{:4.2f}".format(float(n1)) +" plus " +"{:4.2f}".format(float(n2)) +" = "+" {:4.2f}".format(float(n3)))

a = 1/3
print("{:7.3f}".format(a))
a= 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))