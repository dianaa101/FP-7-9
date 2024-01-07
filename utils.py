import random


def random_name(n):
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    # Add a randomly chosen uppercase letter to the string 's'
    s = s + random.choice(uppercase_letters)
    #  Loop n - 1 times
    #  Add a randomly chosen lowercase letter to the string 's'
    for x in range(n - 1):
        s = s + random.choice(lowercase_letters)
    return s


def random_name_between(minimum, maximum):
    # Generate a random integer 'n' between 'minimum' and 'maximum'
    n = random.randint(minimum, maximum)
    return random_name(n)
