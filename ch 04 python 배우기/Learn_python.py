#-*- coding: utf-8 -*-
#Learn_python.py

#예제 1
a = 1
b = 1.0
c = "1.000000000"
d = 12346789012345678901
e = 12345678901234567
f = 12333 + 14j


print (type(a))
print (type(b))
print (type(c))
print (type(d))
print (type(e))
print (type(f))


#예제 2
a = 1
b = 1.0
c = "1.000000000"

d = a + b
e = b + c
print (e)





#예제 3
a = 1
b = 1.0
c = "1.000000000"
c = float(c)

d = a + b
e = b + c
print (e)

# list형 자료
#예제 4
a = [ ]
b = [1, 2, 3, 4]
c = [1.0, 2.0, 3.0, 4.0]
print (a, type(a))
print (b[0])
print (c[-1])


#예제 5
a = [1,2,3,4,5]
b = [[1,2], [3,4]]
print (a[:])
print (a[0:2])
print (a[2:-1])
print (b[0:1])
