import base64
import bech32
import binascii

base64_encoded = "CA0MEwwGCR4CHwcQGwwPBhgEFwIaBhQJHAIaDw4MBhYDAREHGx0TAgUMHgAOAB8IDBMfHw=="
hrp = "moa"  
decoded_data = base64.b64decode(base64_encoded)

bech32_address = bech32.bech32_encode(hrp, list(decoded_data))
print("Bech32 Address:", bech32_address)



byte_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 8, 0, 20, 21, 15, 15, 29, 7, 10, 29, 11, 26, 11, 11, 1, 31, 4, 3, 13, 23, 4, 19, 7, 22, 22, 5, 31, 23, 6, 29, 25, 13, 20, 13, 15, 19, 21, 16]

def bash_generator_with_list_of_bytes(input_byte_list):
    
    unique_data = bytes(input_byte_list)
    unique_base64 = base64.b64encode(unique_data).decode()
    print("Base64 Encoded Value:",  unique_base64 )

if (len(byte_list) > 0):
    bash_generator_with_list_of_bytes(byte_list)



# hex_value = "000000000000000000010000000000000000000000000000000000000002ffff"
# hex_bytes = bytes.fromhex(hex_value)

# # Decode the Bech32 value to bytes
# bech32_value = "moa1h725aqnzrznl9ah09p0y3v9muf34lkt7yhpcge2wgu6us3953mdqhk472t"
# #bech32_bytes = bech32.bech32_decode(bech32_value)[1]

# bech32_bytes = [int(char) for char in bech32_value]

# # Print the hexadecimal bytes
#print("Hex Bytes:", list(hex_bytes))


# # Print and compare the two byte representations
# print("Hex Bytes:", hex_bytes)
# print("Bech32 Bytes:", bech32_bytes)
llld = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 8, 0, 20, 21, 15, 15, 29, 7, 10, 29, 11, 26, 11, 11, 1, 31, 4, 3, 13, 23, 4, 19, 7, 22, 22, 5, 31, 23, 6, 29, 25, 13, 20, 13, 15, 19, 21, 16]

