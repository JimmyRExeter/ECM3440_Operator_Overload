# Python operator overloading

## Exercises

Rational numbers, often called fractions, are numbers that can be written as two integers in the form a/b such as 1/3, 1/8.

To complete this exercise study the files ```rational.py```, ```test_rational.py```, and ```rational_demo.py``` In these you will find the definition of the class ```Rational```, some unit tests, and a sample program using the ```Rational``` number class.

Unfortunately the ```Rational``` class is incomplete, with no implementation of subtraction.

Another fault in the implementation is that conversion of rational numbers to strings yields text such as "1.0/2.0" rather than "1/2".


```py
from rational import Rational

a = Rational(1, 2)
b = Rational(1, 8)
print("Add two rational numbers")
print(f"{a} + {b} = {a+b}")

print()
print("Subtract one rational number from another")
print(f"{a} - {b} = {a-b}")
```

Running the above code in the Python3 interpreter gives the following output.

```txt
Add two rational numbers
1.0/2.0 + 1.0/8.0 = 5.0/8.0

Subtract one rational number from another
Traceback (most recent call last):
  File "rational-demo.py", line 18, in <module>
    print(f"{a} - {b} = {a-b}")
TypeError: unsupported operand type(s) for -: 'Rational' and 'Rational'
```

Ideally the output should be.

```txt
Add two rational numbers
1/2 + 1/8 = 5/8

Subtract one rational number from another
1/2 - 1/8 = 3/8
```

Exercise 1. Implement the subtract function and appropriate unit tests.

Exercise 2. Improve the ```__str__``` method to give values such as 1/3 rather than 1.0/3.0

Exercise 3. Can you implement support for operations that mix rational numbers with integers? e.g. 1 + Rational(1, 3)


## Example code

This exercise is based on example code from the book -

Lambert, K. 2018. . Fundamentals of Python: First Programs. Cengage Learning.

<https://lambertk.academic.wlu.edu/publications/python-programming/fundamentals-of-python/>


## Arithmetic operators

See <https://docs.python.org/3/library/operator.html> for the full list of operators.

| operator | method |
| -------- | ------ |
| ```+``` |  ```__add__``` |
| ```-``` |  ```__sub__``` |
| ```*``` |  ```__mul__``` |
| ```/``` |  ```__div__``` |
| ```%%``` |  ```__mod__``` |

## Comparison operators

| operator | method |
| -------- | ------ |
| ```==``` | ```__eq__``` |
| ```!=``` | ```__ne__``` |
| ```<``` | ```__lt__``` |
| ```<=``` | ```__le__``` |
| ```>``` | ```__gt__``` |
| ```>=``` | ```__ge__``` |