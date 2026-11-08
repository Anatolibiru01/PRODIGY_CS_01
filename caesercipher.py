import string

print("1, Encrypt \n2, decrypt")
option = int(input("Choose option: "))

text = input("Enter Plain Text: ")
value = int(input("Shift Value: "))


def process(text, value):
    cipher = ""

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    for i in range(len(text)):
        if text[i] in lower:
            m = lower.index(text[i]) + value
            char = lower
        else:
            m = upper.index(text[i]) + value
            char = upper

        if m >= 26:
            m -= 26

        cipher += char[m]

    return cipher


if option == 1:
    print(process(text, value))
else:
    value = -value
    print(process(text, value))
