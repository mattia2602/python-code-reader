# Create a new trigger for a new construct

Currently, the constructs that the [parser.py](./files/parser.py) file offers are those declared in [implementations.md](./implementations.md).

To create a new trigger related to a construct not yet managed in [parser.py](./files/parser.py) the steps are quite standard and can be summarized in the following steps:

# Identify which methods of the Python 'ast' library make up the construct
The 'ast' library used in [parser.py](./files/parser.py) offers a wide variety of methods for handling Python language constructs, so that much work is done directly from the library without having to add additional changes.

Let's take a practical example: we want to implement the trigger on the 'continue' statement in Python

In this step we simply need to identify if a method already exists in the 'ast' library that allows us to identify when the 'continue' instruction is used in a program --> in our case the method exists and is called as "ast.Continue" .

# Define a function to handle the construct trigger

Now it is necessary that a new function be inserted inside the [parser.py](./files/parser.py) file, which will manage the trigger and the actions to be performed once the construct of interest in the our program.

Again going back to our example program: it can be seen that all the trigger functions have the prefix name "visit_", followed by the name of the construct, so in this case, the name of the function we are going to define will be "visit_Continue".

   ```python
 
   def visit_Continue(self, code):
    global parsing_trace
    if isinstance(node.value, ast.Continue):
      parsing_trace += "continue statement. \n"
    
   ```
 
After recalling the global variable which takes care of containing all the "long comment" which will then be read by the screen reader, we are going to use "isinstance" of the 'ast' library to ask ourselves if the current node of our code can be traced back to the construct " continue" of the Python language, if so, we insert in the global variable what we want the screen reader to read when it encounters this instruction.

# Insert the new function in the search of the expressions

To have greater certainty that our instruction is "translated" correctly, it is necessary to place a call to our function inside "visit_Expr", as it may happen that our instruction is a component of an expression inside our code, therefore it is first necessary to divide the expression into more basic blocks, so that each of them can be known by its own trigger.

It is therefore necessary to look in [parser.py](./files/parser.py) for the line of code relating to the beginning of the "visit_Expr" function and call our function, in this case always "visit_Continue"

```python
def visit_Expr(self, node):
     # Code present in file...
     elif isinstance(node,ast.continued):
         visitor.visit_Continue(node)
     #other code...
```

Therefore, if the expression is also composed of a "continue" construct, it is recognized and managed by its specific function.

Now our program [parser.py](./files/parser.py) is able to do advanced parsing of a "continue" statement :)
