# Reverses a given string.
def reverse(s):
    return s[::-1]

def isPalindrome(s):
    # Convert s to uppercase to ignore case sensitivity
    s = s.upper()
    # Checking if both string are equal or not
    if (s == reverse(s)):
        return True
    return False

# Tests
print(isPalindrome('Racecar'))
print(isPalindrome('ferrari'))
print(isPalindrome('CiVIc'))
