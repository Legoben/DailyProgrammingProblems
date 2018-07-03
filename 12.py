# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function
# that returns the number of unique ways you can climb the staircase. The order of the steps matters.
#
# For example, if N is 4, then there are 5 unique ways:
#
# • 1, 1, 1, 1
# • 2, 1, 1
# • 1, 2, 1
# • 1, 1, 2
# • 2, 2
#
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive
# integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

cache = {1: 1, 0: 1}

def numCombosOneTwo(n):
    if n in cache:
        return cache[n]

    total = 0
    if n >= 2:
        total += numCombosOneTwo(n - 2)

    total += numCombosOneTwo(n - 1)

    return total

def numCombosArb(n, steps):
    if n in cache:
        return cache[n]

    total = 0
    for i in steps:
        if n >= i:
            total += numCombosArb(n - i, steps)

    return total

if __name__ == "__main__":
    assert numCombosOneTwo(4) == 5
    cache = {1: 1, 0: 1}
    assert numCombosArb(4, [1, 2]) == 5
    cache = {1: 1, 0: 1}
