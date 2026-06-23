import secrets
import string




def generate_password(length):
    try :
        if length < 4 :
            raise ValueError
        lower =  string.ascii_lowercase 
        upper = string.ascii_uppercase 
        ponct = string.punctuation
        digit = string.digits 
        password =[
            secrets.choice(lower),
            secrets.choice(upper),
            secrets.choice(ponct),
            secrets.choice(digit)]
        all_char = lower + upper + ponct + digit
        
        for _ in range(length-4) :
            password += [secrets.choice(all_char)]
        secrets.SystemRandom().shuffle(password)
        return ''.join(password) 
    except ValueError :
        error = f'"Minimum length is 4"'
        return error

