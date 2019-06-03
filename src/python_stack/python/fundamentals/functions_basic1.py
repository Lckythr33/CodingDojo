print("\n #1")
print("prediction: will print 5")
def a():
    return 5
print(a())

print("\n #2")
print("prediction: will print 10")
def a():
    return 5
print(a()+a())

print("\n#3")
print("prediction: will print 5")
def a():
    return 5
    return 10
print(a())

print("\n#4")
print("prediction: will print 5")
def a():
    return 5
    print(10)
print(a())

print("\n#5")
print("prediction: will print 5 and then null")
def a():
    print(5)
x = a()
print(x)

print("\n#6")
print("prediction: error")
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))

print("\n#7")
print("prediction: parses ints as strings and prints 25")
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

print("\n#8")
print("prediction: prints 100 and then 10")
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

print("\n#9")
print("prediction: prints 7, 14 and then 21")
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

print("\n#10")
print("prediction: prints 8")
def a(b,c):
    return b+c
    return 10
print(a(3,5))

print("\n#11")
print("prediction: prints 500, 500, 300, 500")
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

print("\n#12")
print("prediction:  prints 500, 500, 300, 500")
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

print("\n#13")
print("prediction: prints 500, 500, 300, 300")
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

print("\n#14")
print("prediction: prints 1,3,2")
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

print("\n#15")
print("prediction: prints 1,3,5,10")
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)