'''Making an Admin instance from different modules'''
from userr import Users
from privilege import Admin,Privileges

yo_admin=Admin('brigid','addai-mmra',21,'kumasi')
yo_admin.privileges.show_privileges("can add post", "can delete post", "can ban user")

