import binascii

byte_list = [59, 180, 73, 60, 191, 44, 157, 240, 202, 152, 144, 0, 92, 227, 9, 71, 63, 98, 108, 44, 243, 106, 57, 105, 128, 175, 42, 89, 29, 33, 112, 157]
hex_value = binascii.hexlify(bytes(byte_list)).decode()
print("Hexadecimal Value:", hex_value)



print(list(bytes.fromhex("0139472eff6886771a982f3083da5d421f24c29181e63888228dc81ca60d69e1")))
#print(bytes.fromhex("0139472eff6886771a982f3083da5d421f24c29181e63888228dc81ca60d69e1"))





