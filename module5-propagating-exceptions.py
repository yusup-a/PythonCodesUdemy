#If a function that raises the exception does not have a try except block,
# then that exception is propagated to the function that called it (so get_user_bday takes care of it)
# If the get_user_bday or that function doesn't have a try except block either,
# then the exception is propagated again until there finally is a try except block somewhat in the funciton call chain.
# If no try except block can be found anywhere,
# then Python will show the error message