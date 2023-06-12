## Resources

**Read or watch:**

- [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (Read until “4.6. Defining Functions” included)
- [IndentationError](https://www.youtube.com/watch?v=1QXOd2ZQs-Q&ab_channel=ATOM)
- [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
- [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
- [Learn to Program 2 : Looping](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
- [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

General
  <details>
  <summary>
Why Python programming is awesome
      </summary>
  Python programming is considered awesome for several reasons:

1. **Readability:** Python uses a clean and straightforward syntax, making it easy to read and understand. It emphasizes code readability, allowing developers to write clear and concise code.

2. **Ease of Use:** Python has a gentle learning curve, making it accessible for beginners. Its simplicity and readability contribute to its ease of use.

3. **Versatility:** Python is a versatile programming language that can be used for a wide range of applications, including web development, data analysis, machine learning, scientific computing, automation, and more. It has a vast collection of libraries and frameworks that support various domains.

4. **Large and Active Community:** Python has a large and active community of developers worldwide. This vibrant community contributes to the development of libraries, frameworks, and resources, making it easier to find solutions and get support.

5. **Portability:** Python is a cross-platform language, meaning you can run Python code on different operating systems, including Windows, macOS, and Linux, without making significant changes to the code.

6. **Integration:** Python can be easily integrated with other programming languages, allowing developers to leverage existing code and tools.
    </details>
  <details>
  <summary>
Why indentation is so important in Python
        </summary>
Indentation plays a crucial role in Python because it defines the structure and hierarchy of the code. In Python, indentation is used to indicate blocks of code (such as loops, functions, and conditional statements) and their nesting levels.

The Python interpreter uses indentation to understand the logical structure of the code. Blocks of code with the same indentation level are considered part of the same block. Incorrect indentation can lead to syntax errors or alter the program's logic.

Unlike other programming languages that use braces or keywords to delimit blocks of code, Python uses indentation as a visual indicator. This feature enhances code readability and enforces consistent formatting practices among developers.
  </details>

  <details>
  <summary>
How to use the if, if ... else statements
        </summary>
In Python, the `if` statement is used to perform conditional execution of code. It allows you to specify a condition, and if that condition is true, the associated block of code is executed. Optionally, you can include an `else` statement to specify a block of code to execute when the condition is false.

Here's an example of using the if statement:

```python
x = 10

if x > 0:
    print("x is positive")

# Output: x is positive
```

In this example, if the condition `x > 0` is true, the code inside the `if` block is executed, and the message "x is positive" is printed.

You can also use the `if ... else` statement to specify different blocks of code to execute based on the condition:

```python
x = 10

if x > 0:
  print("x is positive")
else:
  print("x is non-positive")

# Output: x is positive
  ```
In this case, if the condition x > 0 is true, the code inside the if block is executed. Otherwise, the code inside the else block is executed.

  </details>

  <details>
  <summary>
How to use comments
   </summary>
Comments in Python are used to add explanatory notes or annotations to the code. They are ignored by the interpreter and do not affect the program's execution. Comments help in understanding the code, making it more readable and maintainable.
<br>
In Python, you can use two types of comments:

- **Single-line comments:** Single-line comments begin with a hash symbol *(`#`)* and continue until the end of the line. Anything after the hash symbol on the same line is considered a comment.
  
  ```python
  # This is a single-line comment
  ```

- Multi-line comments: Multi-line comments are enclosed within triple quotes (""" or '''). They can span multiple lines and are commonly used for documenting functions, classes, or larger code sections.

  ```python
  """
  This is a multi-line comment.
  It can span multiple lines.
  """
  ```
It's good practice to add comments to explain complex sections of code, provide context, or document your code's purpose and behavior.

  </details>

  <details>
  <summary>
How to affect values to variables
  </summary>
In Python, you can assign values to variables using the assignment operator (=). The variable on the left side of the operator receives the value on the right side. Here's an example:
  
```python
x = 10  # Assigns the value 10 to the variable x
```

In this example, the variable x is assigned the value 10.

You can assign different types of values to variables, including numbers, strings, booleans, lists, and more. Python is a dynamically typed language, meaning you don't need to declare the variable's type explicitly.

```python
name = "Alice"  # Assigns a string value to the variable name
is_active = True  # Assigns a boolean value to the variable is_active
numbers = [1, 2, 3, 4, 5]  # Assigns a list of numbers to the variable numbers
```
  </details>

  <details>
  <summary>
How to use the while and for loops
  </summary>

In Python, you can use the `while` and `for` loops to iterate over a sequence of elements or repeat a block of code.

The `while` loop executes a block of code repeatedly as long as a specified condition is true. Here's an example:

```python
count = 0

while count < 5:
    print(count)
    count += 1

# Output: 0 1 2 3 4
```
In this example, the loop prints the value of `count` and increments it by 1 until `count` is no longer less than 5.

The `for` loop is used to iterate over a sequence of elements, such as a list, string, or range. Here is an example:

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

# Output: apple banana orange
```

In this example, the loop iterates over each element in the `fruits` list and prints it.


  </details>

  <details>
  <summary>
How is Python’s for different from C‘s?
  </summary>
In Python, the `for` loop works differently from C's `for` loop. In C, the `for` loop is typically used for iterating over a range of values defined by an initial value, a condition, and an increment or decrement. The loop control is more explicit.

In Python, the `for` loop is more flexible and powerful. It is used to iterate over a sequence of elements, such as a list, string, or range, without requiring explicit control variables or defining the loop range. The loop variable automatically takes the value of each element in the sequence, one by one, until the sequence is exhausted.

Python's `for` loop abstracts away the lower-level details of iterating over a range of values, providing a simpler and more intuitive syntax for iterating over sequences.
  </details>
How to use the break and continues statements
How to use else clauses on loops
What does the pass statement do, and when to use it
How to use range
What is a function and how do you use functions
What does return a function that does not use any return statement
Scope of variables
What’s a traceback
What are the arithmetic operators and how to use them
