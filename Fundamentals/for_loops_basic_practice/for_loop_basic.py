for x in range(151):
    print(x)

for y in range(5,1005,5):
    print(y)

for a in range(1,101):
    if a % 10 == 0:
        print("Coding")
    elif a % 5 == 0:
        print("Coding Dojo")
    else:
        print(a)

sum = 0
for j in range(0,500001,1):
    if j % 2 == 1:
        sum += j
        print(sum)

for d in range(2018,0,-4):
    if d % 2 == 0:
        print(d)

lowNum = 2
highNum = 9
mult = 3
for f in range(lowNum,10):
    if f % mult == 0:
        print(f)