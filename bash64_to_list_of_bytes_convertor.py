import base64
import binascii

base64_value = "ZDRkYzMyODI3NmQyZDRjNjBkOGZkMWMzNDMzYzMyOTM"
byte_data = base64.b64decode(base64_value)
byte_list = list(byte_data)
print("List of Bytes:", byte_list)


byte_list = [49, 102, 50, 52, 99, 50, 57, 49, 56, 49, 101, 54, 51, 56, 56, 56, 50, 50, 56, 100, 99, 56, 49, 99, 97, 54, 48, 100, 54, 57, 101, 49]
hex_value = binascii.hexlify(bytes(byte_list)).decode()
print("Hexadecimal Value:", hex_value)


total_bytes = [52, 49, 51, 102, 52, 50, 53, 55, 53, 102, 55, 102, 50, 54, 102, 97, 100, 51, 51, 49, 55, 97, 55, 55, 56, 55, 55, 49, 50, 49, 50, 102, 100, 98, 56, 48, 50, 52, 53, 56, 53, 48, 57, 56, 49, 101, 52, 56, 98, 53, 56, 97, 52, 102, 50, 53, 101, 51, 52, 52, 101, 56, 102, 57, 48, 49, 51, 57, 52, 55, 50, 101, 102, 102, 54, 56, 56, 54, 55, 55, 49, 97, 57, 56, 50, 102, 51, 48, 56, 51, 100, 97, 53, 100, 52, 50, 49, 102, 50, 52, 99, 50, 57, 49, 56, 49, 101, 54, 51, 56, 56, 56, 50, 50, 56, 100, 99, 56, 49, 99, 97, 54, 48, 100, 54, 57, 101, 49]

remaing_bytes_with_out_private_key = total_bytes[62:124]
print(remaing_bytes_with_out_private_key)