"""
This file can be imported as a module and contains the following
function:

    * getFourLenSubStringRepeated - returns how many substrings of 4 characters appear more than once along a main string
"""

def getFourLenSubStringRepeated(mainString):
    """
    Method that identifies how many substrings of 4 characters appear more than once along the main string.

    Parameters
    ----------
    mainString : str
        String to be analyzed

    Returns
    -------
    dict
        a dict with the next format, with a line from each substring:
        {
            "key" : value,
        }

        key: substring found
        value: how many time the substring appear
    """
    result = {}
    length = len(mainString)

    for index in range(0, length):
        if index <= (length-4):
            substring = mainString[index:(index+4)]
            count = mainString.count(substring)
            if(count > 1):
                result[substring] = count

    return result