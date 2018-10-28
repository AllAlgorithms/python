def is_palindrome(num):
    """is the supplied argument a palindrome?
    checks if a number/string is a palindrome by casting it to a string
    and comparing if it stays the same when reversed
    """
    return str(num).lower() == str(num).lower()[::-1]


if __name__ == "__main__":
    print(is_palindrome(9219))
    print(is_palindrome(1221))
    print(is_palindrome("horse"))
    print(is_palindrome("abba"))
