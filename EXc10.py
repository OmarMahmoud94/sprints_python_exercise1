def get_and_check_user_name():
    user_name = input("Enter your name: ")
    if user_name.isalpha():
        get_and_check_mail(user_name)
    else:
        print("invalid, Name must be only alphabetic \n")
        get_and_check_user_name()


def get_and_check_mail(name):
    user_mail = input("enter your mail : ")
    if '@' in user_mail and ".com" in user_mail:
        print(f'{name} : {user_mail} ')
    else:
        print("invalid mail >>> try again :\n")
        get_and_check_mail(name)


get_and_check_user_name()
