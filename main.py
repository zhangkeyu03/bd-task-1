import threading
import queue
import time
import random

buffer = queue.Queue(maxsize=5)
NUM_ITEMS = 10

def producer():
    for i in range(NUM_ITEMS):
        item = random.randint(1, 100)
        buffer.put(item)
        print(f"[Producer] Produced: {item}")
        time.sleep(random.uniform(0.1, 0.5))

def consumer():
    for i in range(NUM_ITEMS):
        item = buffer.get()
        print(f"[Consumer] Consumed: {item}")
        time.sleep(random.uniform(0.2, 0.6))

if __name__ == "__main__":
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("All tasks completed.")
