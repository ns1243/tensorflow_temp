#-*- coding: utf-8 -*-
#Learn_python3.py

#예제 12

def my_function(input_num):
    output_num = input_num + 1
    return output_num


a = my_function(1)

print (a)


#예제 13

def my_function(input_num):
    output_num = input_num + 1
    return output_num

print(my_function(1))


#예제 14
def add_function(input_value):
    a = 0
    for i in range (0,input_value):
        a = a + i
    return a

print(add_function(21))
print(add_function(31))
print(add_function(41))
print(add_function(51))


#예제 15
def add_function(start_value, end_value):
    a = 0
    for i in range (start_value,end_value):
        a = a + i
    return a

print(add_function(10,21))
print(add_function(20,31))
print(add_function(30,41))
print(add_function(40,51))


#예제 16
def add_function(start_value, end_value, even_only):
    a = 0
    for i in range (start_value,end_value):
        if(even_only):
            if(i % 2 ==0):
                a = a + i
        else:
            a = a + i
    return a

print(add_function(10,21, True))
print(add_function(10,21, False))
print(add_function(30,41, True))
print(add_function(30,41, False))

#예제 17
def add_function(start_value, end_value, even_only):
    a = 0
    for i in range (start_value,end_value):
        if(even_only):
            if(i % 2 ==0):
                a = a + i
        else:
            a = a + i
    print(a)

add_function(10,21, True)
add_function(10,21, False)
add_function(30,41, True)
add_function(30,41, False)

#예제 18
def add_function(start_value, end_value, even_only):
    a = 0
    for i in range (start_value,end_value):
        if(even_only):
            if(i % 2 ==0):
                a = a + i
        else:
            a = a + i
    print(a)

a = add_function(10,21,True)
print("a is", a)

#예제 18
def add_function(start_value, end_value, even_only):
    a = 0
    for i in range (start_value,end_value):
        if(even_only):
            if(i % 2 ==0):
                a = a + i
        else:
            a = a + i
    print(a)

a = add_function(10,21,True)
print("a is", a)


#예제 19
def add_function(input_value):
    a = 0
    for i in range (0,input_value):
        a = a + i
    return a

    
print(add_function(add_function(10)))
print(add_function(add_function(20)))