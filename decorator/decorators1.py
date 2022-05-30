def decorators_function (any_function):
    def wrap():
        print("This is reliable path ")
        any_function()
    return wrap

@decorators_function
def function1():
    print("for execution our program !!")
function1()

@decorators_function
def function2():
    print("for execution our code !!")
function2()
