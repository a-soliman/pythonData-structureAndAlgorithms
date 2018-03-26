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
