# Python implementation of Letter Case Permutation
# Author: Irsyad

# This function will return every possible string with lowercase or uppercase combination of a given string.
# Sample input and output
# letterCasePermutation("abc") will produce ["abc","abC","aBc","aBC","Abc","AbC","ABc","ABC"]

def letterCasePermutation(S):
  result = ['']
  for char in S:
      if char.isalpha():
          result = [i+j for i in result for j in [char.lower(), char.upper()]]
      else:
          result = [i+char for i in result]
      print result
  return result

# Test
print(letterCasePermutation("a1b2"))