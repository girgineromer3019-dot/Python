

#Python f-Strings Example
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Comparison Example
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Arithmetic Operations Example
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#Python Lists Example
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#List removal example
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
for fruit in fruits:
    print(fruit)

#List comprehension example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "c" in x]
print(newlist)
output: ['cherry']

#List iterable example
newlist = [x for x in range(10) if x < 5]
print(newlist)
output: [0, 1, 2, 3, 4]

# my_module.py
def greet(name):
    return f"Hello, {name}!"

pi = 3.14159


class Calculator:
    def add(self, a, b):
        return a + b
