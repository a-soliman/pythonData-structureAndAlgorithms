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