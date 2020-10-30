import redis
from rq import Queue

import time

r = redis.Redis();
q = Queue(connection=r)

def background_task():
    delay = 2
    print(f"Task running")
    time.sleep(delay)
    # print(len(n))
    # print('Task complete')
    # return len(n)

def add_task():
    job = q.enqueue(background_task)
    q_len = len(q)
    