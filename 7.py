# Problem 7 - Ben Stobaugh
#
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not allowed.


combos = set()

def parse_num(nums_remaining, curr_phrase = ""):
    if curr_phrase in combos:
        return

    if len(nums_remaining) == 0:
        if curr_phrase != "" and curr_phrase not in combos:
            combos.add(curr_phrase)
            return
        else:
            return

    if len(nums_remaining) != 1:
        addition = int(nums_remaining[:2])
        if addition <= 26:
            parse_num(nums_remaining[2:], curr_phrase + chr(addition))

    parse_num(nums_remaining[1:], curr_phrase + chr(int(nums_remaining[:1])))



def run_parse(nums):
    parse_num(nums)
    val = len(combos)
    combos.clear()
    print(val)
    return val


if __name__ == "__main__":
    assert run_parse('111') == 3
    assert run_parse('456') == 1
    assert run_parse('23221') == 6
    assert run_parse('321') == 2