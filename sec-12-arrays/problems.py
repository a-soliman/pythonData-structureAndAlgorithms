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
                  print('val1 ', val1, 'remidnd: ', remaind)

                  if remaind in hash and hash[remaind] > 0:
                        val2 = remaind

                        hash[val1] -= 1
                        hash[val2] -= 1

                        result.append([val1, val2])
      return result


print(arry_pair_sum([1,3,2,2,0],1))
