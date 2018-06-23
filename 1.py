# Problem 1 - Ben Stobaugh

def one_pass(arr, target):
    aux = set()

    for i in arr:
        if target - i in aux:
            return True
        else:
            aux.add(i)

    return False


if __name__ == "__main__":
    assert one_pass([10, 15, 3, 7], 17) == True, "Given example"
    assert one_pass([0, 1, 1, 1, 7], 1) == True, "0 + dupes"
    assert one_pass([0, 1, 1, 1, 7], 0) == False, "0 + dupes"
    assert one_pass([0], 0) == False
    assert one_pass([], 0) == False
    assert one_pass([20, -20], 0) == True
    assert one_pass([20, 34, 435, 543, -3, 40, 543, 50, 3], 0) == True


