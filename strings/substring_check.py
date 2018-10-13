def substring_check(string, sub_str):
    return sub_str in string

string = "Hello everyone"
sub_str_present ="llo e"
sub_str_absent ="abcd"
print(substring_check(string, sub_str_present)) # True
print(substring_check(string, sub_str_absent)) # False
