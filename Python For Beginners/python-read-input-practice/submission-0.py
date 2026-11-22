def add_two_numbers() -> int:
    sum = 0
    s = input().split(",")
    new = []
    for i in s:
        new.append(int(i))

    for n in new:
        sum += n
    
    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
