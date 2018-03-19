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

print('is_anagram:\n {} || {}. = '.format(s1, s2), is_anagram(s1, s2))