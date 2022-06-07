# Write code for algorithm 5 below

def palindrome(str):
    if len(str) < 2:
        return True
    else:
        if str[0] == str[-1]:
            return palindrome(str[1:-1])
        else:
            return False


# All should print True
print(palindrome("madam"))
print(palindrome("radar"))
print(palindrome("kayak"))


# First should print False, second should print True
print(palindrome("test"))
print(palindrome("aa"))

