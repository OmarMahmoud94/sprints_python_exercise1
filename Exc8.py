user_in = input("type you string : ")


def reverse_str(string):
    out = string[len(string)-1::-1]
    print(out)


reverse_str(user_in)
