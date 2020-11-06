import random, time

# print() is a function. Functions do something
print("Hello Pivot!")

# In Python, words, sentences, pieces of text, etc. are represented as strings
# "Strings go between double quotations."
print("Zoom is fun.")

print(32) # 1, 2, 10, 256 are integers
print(1.28) # Most decimal numbers are floats
print(4.0) # 5.0 and 6.00 are floats

# True and False are booleans
print(True)
print(False)

# Variables are like x's and y's in algebra or containers that hold data or object(s)
my_text = "Python is fun."
my_int = 64
my_boolean = True

print(my_text)
print(my_int)
print(my_boolean)

# if, elif, and else denote logic statements or logical expressions
porridge_temp = "hot"
if porridge_temp == "hot":
	print("Too hot!")
elif porridge_temp == "cold":
	print("Too cold!")
elif porridge_temp == "warm":
	print("Just right")
else:
	print("The temperature is nonexistent.")

x = 16
if x <= 64:
	print("x is less than or equal to 64!")
else:
	print("x more than 64!")

porridge_temp = "hot"
if porridge_temp != "warm":
	if porridge_temp == "hot" or porridge_temp == "cold":
		print("Too", porridge_temp)
	else:
		print("The temperature is nonexistent.")
else:
	print("Just right")

# for and while loops denote repetition or iteration over a sequence
for i in range(1, 10): # 1 -> 9
	print(i)
for i in range(1, 11): # 1 -> 10
	print(i)
for i in range(10): # 0 -> 9
	print(i)
for i in range(0, 21, 2): # Multiples of 2 from 0 -> 20
	print(i)
for i in range(20, -1, -1): # 20 -> 0
	print(i)

counter = 1
while counter <= 10:
	print("The counter is:", counter) # print("The counter is: " + counter)
	counter += 1

# From the Python shell, use Ctrl + C to end Python programs prematurely
#while True:
#	pass