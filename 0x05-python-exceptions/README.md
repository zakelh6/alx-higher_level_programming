# 0x05. Python - Exceptions

## Resources

Read or watch:

- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Learn to Program 11 Static & Exception Handling](https://intranet.alxswe.com/rltoken/xASzXarhF1sBhzYkJ14LvQ) (starting at minute 7)

## General

<details>
<summary>
What’s the difference between errors and exceptions
</summary>

In Python, **errors** and **exceptions** are related but have distinct meanings.

- **Errors** in Python generally refer to syntax errors or logical errors that occur during the interpretation of the code. These errors prevent the program from running correctly and typically need to be fixed before the code can be executed.

- **Exceptions**, on the other hand, are events that occur during the execution of a program that disrupt the normal flow of the code. They are used to handle various types of exceptional or error conditions that may arise while the program is running.
</details>

<details>
<summary>
What are exceptions and how to use them
</summary>
Exceptions provide a way to handle runtime errors gracefully and prevent the program from abruptly terminating. They allow you to catch and handle specific types of errors, perform necessary actions, and continue with the execution of the program.
</details>

<details>
<summary>
When do we need to use exceptions
</summary>

To use exceptions in Python, you need to use a try-except block. The code that may potentially raise an exception is placed within the try block, and if an exception occurs, it is caught by an except block. The except block specifies the type of exception it can handle, and you can include multiple except blocks to handle different types of exceptions.

Here's an example of using a try-except block to catch a specific exception:

```python
try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Handle the ZeroDivisionError
    print("Error: Division by zero occurred.")
```
</details>


<details>
<summary>
How to correctly handle an exception

</summary>
To handle an exception correctly, you can perform error handling tasks such as displaying an error message, logging the error, or taking alternative actions. You can also raise exceptions yourself using the raise keyword to indicate that an error condition has occurred.
</details>

<details>
<summary>
What’s the purpose of catching exceptions
</summary>
Catching exceptions serves the purpose of preventing the program from crashing and allows you to handle exceptional situations gracefully. By catching and handling exceptions, you can take appropriate actions, provide meaningful error messages to the users, or recover from errors and continue with the execution.
</details>


<details>
<summary>
How to raise a builtin exception
</summary>

To raise a built-in exception, you can use the raise keyword followed by the exception type. For example:

```python
raise ValueError("Invalid value entered.")
```
</details>


<details>
<summary>
When do we need to implement a clean-up action after an exception
</summary>
Implementing a clean-up action after an exception is needed when you want to ensure that certain operations are performed regardless of whether an exception occurred or not. You can use the finally block, which is executed after the try and except blocks, to implement the clean-up action. This ensures that the clean-up code runs even if an exception was raised.

```python
try:
    # Code that may raise an exception
    file = open("example.txt", "r")
    # Perform some operations with the file
except FileNotFoundError:
    # Handle the FileNotFoundError
    print("Error: File not found.")
finally:
    # Clean-up action to close the file
    file.close()
```

In the above example, the finally block ensures that the file is closed, regardless of whether an exception occurred or not.

Handling exceptions and implementing clean-up actions are crucial for maintaining the stability and reliability of your program, especially when dealing with external resources like files or network connections.

</details>