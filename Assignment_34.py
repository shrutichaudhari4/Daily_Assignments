# Binary To Octal:

bin_num=input("Enter binary num:")
# print(bin_num)
num=""
octal_list={'000':'0','001':'1','010':'2','011':'3','100':'4','101':'5','110':'6','111':'7'}
while(bin_num!=""):
   for i in str(bin_num):
       if len(bin_num)//3==0:
           num+=str((int(i)%3))
           bin_num=str(int(bin_num)%1000)
print(num)
if num in octal_list:
    print(octal_list.get(num))

