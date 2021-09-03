"""
Script with terminal input for test the method 
to get repeated substrings of length 4 
"""

import json
from method import getFourLenSubStringRepeated

string = input("Insert the main string to analyze: ")

result = getFourLenSubStringRepeated(string)

if result:
    print(f"The substrings found are: ")
    #For pretty print the dict
    print(json.dumps(result, indent=3))
else:
    print("There aren't substrings of 4 characters that appear more than once along the main string.")

