# #1 This should return 5 to the print() built-in function
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())


# #2 This should give a NameError
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


# #3 This should return 5 to print and exit out of the function ignoring the rest of the instructions
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())


# #4 This should return 5 to the print function and ignore all the other instructions
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())


# #5 This should just print 5 inside the function and then return nothing to (x) but return back to the line it was called from, and print should print the entire outline of the function number_of_great_lakes
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x)


# #6 This function has two function calls, this function also takes two parameters. This function should pass the first function call arguments to the functions parameters and print b+c for inside the function to the terminal, and then do the same for the second function call. Print should have a Error because nothing was returned (TypeError)
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))


# #7 This function takes two parameters. the function is called in the built in print() function and passes it two arguments (integers). The instructions for this function is to return the integers as strings using the built-in str() function. Then after the concatenation is done print the function call which is set equal to the return statement in the function
# def concatenate(b,c):
#     return str(b)+str(c)
# print(concatenate(2,5))


#8 This functions is called by the print() built-in function. The instrcutions say to declare a variable (b) and set it to 100. Then the next line says to print the variable. Then the function is called and now the interpreter goes inside the function code block to execute the instructions, which say to declare a variable (b) and set it to 100. Then print the variable(b). And it doesn't matter that the default t-diagram's variable is the same as the functions variable because it is inside the function and they are separately t-diagramed. Then if checks asking Boolean questions and if the fist is true the second is skipped and since it is a else statement with a return inside of it the interpreter take that return and ignores the rest of the instructions. So 10 should be returned to the function call and printed.
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(number_of_oceans_or_fingers_or_continents())


# #9 This function takes two parameters. And has three function calls. So This code snippet should produce 7 for the first function call and 14 for the second function call and then 21 for the third function call.
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


# #10 I have the print() built-in function calling the function. The Function call is passing two arguments to the function parameters or inputs. So this function should return 8 to the function call which is ALWAYS set equal to what the return statement is. And then the interpreter ignores the rest of the instructions.
# def addition(b,c):
#     return b+c
#     return 10
# print(addition(3,5))


# #11 This code snippet is declaring a variable (b) outside the function and setting it to 500. And then printing the variable (b) to the terminal. Then the code says to print the outside variable (b) again. Then the code calls the function, And in the functions, the instructions say to declare a variable (b) and set it to the integer 300 and then print (b) to the terminal but does not return anything. Then the interpreter returns back to the line it was called from and runs the next line of code which says to print the outside (b).
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
# print(b)
# foobar()
# print(b)


# #12 Outside the function variable (b) is being declared and set to the integer 500. Then the code says to print the outside variable (b). This code snippet should produce 500,500,300,500
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)


# #13 This code should produce 500 outside,500 outside,300 inside,300 outside, Because (b) is now set to the foobar function.
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar()
# print(b)


# #14 1 gets printed inside of the function, 3 gets printed to the terminal for the bar() function that was called inside the foo function, Causing the foo function to pause so the interpreter can run the bar() functions instructions. Nothing gets/is returned from the bar() function. So foo now continues and prints 2 to the terminal.
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()


# #15 print 1 for the foo() function, then (x) is set to the bar() function so the foo() function is paused so the interpreter can parse the bar() functions instruction and in the bar() instructions its says to print 3 to the terminal and return 5 back to the variable (x) in the foo() function that called the bar() function. So now the foo() function continues and the next instruction to the interpreter is to print (x) which is the integer 5 from the bar() function. And then return 10 to y, which was set to the function call and the function call is ALWAYS set to the return value. And finally print y to the terminal.
# def foo():
#     print(1)
#     x = bar()
#     print(x)
#     return 10
# def bar():
#     print(3)
#     return 5
# y = foo()
# print(y)