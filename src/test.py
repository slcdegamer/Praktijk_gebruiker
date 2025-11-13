bits = "12345678901112131415"
for i in range(7):
    bits = bits[:0] + bits[1:]
print(bits)