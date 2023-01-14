current_users=['aubrey','pius','jessica','brigid','erica']
new_users=['phyte','asumadu','godfred','punch','BRIGID']
for name in new_users:
    if name.lower() in current_users:
        print('The name has been used.Take a different name.')
    else:
         print('The username is available.')
