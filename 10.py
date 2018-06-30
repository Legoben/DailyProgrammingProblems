# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import bisect
import time
times = []
store = {}

def hello():
    print("hello1")

def hello2():
    print("bye")

def add_job(f, n):
    if n not in store:
        bisect.insort(times, n)
        store[n] = []

    store[n].append(f)

def run_scheduler():
    start = int(round(time.time() * 1000))
    while len(times) > 0:
        if times[0] <= int(round(time.time() * 1000)) - start:
            t = times.pop(0)
            [x() for x in store[t]]

if __name__ == "__main__":
    add_job(hello, 400)
    add_job(hello2, 1000)
    add_job(hello, 1400)
    add_job(hello2, 5000)
    add_job(hello, 5000)

    run_scheduler()
    pass

