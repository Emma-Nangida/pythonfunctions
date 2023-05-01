#Write a Python function that takes two arguments
#(a and b) and returns their sum.

def total_number(a,b):
  return a+b
a=200
b=300
print(total_number(a,b))


#Write a Python function that takes a string as 
#input and returns the string reversed.

def my_word(name):
  return name[::-1]

mytxt = my_word("emma")

print(mytxt)



#Write a Python function that takes a list of 
#integers as input and returns the sum of all the integers in the list.
def group_of_integers(integers):
  sum=0
  for int in integers:
    sum +=int
    return sum
integers = [1, 2, 3, 4, 5]
print(f'The sum of the list {integers} is {group_of_integers(integers)}')

#Write a Python function that takes a list of 
#integers as input and returns a new list with all the even numbers removed.
def odd_numbers(num):
  new_num=[]
  for i in num:
    if i%2!=0:
     new_num.append(i)
    return new_num
print(odd_numbers([2,5,6,7,9,11]))

# Write a Python function that takes a list of 
#integers as input and returns the highest value in the list.
def highest_value(nums):
  a=max(nums)
  return a
print(highest_value([10,30,41,10]))
#Write a Python function that takes a list of strings as input 
#and returns a new list with all the strings capitalized.
def capitalise(name):
  return name.capitalize()
print(capitalise("emmah"))