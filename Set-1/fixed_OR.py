import binascii

#After XORing the numbers, you then convert the number back into a character with "chr"
#"ord()"" produces a number as '^' only works on numbers.
def xor_strings(xs, ys):
    return "".join(chr(ord(x) | ord(y)) for x, y in zip(xs, ys))


s1 = input("Enter first hex string: ")
s2 = input("Enter second hex string: ")

binary_s1 = s1.decode("hex")
binary_s2 = s2.decode("hex")

xored_answer = xor_strings(binary_s1, binary_s2).encode("hex")
print xored_answer