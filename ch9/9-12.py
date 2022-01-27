# 9-12. Multiple Modules
from admin import Admin
admin = Admin("James", "Bond", ("can add post", "can ban user"))
admin.privileges.show_privileges()