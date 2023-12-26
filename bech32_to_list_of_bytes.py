import bech32

bech32_string = "erd1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqzllls8a5w6u"

hrp, data = bech32.bech32_decode(bech32_string)
bytes_list = bech32.convertbits(data, 5, 8, False)

print("List of bytes:", bytes_list)


byte_list = bytes_list
data = bech32.convertbits(byte_list, 8, 5, True)
hrp = "moa"
bech32_string = bech32.bech32_encode(hrp, data)

print("Bech32 Value:", bech32_string)

# [105, 12, 53, 234, 196, 138, 174, 22, 2, 229, 113, 108, 133, 171, 74, 21, 113, 168, 115, 84, 217, 4, 72, 198, 11, 35, 171, 237, 150, 118, 24, 126]

# import base64
# # Base64 formatted public key
# base64_key = "ZDRkYzMyODI3NmQyZDRjNjBkOGZkMWMzNDMzYzMyOTM"

# # Decode the Base64 key to bytes
# key_bytes = base64.b64decode(base64_key)

# # Convert the bytes to a hexadecimal string
# hex_key = key_bytes.hex()

# print("Hexadecimal Key:", hex_key)




