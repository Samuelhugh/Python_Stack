class Mathdojo:

    def __init__(self):
        self.result = 0

    def add(self, *num):
        for i in range(len(num)):
            self.result += num[i]
            # print(self.result)
        return self


    def subtract(self, *num):
        for j in range(len(num)):
            self.result -= num[j]
            # print(self.result)
        return self

# Instances
md = Mathdojo()
mdd = Mathdojo()

# Invoking or Calling my Methods
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
y = mdd.add(1).add(1, 4, 0).subtract(2, 1).result
print(x)
print(y)