# # Countdown
# def countdown(input):
#     print(input)
#     l = []
#     for i in range(input,0,-1):
#         print(i)
#         l.append(i)
#         print(l)
#     return l
# x = countdown(6)
# print(x)

# # Print and Return
# def copy(num):
#     print(num)
#     print(num[0])
#     return num[1]
# y = copy([1,2])
# print(y)

# #First plus Length
# def plus(num1):
#     print(num1)
#     num1[0] += len(num1)
#     return num1[0]
# o = plus([1,2,3])
# print(o)

# #Values Greater than Second
# def list(Values):
#     print(Values)
#     k = 5
#     count = 0
#     m = []
#     for f in Values:
#         print(f)
#         if f > k:
#             count = count + 1
#             m.append(f)
#     print(count)
#     if count == 2:
#         return count,m,'false'
# w = list([1,3,5,7,9])
# print(w)

# # This Length, That Value
# def this(num2,num3):
#     print(num2, num3)
#     q = []
#     start = 0
#     end = num2
#     while start < end:
#         q.append(num3)
#         start = start + 1
#     print(q)
#     return q
# r = this(4,7)
# e = this(6,2)
# print(r,e)