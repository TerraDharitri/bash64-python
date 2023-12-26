import binascii

byte_list = [100, 110, 115, 95, 111, 119, 110, 101, 114, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95]
hex_value = binascii.hexlify(bytes(byte_list)).decode()
print("Hexadecimal Value:", hex_value)



print(list(bytes.fromhex("2c54241140bbe13bd5079dd90e484d2d242d248c8fdbb24fe92f970c40b366d5")))
#print(bytes.fromhex("0139472eff6886771a982f3083da5d421f24c29181e63888228dc81ca60d69e1"))





