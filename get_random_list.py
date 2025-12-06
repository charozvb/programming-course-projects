import random

def get_random(m, n):
    """function that creates list with random numbers in range between m and n"""
    lst = []
    counter = 0
    while(counter < n):
        lst.append(random.randrange(0, m))
        counter += 1
    return lst


if __name__ == "__main__":
    print(get_random(10, 5))
