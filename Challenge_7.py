import random
import string


def generate_pass() -> str:
    caracteres = string.ascii_letters + string.digits + string.punctuation
    length = random.randint(8, 16)
    password = ''.join(random.choice(caracteres) for _ in range(length))
    return password


user_pass = generate_pass()
print(user_pass)
