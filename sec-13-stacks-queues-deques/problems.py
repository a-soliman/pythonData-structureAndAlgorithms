#=======================================================================================

# Balanced Prentheses

'''
Given a string of opening and closing parentheses, check whether it's balanced.
Assume that the string doesn't contain words or numbers, and you can assume that the string has no spaces


EX:
      '([])'
      output True
EX:
      '([)]'
      output: False
'''

def balance_check(string):
      if len(string) == 0:
            return 
      openining = ('(', '{', '[')
      matches = set([ ('(', ')'), ('[', ']'), ('{', '}') ])
      stack =[]

      for char in string:
            if char in openining:
                  stack.append(char)
            else:
                  for o,c in matches:
                        if c == char:
                              if o != stack.pop():
                                    return False
      return True
                                    
      


print('13- balance_check: ', balance_check('([[]])'))