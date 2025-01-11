#define a function which bools true of a string is palindrome
def is_palindrome (name):
    if name[0] == name[-1]:
        return True
    return False

print(is_palindrome("kiran"))
print(is_palindrome("nayan"))
print(is_palindrome("naman"))