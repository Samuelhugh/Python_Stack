# Creating and Defining the Class (PascalCased)
class MathDojo:

    def __init__(self):
        self.result = 0
# Using Splat Operator
    def add(self, arg_one, *args):
        self.result += arg_one + sum(args)
        print("RESULT: ", self.result)
        return self

# Using Splat Operator
    def subtract(self, arg_one, *args):
        self.result -= arg_one + sum(args)
        print(self.result)
        return self

# Instances
math_done = MathDojo()
math_done_two = MathDojo()

# Invoking or Calling my Methods (Testing)
x = math_done.add(2).add(2,5,1).subtract(3,2).result
y = math_done_two.add(3,5).result
print(x)
print(y)