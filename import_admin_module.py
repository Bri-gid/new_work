from adminn import Privileges,Users,Admin
'''Importing the Users class to make an instance in another file'''
hey_admin=Admin('brigid','addai-mmra',21,'kumasi')
hey_admin.privileges.show_privileges("can add post", "can delete post", "can ban user")





