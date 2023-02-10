a = "Hello World"
d={}
for char in set(a):
    d[char]=a.count(char)
print(d)