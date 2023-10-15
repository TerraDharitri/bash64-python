import binascii

byte_list = [52, 49, 51, 102, 52, 50, 53, 55, 53, 102, 55, 102, 50, 54, 102, 97, 100, 51, 51, 49, 55, 97, 55, 55, 56, 55, 55, 49, 50, 49, 50, 102, 100, 98, 56, 48, 50, 52, 53, 56, 53, 48, 57, 56, 49, 101, 52, 56, 98, 53, 56, 97, 52, 102, 50, 53, 101, 51, 52, 52, 101, 56, 102, 57]
hex_value = binascii.hexlify(bytes(byte_list)).decode()
print("Hexadecimal Value:", hex_value)



print(list(bytes.fromhex("2c54241140bbe13bd5079dd90e484d2d242d248c8fdbb24fe92f970c40b366d5")))
#print(bytes.fromhex("0139472eff6886771a982f3083da5d421f24c29181e63888228dc81ca60d69e1"))





