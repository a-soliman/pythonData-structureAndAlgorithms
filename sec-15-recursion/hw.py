'''

'''


#=======================================================================================

# recursive Sum

'''
Write a recursive function that returns the sum from 0 up to n

'''

def sum_down( n ):
      if n == 1:
            return 1
      else:
            return n + sum_down(n-1)

print('23- sum_down: ', sum_down(5))



#=======================================================================================

# recursive fibonacci

'''


'''

def nth_fibonacci( n ):
      fibonacci = [0, 1]

      # helper function
      def search(x, limit):
            #base-case
            if x == limit:
                  return
            
            sum  = fibonacci[x-1] + fibonacci[x-2]
            fibonacci.append(sum)
            search(x+1, limit)
      
      if n < 2:
            return n

      search(2, n)
      return fibonacci[-1]


print('24- Fibonacci(50): ', nth_fibonacci(50))

#=======================================================================================

# recursive fibonacci_2

'''


'''

def nth_fibonacci_2( n ):
      if n == 1:
            return 1
      if n == 2:
            return 1
      
      if n > 2:
            return nth_fibonacci_2(n-1) + nth_fibonacci_2(n-2)

print('25- Fibonacci(10): ', nth_fibonacci_2(10))

#=======================================================================================

# recursive fibonacci_3

'''
using memoization

'''

def nth_fibonacci_3( n ):
      fib_hash = {}
      
      def search(x):
            if x in fib_hash:
                  return fib_hash[x]
            value = 0
            if x == 1:
                  value = 1
            if x == 2:
                  value = 2
            if x > 2:
                  value = search(x-1) + search(x-2)
                  fib_hash[x] = value
            return value
      search(n)
      return fib_hash[n]

print('26- Fibonacci_with_memoization(100): ', nth_fibonacci_3(100))

#=======================================================================================

# sum_func

'''
Given an integer, create a function which returns the sum of all the individual digits in that integer.
for example:
      if n = 4321m, return 4 + 3 + 2 + 1
'''