import random, string

def str_gen(size=16, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))