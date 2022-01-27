# 9-11. Imported Admin 
from user import User, Admin

admin = Admin("James", "Bond", ("can add post", "can ban user"))
admin.privileges.show_privileges()