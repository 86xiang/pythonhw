import math
a = eval(input("请输入a边长："))
b = eval(input("请输入b边长："))
c = eval(input("请输入c边长："))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("三角形的面积是{:.2f}".format(s))
