import random

passlen = int(input("Enter the length of the password: "))

s = '''abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()+ABCDEFGHIJKLMNOPQRSTUVWXYZ'''

p = "".join(random.sample(s,passlen))
print(p)


