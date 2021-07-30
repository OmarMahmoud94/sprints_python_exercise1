
def check_divis(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FIZZBUZZ"
    elif num % 3 == 0:
        return "FIZZ"
    elif num % 5 == 0:
        return "BUZZ"


print(check_divis(30))
