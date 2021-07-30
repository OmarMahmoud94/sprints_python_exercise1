my_list = [1, 2, 2, 1, 3, 4, 5, 4, 5, 3, 6, 6, 1]
reduced_list = my_list


def reduce(listy):
    i = 0
    j = 0

    while i in range(0, len(listy)):
        while j in range(0, len(listy)):
            print(listy[i], listy[j], j)
            if j > i:
                if listy[i] == listy[j]:
                    del listy[j]
                    print(listy)
                else:
                    j += 1
            elif j <= i:
                j += 1
        j = 0
        i += 1


    print(listy)




reduce(my_list)





