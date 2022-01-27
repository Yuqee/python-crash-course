# 8-13. User Profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_info = build_profile('Yuqi', 'Liu',
                         location='Chengdu',
                         nationality='Chinese',
                         filed='computing sciece')

print(user_info)