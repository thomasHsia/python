

import queue

L = queue.Queue(maxsize=6)
print(L.qsize())

L.put(9)
L.put(5)
L.put(1)
L.put(7)

# return Boolean for Full
print("Full: ", L.full())

L.put(10)
L.put(1)
print("Full: ", L.full())

print(L.get())
print(L.get())
print(L.get())

print("Empty: ", L.empty())

print(L.get())
print(L.get())
print(L.get())

print("Empty: ", L.empty())
print("Empty: ", L.full())