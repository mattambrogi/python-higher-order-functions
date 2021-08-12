

"""
Playing with Lambda Functions

From section 1.6.7 of composing programs

In general, python prefers def statements, but lambdas are useful where there is a simple nested function as an argument or return value.
"""
def compose(f, g):
  return lambda x: f(g(x))

f = compose(
  lambda x : x*x, 
  lambda y : y+1 )

result = f(11)

print(result)


#I'd like to come back and write an acutal test for this instead of a print

"""
Example of simple recursive function
"""
def sum_digits(n):
  if n < 10:
    return n
  else:
    all_but_last, last = n // 10, n % 10
    return sum_digits(all_but_last) + last

summed_result = sum_digits(552)
print(summed_result)


"""
Example of mutual recursion
"""

def is_even(n):
  if n == 0:
    return True
  else:
    return is_odd(n-1)

def is_odd(n):
  if n == 0:
    return False
  else:
    return is_even(n-1)

result3 = is_even(4)
print(result3)

"""
Example of tree recursion
"""

def fib(n):
  """
  Returns Nth number in fibonacci series
  """
  if n == 1:
    return 0
  if n == 2:
    return 1
  else:
    return fib(n-2) + fib(n-1)

result_fib = fib(6)
print(result_fib)



"""
List Comprehension
"""

def divisors(n):
  return [1] + [x for x in range(2,n) if n % x == 0]

result_divisors = divisors(8)
print(result_divisors)



#keep if function
#takes an list and a filter
#So if want all posts from a user
#have a general keep if
#pass that by_user
#by user definted elsewhere
