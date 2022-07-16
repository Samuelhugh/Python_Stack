# 1. TASK: print "Hello World"
hw = 'Hello World'
print(hw.title())
# 2. print "Hello Noelle!" with the name in a variable
name = "Samuel"
fav_num = 33
print('Hello My name is %s and my favorite number is %d' % (name,fav_num))	# with a comma
print('Hello ' + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
num = 33
print('Hello', num)	# with a comma
print('Hello ' + str(num))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
food_one = "lobster"
food_two = "fried chicken"
print('I love to eat {} and {}.' .format(food_one,food_two)) # with .format()
print(f'I love to eat {food_one} and {food_two}.') # with an f string