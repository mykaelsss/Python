num1 = 42
"""
variable declaration
data types
primitive
numbers
interger
"""
num2 = 2.3
"""
variable declaration
data types
primitive
numbers
float
"""
boolean = True
"""
variable declaration
data types
primitive
boolean
"""
string = 'Hello World'
"""
variable declaration
data types
primitive
strings
"""
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
"""
variable declaration
data types
composite
list
"""
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
"""
variable declaration
data types
composite
dictionary
"""
fruit = ('blueberry', 'strawberry', 'banana')
"""
variable declaration
data types
composite
tuple
"""
print(type(fruit))
"""
log statement
type check
data type
compostie
access value
"""
print(pizza_toppings[1])
"""
log statement
data type
compostie
list
access value
"""
pizza_toppings.append('Mushrooms')
"""
log statement
data type
compostie
list
add value
"""
print(person['name'])
"""
log statement
data type
compostie
dictionary
access value
"""
person['name'] = 'George'
"""
log statement
data type
compostie
dictionary
change value
"""
person['eye_color'] = 'blue'
"""
log statement
data type
compostie
dictionary
access value
"""
print(fruit[2])
"""
log statement
data type
compostie
tuple
access value
"""
if num1 > 45:
        """
        condiotional
        if
        """
        print("It's greater")
    #log statement
else:
        """
        condiotional
        else
        """
        print("It's lower")
#log statement
if len(string) < 5:
    """
    length check
    condiontional
    if
    data type
    number
    int
    """
    print("It's a short word!")
    #log statement
elif len(string) > 15:
    """
    variable delcaration
    length check
    condiontional
    else if
    data type
    number
    int
    """
    print("It's a long word!")
    #log statement
else:
        """
        condiotional
        else
        """
        print("Just right!")
    #log statement
for x in range(5):
    """
    variable declaration
    for loop
    """
    print(x)
        #log statement
for x in range(2,5):
    """
    variable declaration
    for loop
    """
    print(x)
    #log statement
for x in range(2,10,3):
    """
    variable declaration
    for loop
    """
    print(x)
    #log statement
x = 0
#variable declaration
while(x < 5):
    #while loop
    print(x)
    #log statement
    x += 1
    # variable declaration

pizza_toppings.pop()
"""
composite
List
delete value
"""
pizza_toppings.pop(1)
"""
composite
List
access value
delete value
"""

print(person)
"""
log statment
data type
composite
access value
"""
person.pop('eye_color')
"""
data type
composite
access value
delete value
"""
print(person)
"""
log statment
data type
composite
access value
"""
for topping in pizza_toppings:
    #for loop
    if topping == 'Pepperoni':
        """
        condiotional
        if
        """
        continue
        """
        for loop
        continue
        """
    print('After 1st if statement')
    #log statement
    if topping == 'Olives':
        break
        """
        for loop
        break
        """

def print_hello_ten_times():
    #function
    for num in range(10):
        """
        for loop
        declaring variable
        """
        print('Hello')
        #log statement
print_hello_ten_times()
"""
function
log statement
"""
def print_hello_x_times(x):
    """
    function
    parameter
    """
    for num in range(x):
        """
    for loop
    varible declaration
    """
        print('Hello')
        #log statement
print_hello_x_times(4)
"""
function
parameter
log statement
"""
def print_hello_x_or_ten_times(x = 10):
    """
    function
    parameter
    """
    for num in range(x):
        """
        for loop
        variable declaration
        """
        print('Hello')

print_hello_x_or_ten_times()
"""
function
log statement
"""
print_hello_x_or_ten_times(4)
"""
function
parameter
log statement
"""

"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
