# Num of Days in a Month:
month=11
year=2020

if(month==2 and ((year%4==0) or (year%100==0 and year%400==0))):
    print("Month has 29 days")
elif(month==2):
    print("Month has 28 days")
elif(month==6 or month==9 or month==11 or month==4):
    print("Month has 30 days")
else:
    print("Month has 31 days")
