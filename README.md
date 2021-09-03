# Swapps technical test

Test 2: solving programming problems test

## Problem description

Having a string of random characters and random length, create a method that identifies how
many substrings of 4 characters appear more than once along the main string. The method’s
only argument should be the main string.
It should return the substrings that repeat and how many times they appear in the text in a data
structure.

## Install and use
* For proper use, the test should be performed on a Unix system with python 3 installed.

~~~
$ git clone https://github.com/cjcruzrivera/swapps_test_1.git
~~~

* You can test the main file directly or if you need, you can move the method.py file to your own project, and include on your code like that.

~~~
from method import getFourLenSubStringRepeated

string = "main string"
results = getFourLenSubStringRepeated(string)
~~~

For test with main file, only needs to execute it.

~~~
$ python main.py

===
Insert the main string to analyze:  (insert string here)
===

If there isn't any result.
Output:
There aren't substrings of 4 characters that appear more than once along the main string.

If there are results.
Output:
Dict {
    "substring": "how many times they appear"
}
~~~


