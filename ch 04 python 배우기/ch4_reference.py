class Adder_copy:
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



def add_function_copy( input_value, to_value ):
    for i in range (0,to_value):
        input_value = input_value + 2
        return input_value



def add_function_copy1( input_value, to_value ):
    for i in range (0,to_value):
        input_value = input_value + 2
        return input_value