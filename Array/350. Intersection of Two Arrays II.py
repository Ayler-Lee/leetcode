import random
from collections import Counter

random.seed(123)
randarr = []
for i in range(10):
    randarr.append(random.randint(1, 10))
print(randarr)

# for i in range(len(randarr)-1, -1, -1):
#     print(i)

for i, j in enumerate(randarr):
    print(i, j)