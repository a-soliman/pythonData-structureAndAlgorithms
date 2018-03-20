# Anagram Check

'''
Given two strings, check to see if they are anagrams. An anagram is when the two strings can 
be written using the exact same letters (so you just rearrange the letters to get the diffrent phrase or word).

FOR EXAMPLE:
      'public relations' is an anagram of 'crap built on lies.'
      'client eastwood' is an anagram of 'old west action'

- ignore spaces and capitalizations 
'''

def is_anagram(str1, str2):
      str1 = str1.replace(' ', '').lower()
      str2 = str2.replace(' ', '').lower()

      letters_count = {}

      for letter in str1:
            if letter in letters_count:
                  letters_count[letter] += 1
            else:
                  letters_count[letter] = 1 

      for letter in str2:
            if letter in letters_count and letters_count[letter] > 0:
                  letters_count[letter] -= 1
            else:
                  return False
      
      for letter in letters_count:
            if letters_count[letter] != 0:
                  return False
      
      return True

s1 = 'clint eastwood'
s2 = 'old west action'

print('1- is_anagram:\n {} || {}. = '.format(s1, s2), is_anagram(s1, s2))

#=======================================================================================

# Array Pair Sum

'''
Given an int arry, output all the unique pairs that sum up to a specific value k.

EX:
      pair_sum([1,3,2,2], 4)
      will return 2 pairs (1,3), (2,2)
'''

def arry_pair_sum(arr, value):
      hash = {}
      result= []

      for num in arr:
            if num in hash:
                  hash[num] += 1
            else:
                  hash[num] = 1
      
      for num in hash.keys():
            if int(num) <= value and hash[num] > 0:
                  val1 = int(num)
                  remaind = value - val1

                  if remaind in hash and hash[remaind] > 0:
                        val2 = remaind

                        hash[val1] -= 1
                        hash[val2] -= 1

                        result.append([val1, val2])
      return result

arr = [1,3,2,2,0]
sum = 4
print('2- pair_sum : ', arry_pair_sum( arr,sum))

#=======================================================================================

# Find the missing element

'''
Consider an array of non-negative ints, A second array is formed by shuffling the elements
of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array

EX:
      finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
      5 is the missing element
'''
def finder1(arr1, arr2):
      if len(arr2) != len(arr1)-1:
            return
      
      for num in arr1:
            if num not in arr2:
                  return num

print('3- Find the missing element: ', finder1([1,2,3,4,5,6,7], [3,7,2,1,4,6]))

def finder2(arr1, arr2):
      hash = {}

      for num in arr2:
            if num in hash:
                  hash[num] += 1
            else:
                  hash[num] = 1
            
      for num in arr1:
            if num not in hash:
                  return num

print('4- Find the missing element: ', finder2([1,2,3,4,5,6,7], [3,7,2,1,4,6]))

#=======================================================================================

# Largest continuous Sum

'''
Given an array of integers (positive and negative) find the largest continuous sum.


EX:
      largest_cont_sum([1,2,-1,3,4,10,10,-10,-1])
      output 29
'''
def largest_cont_sum(arr):
      if len(arr) == 0:
            return 0
      
      max_sum = current_sum = arr[0]

      for num in arr[1:]:
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)

      return max_sum

print(largest_cont_sum([-10,2,-1,3,4,10,10,-10,-1]))