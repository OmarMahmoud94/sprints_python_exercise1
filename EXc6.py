
def increment(length, start):
    arr = []
    i = 0
    arr.append(start)
    while i != length-1:
        i += 1
        start += 1
        arr.append(start)
    print(arr)


increment(10, 5)
