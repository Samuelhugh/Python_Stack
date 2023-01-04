# 1) Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Declaring a Variable and Assigning it the Value of a List containing two other List
x = [ [5,2,3], [10,8,9] ]
# Printing to the Terminal the Value of the "x" Variable
print(x)
# Manipulating the List within the Variable to change the Second Index of the List and the First Indexed Value of that List
x[1][0] = 15
# Printing to the Terminal the Variable "x", to see if I correctly Maneuvered the List as expected
print(x)

# 2) Change the last_name of the first student from 'Jordan' to 'Bryant'
# Declaring a Variable and Assigning it the Value of a List containing two Dictionaries
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
# Accessing the First Index of the List and the "last_name" Key to change the current Value to another
students[0]['last_name'] = 'Bryant'
# Printing the "students" Variable to see if I changed the Key/Value pair as expected
print(students)

# 3) In the sports_directory, change 'Messi' to 'Andres'
# Declaring a Variable and Assigning it the Value of a Dictionary with the Values being Lists
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
# Accessing the Dictionary's "soccer" Key to change the First Value of its List to another Value
sports_directory['soccer'][0] = 'Andres'
# Printing the Variable to see if the First Value of Key "soccer" changed as expected
print(sports_directory)

# 4) Change the value 20 in z to 30
# Declaring a Variable and Assigning it the Value of a List with one Dictionary
z = [ {'x': 10, 'y': 20} ]
# Accessing the First Index of the List and "y" Key of the Dictionary to change its numerical Value
z[0]['y'] = 30
# Printing the Variable to see if I Manipulated/Mutated the Key's Value as expected
print(z)
# *************************************************************************************************** #

# 1) Declaring a Variable, and Assigning it the Value of a List of four Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# 2) Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.
def iterateDictionary(some_list):
    for x in some_list:
        print(x)
        output = ""
        for key, value in x.items():
            # print(f'{key} - {value}')
            output += f" {key} - {value},"
        print(output)
# Function Call
iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
# *************************************************************************************************** #

# Declaring a Variable, and Assigning it the Value of a List of four Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# 3) Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.
def iterateDictionary2(key_name, some_list):
    for i in range(0, len(some_list)):
        output = ""
        for key in some_list[i]:
            print(key)
            if key != key_name:
                output += f"{key_name} - {some_list[i][key_name]}"
                # print(f"{key_name}, {some_list[i][key_name]}")
        print(output)
# Function Call
iterateDictionary2("last_name", students)
# *************************************************************************************************** #

dojo = {
    'locations' : ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors' : ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# 4) Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list.
def printInfo(some_dict):
    for x in some_dict:
        print(len(some_dict[x]), x)
        for values in some_dict[x]:
            print(values)
# Function Call
printInfo(dojo)
# # # output:
# # 7 LOCATIONS
# # San Jose
# # Seattle
# # Dallas
# # Chicago
# # Tulsa
# # DC
# # Burbank

# # 8 INSTRUCTORS
# # Michael
# # Amy
# # Eduardo
# # Josh
# # Graham
# # Patrick
# # Minh
# # Devon