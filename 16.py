# You run an e-commerce website and want to record the last N order ids in a log.
#
# Implement a data structure to accomplish this, with the following API:
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
#
# You should be as efficient with time and space as possible.

class Logs():
    def __init__(self, N):
        self.N = N
        self.cur_start = -1
        self.logs = {-1: None}

    def record(self, order_id):
        if len(self.logs) == self.N:
            del self.logs[self.cur_start - self.N + 1]

        self.logs[self.cur_start + 1] = order_id
        self.cur_start += 1

    def get_last(self, i):
        return self.logs[self.cur_start - i]


if __name__ == "__main__":
    l = Logs(10)

    for i in range(40):
        print(i)
        l.record(chr(i + 30))
        print(l.cur_start)
        if i >= 5:
            print(l.get_last(2))
        print(l.logs)

