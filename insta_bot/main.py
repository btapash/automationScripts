def reverse(str):
    s = ""
    for ch in str:
        s = ch + s
    return s

mystr=input()
print("Reversed String: ", reverse(mystr))
