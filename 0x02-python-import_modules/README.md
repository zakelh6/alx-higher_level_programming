# Resources
Read or watch:

- [Modules](https://docs.python.org/3/tutorial/modules.html)
- [Command line arguments](https://intranet.alxswe.com/rltoken/5e3TphtJ6WSVkWsdd2eX_A)
- [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

# General
<details>
<summary>
Why Python programming is awesome
</summary>

Python programming is awesome for several reasons:

1. **Readability**: Python has a clean and easy-to-read syntax, making it simpler to write and understand code. It emphasizes code readability, which reduces the cost of program maintenance.

2. **Simplicity**: Python's simplicity enables beginners to quickly grasp the language and start coding. It emphasizes code clarity and avoids unnecessary complexity.

3. **Versatility**: Python can be used for a wide range of applications, such as web development, data analysis, artificial intelligence, scientific computing, automation, and more. It offers numerous libraries and frameworks to facilitate different tasks.

4. **Large Standard Library**: Python comes with a vast standard library that provides pre-built modules and functions for various tasks. It reduces the need to write code from scratch, making development faster and more efficient.

5. **Community** and Support: Python has a large and active community of developers who contribute to its growth. This results in extensive documentation, tutorials, forums, and resources available online, making it easier to learn and troubleshoot issues.
</details>

<details>
<summary>
How to import functions from another file
</summary>

1. Create a Python file containing the functions you want to import. For example, let's say the file is called `my_module.py`.

2. In the file where you want to use the functions, use the `import` statement followed by the name of the module (file) without the `.py` extension. For example, `import my_module`.

3. To use a specific function from the module, you can either call it directly using the syntax `module_name.function_name()` or import the function directly using the `from` statement. For example, `from my_module import my_function`
</details>

<details>
<summary>
How to use imported functions
</summary>
</details>

<details>
<summary>
How to create a module
</summary>


To create a module:

1. Create a Python file containing the functions, classes, or variables you want to include in the module.

2. Save the file with a `.py` extension and choose a descriptive name for the module.

3. In other Python files, you can import this module using the `import` statement as described earlier.

</details>

<details>
<summary>
How to use the built-in function `dir()`
</summary>


To use the built-in function `dir()`:

The `dir()` function in Python returns a list of names in the current local scope or a list of attributes and methods of an object if an object is provided as an argument. It is used to explore the properties and methods available for an object or module.
</details>


<details>
<summary>
How to prevent code in your script from being executed when imported
</summary>


To prevent code in your script from being executed when imported:

When writing a Python script, you may have some lines of code that you only want to execute when running the script directly and not when the script is imported as a module. To achieve this, you can use the following code structure:

```python
if __name__ == "__main__":
    # Code to be executed only when running the script directly
```
The `__name__` variable is set to `"__main__"` when the script is executed directly, but it is set to the module name when the script is imported. By checking if `__name__` is equal to `"__main__"`, you can ensure that the code block is executed only when running the script directly.
</details>

<details>
<summary>
How to use command line arguments with your Python program
</summary>

To use command line arguments with your Python program:

Python provides the `sys` module, which allows you to access command line arguments passed to your script. Here's an example:

```python
import sys

# Access command line arguments using sys.argv
# sys.argv[0] contains the script name
# sys.argv[1:] contains the command line arguments
arguments = sys.argv[1:]

# Process the command line arguments as needed
for arg in arguments:
    print(arg)
```

In this example, `sys.argv` is a list that holds the command line arguments. `sys.argv[0]` contains the script name, and `sys.argv[1:]` contains the additional command line arguments.

You can then process these arguments based on your script's requirements.
</details>
