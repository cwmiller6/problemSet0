#Author: Cole Miller
#Date: 30 March 2016

#Problem 0 
def is_even(integer):

	''' Takes a non-negative integer and returns True if it is even, and False if it is odd ''' 

	integer = int(integer)

	eoro = integer % 2

	#If the number has a remainder, it is odd, so using the mod function we can detect if there is a remainder of more than 0
	if eoro > 0:
		return False 
	else:
		return True

#Problem 1 
def digits(integer):

	''' Takes a non-negative integer and returns the number of digits ''' 

	counter = 0
	while integer >= 1: #Decimal places
		integer = integer/10 
		counter += 1
	return counter

#Problem 2
def sum_digits(integer):

	''' Takes a non-negative integer and returns the sum of all its digits '''
	sum = 0
	while integer > 0:
		ten  = integer % 10 #This will find the value of the tens place of the int
		sum += ten #First part of adding digits, tens place
		integer = integer - ten #Now the tens place needs to be 0
		integer = integer /10 #continue to divide int by 10 to make hundreds place tens place
	return sum

#Problem 3
def sum_less_ints(number):

	''' Takes a non-negative integer and returns the sum of all integers that are less than the given number '''
	
	number = int(number)
	intList = range(1, number) 
	sumLessInts = sum(intList)
	return sumLessInts

#Problem 4
def number_factorial(number):
	number = int(number)
	''' Takes a non-negative integer and returns its factorial '''
	intList = range(1, number + 1) #This time we will use number + 1, so that the range goes up to number but does not inlcude
	product = 1
	for item in intList:
		product *= item #Multiply list together
	return product

#Problem 5 
def factor_firstnumber(firstnumber, secondnumber):

	''' Takes 2 positive integers and determines if the second number is a factor of the first (returns True if it is a factor, else False) '''
	
	result = firstnumber % secondnumber

	if result > 0:
		return False
	else:
		return True

#Problem 6
def is_prime(number):
	''' Takes integer greater than or equal to 2 and returns whether the number is prime '''
	number = int(number)
	divisors = range(2, number) #list of all possible divisiors to determine prime or not
	for item in divisors:
		if number % item == 0:
			return False
		else:
			return True

#Problem 7
def is_perfect(number):
	factors = []
	''' Takes positive integer and returns whether number is perfect ''' 
	number = int(number) #Casting to int all day every day
	divisors = range(1, number) #Make list of possible diviors again (factor of number cannot be itself)
	for item in divisors:
		if number % item == 0:
			factors.append(item)
	sumOfFactors = sum(factors) #Add list of all factors
	if sumOfFactors == number: #Only case of perfection is if all factors add up to original number
		return True
	else:
		return False

#Problem 8
def divided_sum_digits(number):
	number = int(number)
	''' Takes positive integer and returns true if the sum of the digits of the number divides evenly into the number, false otherwise '''
	output = sum_digits(number) #not sure if we could use the functions we already made but its convinient 
	test = number % output
	if test == 0: #If there is not a remainder then the numbers do divide eveny, so return True if this is case
		return True
	else:
		return False




