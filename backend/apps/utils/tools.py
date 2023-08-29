from string import ascii_lowercase, digits
from random import randint, choice


# generate random string
def random_string_gen(min_length, max_length):
    characters = ascii_lowercase + digits
    return "".join(choice(characters) for x in range(randint(min_length, max_length)))
