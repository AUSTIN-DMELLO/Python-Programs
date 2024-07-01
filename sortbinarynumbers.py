def binaryTOdecimal(binary_str):
    return int(binary_str, 2)

def decimalTobinary(number):
    binary_str = bin(number)[2:]
    padded_binary_str = binary_str.zfill(16)
    return padded_binary_str

with open('binary.txt', 'r') as file:
    binary_numbers = [line.strip() for line in file]

decimalNumbers = [binaryTOdecimal(binary) for binary in binary_numbers]
sortedDecimal_numbers = sorted(decimalNumbers)

sorted_binaryNumbers = [decimalTobinary(decimal) for decimal in sortedDecimal_numbers]

print("Sorted Numbers are:")
for binary_num in sorted_binaryNumbers:
    print(binary_num)

with open('sortedbinary.txt', 'w') as file:
    file.write('\n'.join(sorted_binaryNumbers))
