# Ben Stobaugh - problem 4
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array. The array can contain
# duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.


# Not constant space :/
def first_missing_positive(arr):
    arr = set(arr)
    i = 1
    while i in arr:
        i += 1
    return i



if __name__ == "__main__":
    assert first_missing_positive([3, 4, -1, 1]) == 2, "Given"
    assert first_missing_positive([1, 2, 0]) == 3, "Given"