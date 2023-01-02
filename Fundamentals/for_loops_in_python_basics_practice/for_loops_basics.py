# Various ways to Define For Loops in Python
# 0 is Implied if not Specified
for x in range(0,151):
    print(x)

for y in range(5,1001,5):
    print(y)

for a in range(1,101):
    if a % 10 == 0:
        print("Coding Dojo")
    elif a % 5 == 0:
        print("Coding")

# If a Step is not Implied then 1 will be the Default Step
sum = 0
for j in range(500001):
    if j % 2 != 0:
        sum += j
print(sum)

for d in range(2018,-1,-4):
    print(d)

low_num = 2
high_num = 9
mult = 3
for f in range(low_num,high_num):
    if f % mult == 0:
        print(f)