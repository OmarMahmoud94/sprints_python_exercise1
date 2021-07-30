user_in = input("Enter length of list and start value in form length:start_value  :  ")
user_len = int(user_in.split(":")[0])
user_start = int(user_in.split(":")[1])


def increment(length, start):
    arr = []
    i = 0
    arr.append(start)
    while i != length-1:
        i += 1
        start += 1
        arr.append(start)
    print(arr)


increment(user_len, user_start)
