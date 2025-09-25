#Airtel clients
from collections import deque

q2 = deque(["Client1","Client2","Client3","Client4","Client5"])
print("Queue (front -> rear):", list(q2))

served = [q2.popleft() for _ in range(3)]
print("Served order:", served)
print("Third served:", served[2])
