from typing import List

def read_integers() -> List[int]:
    s = input().split(",")
    new = []
    for i in s:
        new.append(int(i))
    return new

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
