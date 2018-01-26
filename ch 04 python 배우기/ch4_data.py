a = 1
b = 1.0
c = "1.000000000"
c = float(c)

print (type(a))
print (type(b))
print (type(c))
# d = a + b
# e = b + c
# print (e)

c = a  +  b
print ("adding value =", c)
c = a * b
print ("multiplying values = ", c)

print (" dividing value =", a/b )
print ("  subtracting values =", a - b)


a = 0
for i in range (0,50):
    a = i +a
print ("when values is added from 0 to 50", a)

a = ""
for i in range (0,50):
    a = i

print ("last value is ", a)


a = ""
for i in range (0,50):
    b = 0
    a = a + str(i) + " "
    c = 0
    e = 0
    f = 0

print ("when values are added form 0 to 50 ", a)


a = 0
b = 0
for i in range (0,50):
    a = 2 + a
b = 2 + b
print ("when 2 is added 50 times, a =", a, " b =", b)



a = 0
for i in range (0,50):
    if (i % 2 == 0):
        a = 2 + a
print ("when 2 is added 50 times, a =", a)

a = 0
for i in range (0,50):
    if (i % 2 == 0):
        a = 2 + a
    else:
        a = 1 +a
print ("when 2 is added 50 times, a =", a)

처리방법 = 0
출력형태 = 0




def add_function( input_value ):
    for i in range (0,50):
        input_value = input_value + 2
    return input_value



a = add_function(0)
print ("when input is 0, output is ", a)

b = add_function(20)
print ("when input is 20, output is", b)

c = add_function(30)
print ("when input is 30, output is ", c)

def add_function2( input_value, to_value ):
    for i in range (0,to_value):
        input_value = input_value + 2
        return input_value

a = add_function2(0, 50)
print ("function2 is", a)

def add_function3( input_value, to_value, add_value ):
    for i in range (0,to_value):
        input_value = input_value + add_value
    return input_value

a = add_function3(0, 50, 2)
print ("function2 is", a)




class Adder:
    def __init__(self, to_value_input, add_value_input):
        self.to_value = to_value_input
        self.add_value = add_value_input

    def run(self, input_value):
        for i in range(0, self.to_value):
            input_value = input_value + self.add_value
        return input_value


add_1 = Adder(40,2)
add_2 = Adder(30,1)
add_3 = Adder(50,5)


a= add_1.run(100)
print ("add_3 output is ", a)

b  = add_2.run(150)
print ("add_2 output is ", b)

c = add_3.run(200)
print ("add_3 output is ", c)

a= add_1.run(100)
print ("add_3 output is ", a)
add_1.print(100)


class Adder:
    def __init__(self, to_value_input, add_value_input):
        self.to_value = to_value_input
        self.add_value = add_value_input

    def run(self, input_value):
        for i in range(0, self.to_value):
            input_value = input_value + self.add_value
        return input_value

    def print(self, input_value):
        for i in range(0, self.to_value):
            input_value = input_value + self.add_value
        print("output value is ",input_value)


add_1 = Adder(40, 2)
add_1.print(100)
print ("add_1's add_value is ", add_1.add_value)

from ch4_reference import Adder_copy
from ch4_reference import add_function_copy

adder_new = Adder_copy(50,2)
adder_new.print(20)
a =  add_function_copy(50,2)
#a = adder_new(20)
#a = ch4_reference.add_function_copy(2,50)
print (" referenced function ", a)

#add_new = ch4_reference.Adder_copy(40,2)
#add_new.print(100)

#
#
# print (type(a), type(b), type(c))
#
# print ("a type is", type(a), "b type is ", type(b), "c type is ", type(c))


#
# print (a + b)
# print (a * b)
# print (a - b)
# print (a * b)
#




# c = "type a="
# d = "type b="
# print (c, type(a))
# print (d, type(b))

