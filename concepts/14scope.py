
# Scope

'''
A variable is only available from inside the region it is created. This is called scope.
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
A variable created in the main body of the Python code is a global variable and belongs to the global scope.
Global variables are available from within any scope, global and local.
'''

x = 10  # global var


def func():
    x = 5  # local
    print("In func:", x)


func()
print("outside:", x)

# To access global var in function

a = 20


def new():
    global a
    a = 30
    print("in func: ", a)


new()
print("outside:", a)

# But this way we can't create local var with same name in this function because it will be using global only.

z = 35
print(id(z))


def new_fun():

    z = 9
    res = globals()['z']  # get address of global var
    print(id(res))

    globals()['z'] = 70
    print('in fun:', z)


new_fun()
print("out:", z)


# nonlocal
'''
The keyword nonlocal is designed to indicate that a variable within a function that is inside a function, 
i.e., a nested function is just not local to it, implying that it is located in the outer function. 
We must define a non-local parameter with nonlocal if we ever need to change its value under a nested function. 
Otherwise, the nested function creates a local variable using that title. 
The example below will assist us in clarifying this.
'''


def the_outer_function():
    var = 10

    def the_inner_function():
        nonlocal var
        var = 14
        print("The value inside the inner function: ", var)
    the_inner_function()
    print("The value inside the outer function: ", var)


the_outer_function()
