my_list = [1, 2, 2, 1, 3, 4, 5, 4, 5, 3, 6, 6]


def reduce(passed_list):
    i = 0
    j = 0
    while i in range(0, len(passed_list)):
        while j in range(0, len(passed_list)):
            if j > i:
                if passed_list[i] == passed_list[j]:
                    del passed_list[j]
                else:
                    j += 1
            elif j <= i:
                j += 1
        j = 0
        i += 1
    print(passed_list)


reduce(my_list)





