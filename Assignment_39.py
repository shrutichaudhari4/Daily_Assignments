# Using Loops and function:
a='Listen'
b='Silent'
a=sorted(a.lower())
b=sorted(b.lower())
def check(st1,st2):
    for i in a:
        if i in b:
            return "Anagram"
        else:
            return "Not Anagram"
print(check(a,b))


# using Counter and function
from collections import Counter
s1='maD'
s2='Dam'
def check2(first,second):
    # print(Counter(s1))
    # print(Counter(s2))
    if Counter(s1)==Counter(s2):
        return "Strings are Anagrams"
    else:
        return "Strings are not Anagrams"
print(check2(s1.upper(),s2.upper()))
