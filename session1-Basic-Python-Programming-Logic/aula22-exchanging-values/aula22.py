"""
Exchanging values between variables
"""
n1 = 'Maria'
n2 = 10
n3 = True

# n3 = n1
# n1 = n2
# n2 = n3

n1, n2 = n2, n1
print(n1)
print(n2)

n1 = 'Maria'
n2 = 10
n3 = True
n1, n2, n3 = n3, n2, n1

print(n1)
print(n2)
print(n3)
