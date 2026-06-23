
def rate_password(password):
    length = len(password)
    has_lower =  any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_symbol = any(not c.isalnum() for c in password)
    has_digit = any(c.isdigit() for c in password)

    types = sum([has_lower,has_upper,has_symbol,has_digit] )
    
    if length>2 and length<8 and types>=2 :
        print("weak")
    elif length>=8 and length<12 and types>=3 :
        print("medium")
    elif length>12 and types ==4 :
        print("strong")
    else :
        print("please add more type and length")
    