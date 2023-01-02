"""
First - Step through my Code in the order that it runs and check for any Unknowns.
Second - Use T-diagrams and Print statements to help visualize the Information and Predict the Code.
Third - My usual starter Unknowns would be what is my Input and what am I expecting as an Output. If I get unexpected results, I should work to eliminate the Unknowns. Also its useful to insert a Print statement in my Code just to make sure it is executing when I am expecting it to.
Fourth - Use Print statements to find out where an Error is occurring, Once discovered make an educated guess for what I should be Searching for.
"""
# def multiply(num_list, num):
#     print(num_list, num)
#     for x in num_list:
#         print(x)
#         x *= num
#         print(x)
#         print(num_list)
#     return num_list, x
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# # output: >>>[2,4,10,16]

# Revised Function Block
def multiply(num_list,num):
    print(num_list, num)
    for x in range(len(num_list)):
        print(x)
        num_list[x] *= num
        print(num_list)
    return num_list
# Variables or Arguments
a = [2,4,10,16]
# Assigning whatever Value comes back from the Function to this Variable
b = multiply(a,5)
# Printing the Value to the Console
print(b)
# output: >>>[10,20,50,80]