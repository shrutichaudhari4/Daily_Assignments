# Replace one string with Another:

# using string and replace method()
string=input('Enter string:')
str1=input("Enter String which needs to be replaced:")
str2=input("Enter string you need to replace with: ")
string=string.replace(str1,str2)
print(string)

# Using if-else and replace method()
s='HeyYou'
s2='Me'
if 'You' in s:
    s=s.replace('You',s2)
print(s)
