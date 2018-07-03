# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

from collections import deque
import time
store = deque() # linked list

def hello():
    print("hello1")

def hello2():
    print("bye")

def add_job(f, n):
    i = 0

    for t in store:
        if t['time'] == n:
            t['jobs'].append(f)
            break
        elif t['time'] > n:
            store.insert(i, {"time": n, "jobs": [f]})
            break

        i += 1
    else:
        store.insert(i, {"time": n, "jobs": [f]})

def run_scheduler():
    start = int(round(time.time() * 1000))
    while len(store) > 0:
        if store[0]['time'] <= int(round(time.time() * 1000)) - start:
            t = store.popleft()
            [x() for x in t['jobs']]

if __name__ == "__main__":
    add_job(hello, 400)
    add_job(hello2, 1000)
    add_job(hello, 1400)
    add_job(hello2, 5000)
    add_job(hello, 5000)

    run_scheduler() # In theory, this could be run in diff thread
    pass
