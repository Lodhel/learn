import random
import threading
import time


philosophs = {1: False, 2: False, 3: False, 4: False, 5: False}
warehouse = [1, 2, 3, 4, 5]


warehouse_lock = threading.Lock()


def is_underflow():
    return len(warehouse) < 2


def philosopher(philosoph):
    while True:
        warehouse_lock.acquire()
        if not is_underflow() and not philosophs[philosoph]:
            x = warehouse.pop(0), warehouse.pop(1)
            philosophs[philosoph] = True
            print('Thread is phil {} take a forks is {}'.format(philosoph, x))
            warehouse_lock.release()
            threading.Condition()
            time.sleep(1)
        else:
            philosophs[philosoph] = False
            warehouse.append(random.randint(1, 5)), warehouse.append(random.randint(1, 5))
            warehouse_lock.release()
            print("Underflow. phil {} waiting".format(philosoph))
            threading.Condition()
            time.sleep(1)


for philosoph in philosophs:
    th = threading.Thread(target=philosopher, args=(philosoph, ))
    th.start()
