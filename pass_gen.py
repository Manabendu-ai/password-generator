import random as rnd


def gen_pass(size = 10, level = "hard"):
    levels = {
        "easy" : password_generator_easy(size),
        "medium" : password_generator_medium(size),
        "hard" : password_generator_hard(size)
    }

    return levels[level]


def password_generator_easy(size=10):
    pwd = " "
    for i in range(size):
        pwd += rnd.choice(rnd.choice([str(x) for x in range(1, 10)]))
    return pwd

def password_generator_medium(size=10):
    pwd = " "
    for i in range(size):
        pwd += rnd.choice([rnd.choice(list("abcdefghijklmnopqrstwuvxyzABCDEFGHIJKLMNOPQRSTWUVXYZ")), rnd.choice([str(x) for x in range(1, 10)])])
    return pwd

def password_generator_hard(size=10):
    pwd = " "
    for i in range(size):
        pwd += rnd.choice([rnd.choice(list("abcdefghijklmnopqrstwuvxyzABCDEFGHIJKLMNOPQRSTWUVXYZ")), rnd.choice([str(x) for x in range(1, 10)]), rnd.choice(list('!@#$%^&*()~'))])
    return pwd

