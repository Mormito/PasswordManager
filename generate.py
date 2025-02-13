import random
import string

def generatepasswd():
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=10))

