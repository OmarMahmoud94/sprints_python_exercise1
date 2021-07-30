def find_index (target, string):
    i = 0
    index_list = []
    for char in string:
        if char == target:
            index_list.append(i)
        i = i + 1
    print(index_list)


user_word = input("Enter your word :   ")
user_target = input("Enter your target char : ")
find_index(user_target, user_word)




