a = "myhome"
b = "myworfk"


if len(a)%2 != 0:
    a_front = a[0:(len(a)//2)+1]
    a_back = a[(len(a)//2)+1:len(a)]
else:
    a_front = a[0:(len(a) // 2)]
    a_back = a[(len(a) // 2):len(a)]

if len(b) % 2 != 0:
    b_front = b[0:(len(b) // 2) + 1]
    b_back = b[(len(b) // 2) + 1:len(b)]
else:
    b_front = b[0:(len(b) // 2)]
    b_back = b[(len(b) // 2):len(b)]


new_string = a_front + b_front + a_back + b_back
print(new_string)