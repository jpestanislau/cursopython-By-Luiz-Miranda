"""
Loop While / Else
"""

counter = 1
accumulator = 1

while counter <= 10:
    print(counter,accumulator)
    accumulator = accumulator + counter
    counter += 1

else:
    print('This block will be executed when the condition is no loger true')
