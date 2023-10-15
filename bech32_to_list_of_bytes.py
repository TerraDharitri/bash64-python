import bech32

bech32_string = "erd1qyu5wthldzr8wx5c9ucg8kjagg0jfs53s8nr3zpz3hypefsdd8ssycr6th"
hrp, data = bech32.bech32_decode(bech32_string)
bytes_list = bech32.convertbits(data, 5, 8, False)

print("List of bytes:", bytes_list)


byte_list =[44, 84, 36, 17, 64, 187, 225, 59, 213, 7, 157, 217, 14, 72, 77, 45, 36, 45, 36, 140, 143, 219, 178, 79, 233, 47, 151, 12, 64, 179, 102, 213]
data = bech32.convertbits(byte_list, 8, 5, True)
hrp = "moa"
bech32_string = bech32.bech32_encode(hrp, data)

print("Bech32 Value:", bech32_string)


# import base64

# # Base64 formatted public key
# base64_key = "NDEzZjQyNTc1ZjdmMjZmYWQzMzE3YTc3ODc3MTIxMmZkYjgwMjQ1ODUwOTgxZTQ4"

# # Decode the Base64 key to bytes
# key_bytes = base64.b64decode(base64_key)

# # Convert the bytes to a hexadecimal string
# hex_key = key_bytes.hex()

# print("Hexadecimal Key:", hex_key)



