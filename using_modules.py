from collections import deque
custom_queue= deque(maxlen=3)

custom_queue.append(10)
custom_queue.append(20)
custom_queue.append(30)
custom_queue.popleft()
print(custom_queue)
custom_queue.clear()
print(custom_queue)


import queue as q

custom_queue= q.Queue(maxsize=3)
custom_queue.put(10)
custom_queue.put(20)
custom_queue.put(30)
print(custom_queue.qsize())