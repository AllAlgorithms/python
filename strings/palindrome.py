# Reverses a given string.
def reverse(s):
    return s[::-1]

def isPalindrome(s):
    # Checking if both string are equal or not
    if (s == reverse(s)):
        return True
    return False

# Tests
print(isPalindrome('racecar'))
print(isPalindrome('ferrari'))
print(isPalindrome('civic'))
