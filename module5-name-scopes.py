# the scope of a name is the part of the code where the name is properly recognizable and can be used.

def show_truth():
    #global just means don't create a second temporary variable
    # and instead use the global variable with this name
    global mysterious_var
    mysterious_var = 'New Surprise!'
    print(mysterious_var)


mysterious_var = 'Surprise!' #global variable
print(mysterious_var)
show_truth()
print(mysterious_var)

#python creates a second temporary variable with the same name and uses it in the function

def show_truth2():
    # we never use the equals operator,
    # which means we never create a local version of the variable
    # this applies to lists and dictionaries since they are mutable
    # this does not apply to tuples since they are immutable
    mysterious_var.append('New Surprise!')
    print(mysterious_var)

mysterious_var = ['Surprise!'] #global variable
print(mysterious_var)
show_truth2()
print(mysterious_var)