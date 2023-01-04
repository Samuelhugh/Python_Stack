# Countdown
def countdown(input):
    print(input)
    l = []
    for i in range(input,-1,-1):
        print(i)
        l.append(i)
        print(l)
    return l
x = countdown(6)
print(x)

# Print and Return
def copy(num):
    print("Printed Inside the Function: ", num[0])
    return num[1]
y = copy([1,2])
print("What was Return from the Function: " + str(y))

# First plus Length
def plus(list):
    print(len(list))
    return list[0] + len(list)
argument = plus([1,2,3,4,5])
print(argument)

# Values Greater than Second
def list(values):
    print(values)
    if len(values) <= 2:
        return False
    new_list = []
    for f in values:
        if f < values[f]:
            pass
        elif f > values[f]:
            new_list.append(f)
    return new_list
w = list([5,2,3,2,1,4])
print(w)

# This Length, That Value
def this(num2,num3):
    print(num2, num3)
    new_list = []
    start = 0
    end = num2
    while start < end:
        new_list.append(num3)
        start = start + 1
    print(new_list)
    return new_list
r = this(4,7)
e = this(6,2)
print(r,e)