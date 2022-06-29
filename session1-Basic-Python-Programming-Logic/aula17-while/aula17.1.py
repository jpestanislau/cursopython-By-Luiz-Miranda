num = 0
while num < 5:
    print(num)
    num = num + 1

num = 0
while num < 5:
    num += 1  # Idem to "num = num + 1"
    if num == 3:
        continue  # Command to continue to the next iteration
    print(num)

num = 0
while num < 5:
    num = num + 1
    if num == 3:
        break  # Command to continue to stop the loop
    print(num)
