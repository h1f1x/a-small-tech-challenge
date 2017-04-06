import random


def generate_testdata(n):
    numbers = range(1, n)
    doublette = random.randint(1, n - 1)
    numbers.append(doublette)
    random.shuffle(numbers)
    return numbers


def first_solution(numbers):
    pass

def second_solution(numbers):
    pass


if __name__ == '__main__':
    numbers = generate_testdata(1000)
