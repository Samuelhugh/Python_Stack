# Importing in Python
import random
# Console Logging in Python
print('Welcome to Python!')
# Console Log in Python
print('This is a loop printing 5 times')
# For Loop in Python
for x in range(1, 6):
    print(f'x is: {x}')
# Declaring a Variable and Assigning it an Array(List in Python)
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# Declaring a Variable and using my Import to Choose a Random day from the List by using a Method from the Random Class
day = random.choice(weekdays)
# Using an F-String to Concatenate the Random day into the Print Statement easier
print(f'Today is: {day}')
# If-Else Block in Python
if day == 'Monday':
    print('It will be a long week!')
elif(day == 'Friday'):
    print('Woohoo, time for the weekend!')
else:
    print('Not quite there yet.')