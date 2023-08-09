Provide brief answers to the knowledge-question worksheet.

1. Briefly explain: what is modular programming

Modular programming is coding in manageable blocks (i.e. modules) and is important for software development as multiple developers can work on separate blocks or sections of code simultaneously. This is achieved by separating the functionality of a program into independent, interchangeable modules, such that each module contains everything necessary to execute only one aspect of the desired functionality, i.e. do one thing and do it well.

2. How can you import only a specific function or class from a module in Python? What is the syntax for this?

A module in Python is a file containing Python definitions and statements. Save your modular code (defined function e.g. def x()) as a .py file, e.g. module.py. Then import it to the program (i.e. import module_name) and call the module function as module_name.function.
For example:

import module.py

module.x(value) 

3. How would you explain Python's parameter-passing mechanism? Is it more similar to pass-by-value or pass-by-reference? Justify your answer.



4. Given the following Python code, what will be the output and why?

def modify_list(list_):
    list_.append("new")
    list_ = ["completely", "new"]

items = ["original"]
modify_list(items)
print(items)

Output is ['original', 'new']. modify_list function appends the item "new" to the list

5. In Python even though variables created within a function are local, there are still situations where you can modify data outside the scope with a local variable. Explain this anomaly and relate it to both mutability and pass by reference.



6. List two benefits of modular coding approaches. How do these benefits assist in the development of medium-sized applications?

Two benefits of modular programming is code reusability and readability, which allows for different modules to be developed, tested and maintained individually. It allows multiple developers to  work on different modules simultaneously, thus making software development of medium-sized applications more efficient and manageable.