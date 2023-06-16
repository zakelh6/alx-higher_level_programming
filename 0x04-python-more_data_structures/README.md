0x04. Python - More Data Structures: Set, Dictionary

Read or watch:

- [Data structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Lambda, filter, reduce and map](https://python-course.eu/advanced-python/lambda-filter-reduce-map.php)
- [Learn to Program 12 Lambda Map Filter Reduce](https://www.youtube.com/watch?v=1GAC6KQUPeg)

General

<details>
<summary>
Why Python programming is awesome
</summary>
Python programming is considered awesome for several reasons. First, it has a simple and readable syntax, making it easy to understand and write code quickly. Python's extensive standard library and large community of developers contribute to its versatility, providing numerous pre-built modules and packages for various tasks. Python is also known for its strong support for integration with other languages and platforms. It is widely used in fields such as web development, data analysis, machine learning, and automation, making it a popular choice among programmers.
</details>

<details>
<summary>
What are sets and how to use them
</summary>
In Python, a set is an unordered collection of unique elements. It is denoted by curly braces ({}) or by using the `set()` function. Sets can store any hashable objects such as numbers, strings, or tuples. Duplicates are automatically removed from a set, and the order of elements is not guaranteed.

To use sets, you can create a set by enclosing comma-separated values within curly braces or by using the set() function. For example:

```python
my_set = {1, 2, 3}  # Creating a set directly
another_set = set([4, 5, 6])  # Creating a set using set() function
```

You can perform various operations on sets, such as adding elements, removing elements, checking membership, performing set operations (union, intersection, difference), and more.


</details>

<details>
<summary>
What are the most common methods of set and how to use them
</summary>
- `add(element)`: Adds an element to the set.
- `remove(element)`: Removes the specified element from the set. Raises an error if the element doesn't exist.
- `discard(element)`: Removes the specified element from the set, if it exists. Doesn't raise an error if the element is not found.
- `pop()`: Removes and returns an arbitrary element from the set.
- `clear()`: Removes all elements from the set.
- `copy()`: Returns a shallow copy of the set.
- `union(other_set)`: Returns a new set that is the union of the current set and the other set.
- `intersection(other_set)`: Returns a new set that is the intersection of the current set and the other set.
- `difference(other_set)`: Returns a new set that contains the elements of the current set not present in the other set.

Here's an example of using some of these methods:

```python
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}
```
</details>

<details>
<summary>
When to use sets versus lists
</summary>
Sets and lists serve different purposes, so their usage depends on the specific requirements of your program.

- Use sets when you want to store a collection of unique elements and order doesn't matter. Sets provide fast membership testing, making it efficient to check if an element exists in a set. They are also useful when you need to perform set operations such as union, intersection, or difference between multiple sets.

- On the other hand, use lists when you need to preserve the order of elements and allow duplicates. Lists are more appropriate for situations where you require sequential access to elements or need to maintain the order in which elements were added.
</details>


<details>
<summary>
How to iterate into a set
</summary>
To iterate over a set in Python, you can use a for loop. The loop will iterate over each element in the set, and you can perform operations on them.

Here's an example of iterating over a set:

```python
my_set = {1, 2, 3}
for element in my_set:
    print(element)

# 1
# 2
# 3
```
</details>

<details>
<summary>
What are dictionaries and how to use them
</summary>

In Python, a dictionary is an unordered collection of key-value pairs. It is also known as an associative array or a hash map. Dictionaries are denoted by curly braces ({}) and consist of comma-separated key-value pairs.

To use dictionaries, you can create one by enclosing key-value pairs within curly braces or by using the dict() function. Keys in a dictionary must be unique and immutable (such as strings, numbers, or tuples), while values can be of any type.

Here's an example of a dictionary:

```python
my_dict = {"name": "John", "age": 30, "city": "New York"}
```

You can access values in a dictionary using the corresponding key. For example, `my_dict["name"]` will return the value `"John"`. You can also modify, add, or remove key-value pairs in a dictionary using various methods.

</details>

<details>
<summary>
When to use dictionaries versus lists or sets
</summary>
Dictionaries, lists, and sets have different use cases:

- Use dictionaries when you want to store and retrieve values based on a unique key. Dictionaries provide fast lookup based on keys, making them suitable for scenarios where you need to associate data with specific identifiers or perform key-based operations.

- Use lists when you need to maintain an ordered collection of elements. Lists are useful when you want to access elements by their index or when the order of elements is crucial.

- Use sets when you want to store a collection of unique elements and order doesn't matter. Sets are beneficial when you need to perform membership tests or set operations efficiently.
</details>

<details>
<summary>
What is a key in a dictionary
</summary>
n a dictionary, a key is a unique and immutable object used to identify and access a corresponding value. Keys can be strings, numbers, or tuples, among other immutable types. Each key in a dictionary must be unique, and it acts as a label or identifier for the associated value.

For example, in the dictionary `{"name": "John", "age": 30}`, `"name"` and `"age"` are the keys, and `"John"` and `30` are the corresponding values.
</details>

<details>
<summary>
How to iterate over a dictionary
</summary>
To iterate over a dictionary in Python, you can use a for loop. The loop iterates over each key in the dictionary, and you can access the associated value using the key.

Here's an example of iterating over a dictionary:
```python
my_dict = {"name": "John", "age": 30, "city": "New York"}
for key in my_dict:
    value = my_dict[key]
    print(key, value)
```

output:
```
name John
age 30
city New York
```

Alternatively, you can use the items() method of a dictionary to iterate over both keys and values simultaneously.

</details>

<details>
<summary>
What is a lambda function
</summary>
In Python, a lambda function is an anonymous function that can be defined without a name. It is a way to create small, one-line functions without the need for a formal `def` statement. Lambda functions are typically used for simple and concise operations.

The syntax for a lambda function is:
```python
lambda arguments: expression
```

Here's an example of a lambda function that adds two numbers:

```python
add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8
```
Lambda functions are often used in conjunction with higher-order functions like `map()`, `reduce()`, and `filter()`.
</details>

<details>
<summary>
What are the map, reduce and filter functions
</summary>
These are built-in functions in Python that operate on iterables like lists, sets, or dictionaries.

- `map(function, iterable)`: Applies a given function to each element in the iterable and returns an iterator with the results. For example:
```python
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]
```
- `reduce(function, iterable)`: Applies a given function to the first two elements of the iterable, then applies it to the result and the next element, and so on, until a single value is obtained. Requires the `functools` module in Python 3. For example:

```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
```

- `filter(function, iterable)`: Applies a given function to each element in the iterable and returns an iterator with the elements for which the function returns `True`. For example:

```python
numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4]
```
These functions provide a concise and functional programming style in Python, allowing you to perform operations on data more elegantly.
</details>