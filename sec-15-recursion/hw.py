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


for x in range(0, 11):
      print('24- Fibonacci: ', x, ' - ', nth_fibonacci(x))