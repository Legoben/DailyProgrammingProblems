# Given an integer k and a string s, find the length of the longest substring that contains at most
# k distinct characters.
#
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

from collections import deque


def longest(s, k):
    if len(s) <= k:
        return s

    if k == 0:
        return ""

    if k == 1:
        return s[0]

    bounds = [0, 0]
    letters_order = deque()
    letters_set = set()

    longest_bounds = bounds[:]

    for i in range(len(s)):
        letter = s[i]
        bounds[1] = i

        if letter not in letters_set and len(letters_set) == k:
            if bounds[1] - bounds[0] > longest_bounds[1] - longest_bounds[0]:
                longest_bounds = bounds[:]
            past = letters_order.popleft()
            letters_set.remove(past[0])
            bounds[0] = letters_order[0][1]

        if letter not in letters_set:
            letters_set.add(letter)
            letters_order.append((letter, i))

    if bounds[1] - bounds[0] > longest_bounds[1] - longest_bounds[0]:
        return s[longest_bounds[0]:bounds[1] + 1]

    return s[longest_bounds[0]:longest_bounds[1]]


if __name__ == "__main__":
    assert longest("abcba", 2) == "bcb", "given"
    assert longest("aaaaaaaaaaaaaaaa", 5) == "aaaaaaaaaaaaaaaa"
    assert longest("babababababacbabababa", 3) == "babababababacbabababa"
    assert longest("babababababacbabababa", 2) == "babababababa"
    assert longest("babababababac", 2) == "babababababa"

