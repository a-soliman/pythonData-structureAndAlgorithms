#=======================================================================================

# reverse a string

'''

'''

def reverse(string):
    def reverse_letter(string, i, new_string=''):
        if i < 0:
            return new_string

        new_string += string[i]
        return reverse_letter(string, i-1, new_string)

    return reverse_letter(string, len(string)-1)

print('26- reverse_string: ', reverse('Hello'))

#=======================================================================================

# string permutation


'''
Given a string, return it's all permutation recrusivly

    ex: 
        input: 'abc'
        output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
'''

def permute(string):
    return string


print('27- string permutaiton: ', permute('abc'))