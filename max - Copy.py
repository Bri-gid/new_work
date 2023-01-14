digits=input('Please enter the list of numbers separated by spaces.')
user_list=digits.split()
print('list:',user_list)
for i in range(len(user_list)):
    user_list[i]=int(user_list[i])
print('max=',max(user_list))
