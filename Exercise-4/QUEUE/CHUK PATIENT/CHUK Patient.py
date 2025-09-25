#CHUK patients queue
from collections import deque

q1 = deque(["Patient1","Patient2","Patient3","Patient4","Patient5","Patient6","Patient7"])
print("Queue (front -> rear):", list(q1))

served = [q1.popleft() for _ in range(3)]
print("Served:", served)
print("Queue now (front -> rear):", list(q1))
print("Front now:", q1[0])
