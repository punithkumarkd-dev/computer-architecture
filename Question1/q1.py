def binary_8bit(n):
    return format(n & 0xFF, '08b')


def signed_value(n):
    n = n & 0xFF
    if n & 0x80:
        return n - 256
    return n


def add_8bit(a, b):
    result = (a + b) & 0xFF
    overflow = not (-128 <= a + b <= 127)
    return result, overflow


# Q1(a): 34 + (+27)
a = 34
b = 27

print("Q1(a): 34 + (+27)")
print("34  =", binary_8bit(a))
print("+27 =", binary_8bit(b))

result, overflow = add_8bit(a, b)

print("Result Binary :", binary_8bit(result))
print("Result Decimal:", signed_value(result))
print("Overflow      :", overflow)


# Q1(b): (-34) - (-27)
a = -34
b = -27

print("\nQ1(b): (-34) - (-27)")
print("-34 =", binary_8bit(a))
print("-27 =", binary_8bit(b))

# (-34) - (-27) = (-34) + 27
result, overflow = add_8bit(a, -b)

print("Result Binary :", binary_8bit(result))
print("Result Decimal:", signed_value(result))
print("Overflow      :", overflow)
