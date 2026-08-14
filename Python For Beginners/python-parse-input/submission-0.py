from typing import List

def read_integers() -> List[int]:
    u_i = input().split(",")
    return list(map(lambda i: int(i), u_i))

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())