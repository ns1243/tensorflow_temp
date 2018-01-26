#-*- coding: utf-8 -*-
#Learn_python2.py

#예제 6
a = 1
b = 2.0
c = a  +  b
# 부분 1
print ("adding value =", c)
c = a * b
print ("multiplying values = ", c)
# 부분 2
print (" dividing value =", a/b )
print ("  subtracting values =", a - b)


# 예제 7

#part 1
a = 0
for i in range (50):
    a = i +a
print ("when values is added from 0 to 50", a)

#part 2
a = 0
for i in range (0, 50):
    a = i +a
print ("when values is added from 0 to 50", a)

#part 3
a = 0
for i in range (10, 50):
    a = i +a
print ("when values is added from 10 to 50", a)



# 예제 8
#part1
a,b = 0,0

for i in range (0,50):
    a = i
    b = b + a

print ("last value is ", a)
print ("added sum is ", b)

#part2
a = ""
for i in range (0,50):
    a = a + str(i) + " "
print ("when values are listed form 0 to 50 ", a)


# 예제 9
a = 0
b = 0
c = 0 
for i in range (0,50,2):
    a = 2 + a
    b = b + 1 
c = 2 + c

print ("when value is added, a =", a)
print (b, "th time is added! ")
print ("value c is ", c)


# 예제 10
a = 0
b = 0
c = 0
for i in range (0,50):
    a = a + 1
    if (i % 2 == 0):
        b = 2 + b
        c = 1 + c 

print ("when 1 is added 50 times, a =" , a)
print ("when 2 is added",c," times, b is", b ) 


# 예제 11

a = 0
for i in range (50):
    if (i % 2 == 0):
        a = 2 + a
    else:
        a = 1 +a
print ("a sum =", a)




