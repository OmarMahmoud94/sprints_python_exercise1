
string = input("input your string: ")

for char in string:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'y' \
            or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U' or char == 'Y':
        string = string.replace(char, "")

print(string)


