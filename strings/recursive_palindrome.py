def checkString(string):
  string = string.lower()
  if(len(string) > 2):
    if(string[0] == string[-1]):
      return checkString(string[1 : -1])
    else:
      return False
  else: return string[0] == string[-1]

print(checkString(input("check word for palindrome: ")))
