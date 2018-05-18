# Given an array of integers, return a new array such that each element at index i of the new array
# is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input
# was [3, 2, 1], the expected output would be [2, 3, 6].



def first_try(arr):
    product = 1
    new = []

    for x in arr:
        product *= x

    for x in arr:
        if x != 0:
            new.append(product/x)
        else:
            new.append(x)

    return new


if __name__ == "__main__":
    print(first_try([1,2,3,4,5]))
    print(first_try([3,2,1]))