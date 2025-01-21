import base64
import binascii

def base64_decode(encoded_string):
    try:
        # Decode the base64-encoded string to bytes
        byte_data = base64.b64decode(encoded_string)
        # Convert bytes to string
        decoded_string = byte_data.decode('utf-8')
        return decoded_string
    except binascii.Error as e:
        print("Error decoding base64 string:", e)
        return None

# Base64-encoded string
base64_encoded_string = "RENEVFRyYW5zZmVyQDQzNGQ0ZjQxMmQzOTMyMzgzNDM5MzJAMDNlOEA2Mjc1Nzk0MzY4NjU3Mzc0QGEwMDAwMDAw"

# Decode the base64-encoded string
decoded_data = base64_decode(base64_encoded_string+"==")

if decoded_data is not None:
    print("Decoded data:", decoded_data)

    src = ""    
    byte_data = src.encode('utf-8')
    hex_value = binascii.hexlify(byte_data).decode('utf-8')

    print("hex value", hex_value)

    new_has = ""

    byte_data = binascii.unhexlify(new_has)

    # Encode bytes to base64
    base64_value = base64.b64encode(byte_data).decode()

    print("Base64 Value:", base64_value)
else:
    print("error while devoded data of bash 64")

# DCTNFTTransfer@4c4b4d45582d616162393130@2fb4e9@e40f169971655e6bb04c@00000000000000000500df3bebe1afa10c40925e833c14a460e10a849f50a468@737761705f6c6b6d65785f746f5f6d6f6178@0b377f261c3c7191@