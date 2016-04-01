#Author: Cole Miller
#Date: 31 March 2016



#Problem 0 Test Case
from problemSet0 import is_even 
print("Problem 0:\n")
case0 = is_even(5)

case0a= is_even(6)

if case0 == False:
	print("The number 5 is odd.")
else:
	print("The number 5 is even.")

if case0a == False:
	print("The number 6 is odd.")
else:
	print("The number 6 is even.") 

#Problem 1 Test Case
from problemSet0 import digits 

print("\nProblem 1:\n")

print("156 has {} digits".format(digits(156)))
print("78 has {} digits".format(digits(78)))
print("3 has {} digits".format(digits(3)))

#Problem 2 Test Case
from problemSet0 import sum_digits 

print("\nProblem 2:\n")

print("The sum of the digits of 356 is {}".format(sum_digits(356)))
print("The sum of the digits of 67 is {}".format(sum_digits(67)))
print("The sum of the digits of 5 is {}".format(sum_digits(5)))

#Problem 3 Test Case
from problemSet0 import sum_less_ints

print("\nProblem 3:\n")

print("The sum of the integer less than 6 is {}".format(sum_less_ints(6)))
print("The sum of the integer less than 70 is {}".format(sum_less_ints(70)))
print("The sum of the integer less than 560 is {}".format(sum_less_ints(560)))

#Problem 4 Test Case
from problemSet0 import number_factorial

print("\nProblem 4:\n")

print("The factorial of the integer 36 is {}".format(number_factorial(36)))
print("The factorial of the integer 12 is {}".format(number_factorial(12)))
print("The factorial of the integer 7 is {}".format(number_factorial(7)))

#Problem 5 Test Case
from problemSet0 import factor_firstnumber

print("\nProblem 5:\n")

print("Is 6 a factor of 36? Answer: {}".format(factor_firstnumber(36, 6)))
print("Is 5 a factor of 78? Answer: {}".format(factor_firstnumber(78, 5)))
print("Is 100 a factor of 8000? Answer: {}".format(factor_firstnumber(8000, 100)))

#Problem 6 Test Case
from problemSet0 import is_prime

print("\nProblem 6:\n")

print("Is the integer 5 prime? Answer: {}".format(is_prime(5)))
print("Is the integer 67 prime? Answer: {}".format(is_prime(67)))
print("Is the integer 100 prime? Answer: {}".format(is_prime(100)))

#Problem 7 Test Case
from problemSet0 import is_perfect

print("\nProblem 7:\n")

print("Is the integer 3 perfect? Answer: {}".format(is_perfect(3)))
print("Is the integer 88 perfect? Answer: {}".format(is_perfect(88)))
print("is the integer 4 perfect? Answer: {}".format(is_perfect(4)))

#Problem 8 Test Case
from problemSet0 import divided_sum_digits

print("\nProblem 8:\n")

print("Do the sum of the digits of 666 divide equally into 666? Answer: {}".format(divided_sum_digits(666)))
print("Do the sum of the digits of 250 divide equally into 250? Answer: {}".format(divided_sum_digits(250)))
print("Do the sum of the digits of 36 divide equally inyo 36? Answer: {}".format(divided_sum_digits(36)))

