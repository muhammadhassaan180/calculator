'''calculator consisting of seven functions:
   add,sub,multiply,divide,power,modulus and floor_div'''
def add(no1, no2):
    print('sum of given numbers: ',end='')
    return no1+no2

def sub(no1, no2):
    print('substraction of given numbers: ',end='')
    return no1-no2

def multiply(no1, no2):
    print('multiplication of given numbers: ',end='')
    return no1*no2

def divide(no1, no2):
    print('division of given numbers: ',end='')
    return no1/no2

def power(no1, no2):
    print('exponent of given numbers: ',end='')
    return no1**no2

def modulus(no1, no2):
    print('modulus of given numbers: ',end='')
    return no1%no2

def floor_div(no1, no2):
    print('floor division of given numbers: ',end='')
    return no1//no2

print('\t\t==========\n\t\tCALCULATOR\n\t\t==========')#Heading

input1 = int(input('Enter first number: '))
input2 = int(input('Enter second number: '))

#prints all mathematical operations
print(add(input1, input2))
print(sub(input1, input2))
print(multiply(input1, input2))
print(divide(input1, input2))
print(power(input1, input2))
print(modulus(input1, input2))
print(floor_div(input1, input2))
