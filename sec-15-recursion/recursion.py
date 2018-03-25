'''
n factorial
'''

def factorial( n ):
      # base case
      if n == 0:
            return 1

      else:
            return n * factorial(n-1)

print(factorial(5))


def sum_down( n ):
      if n == 1:
            return 1
      else:
            return n + sum_down(n-1)

print(sum_down(5))

