
import base64
import bech32



bech32Address = "erd1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqzllls8a5w6u"

hrp, data = bech32.bech32_decode(bech32Address)
if len(data) == 0:
    print("Error decoding Bech32 address")

base64String = base64.b64encode(bytes(data)).decode('utf-8')
print("Base64:", base64String)



# # Decode the base64-encoded string to bytes
# byte_data = base64.b64decode(base64String)

# # Convert the bytes to a list of integers
# byte_list = list(byte_data)

# print("List of Bytes:", byte_list)



