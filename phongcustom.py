from minitorch.scalar import Scalar


a = Scalar(10)
print(a)
print(a.__dict__)
b = a*a
print(b)

c = a*10