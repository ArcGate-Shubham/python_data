# x = lambda a : a + 10
# print(x(5))

# x = lambda a,b,c,d : a+b*c+d
# print(x(1,2,3,4))

# a = [[3,4,6],[11,13,65],[95,25,11]]
# a.sort(key=lambda x :x[2])
# print(a)

a = [[3, 4, 6], [11, 13, 65], [95, 25, 11]]
a.remove(key=lambda x: x[2])
print(a)
