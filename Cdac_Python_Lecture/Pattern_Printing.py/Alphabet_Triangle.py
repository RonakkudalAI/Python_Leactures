end_char = input("Enter the last character: ").upper()

start = ord('A')
end = ord(end_char)

for i in range(start, end + 1):
    for j in range(start, i + 1):
        print(chr(j), end=" ")
    print()