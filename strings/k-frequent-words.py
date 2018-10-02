# Python program to find the k most frequent words 
# from data set 
from collections import Counter 
  
data_set = "" #Enter long string or paragraph here
  
# split() returns list of all the words in the string 
split_it = data_set.split() 
  
# Pass the split_it list to instance of Counter class. 
Counter = Counter(split_it) 
  
# most_common() produces k frequently encountered 
# input values and their respective counts. 
most_occur = Counter.most_common(4) 
  
print(most_occur) 