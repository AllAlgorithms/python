# A Python program to demonstrate working 
# of re.match(). 
import re 
  
# a sample function that uses regular expressions 
# to find month and day of a date. 
def findMonthAndDate(string): 
      
    regex = r"([a-zA-Z]+) (\d+)"
    match = re.match(regex, string) 
      
    if match == None:  
        print "Not a valid date"
        return
  
    print "Given Data: %s" % (match.group()) 
    print "Month: %s" % (match.group(1)) 
    print "Day: %s" % (match.group(2)) 
  
      
# Driver Code 
findMonthAndDate("" #Enter pattern to match) 
print("") 
findMonthAndDate("") #Enter string 