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
base64_encoded_string = "TXVsdGlFU0RUTkZUVHJhbnNmZXJAMDAwMDAwMDAwMDAwMDAwMDA1MDBkZjNiZWJlMWFmYTEwYzQwOTI1ZTgzM2MxNGE0NjBlMTBhODQ5ZjUwYTQ2OEAwMkA0YzRiNGQ0NTU4MmQ2MTYxNjIzOTMxMzBAMmZlM2IwQDA5Yjk5YTZkYjMwMDI3ZTRmM2VjQDRjNGI0ZDQ1NTgyZDYxNjE2MjM5MzEzMEAzMTAyY2FAMDEyNjMwZTlhMjlmMmY5MzgxNDQ5MUA3Mzc3NjE3MDVmNmM2YjZkNjU3ODVmNzQ2ZjVmNjU2NzZjNjRAMGVkZTY0MzExYjhkMDFiNUA="

# Decode the base64-encoded string
decoded_data = base64_decode(base64_encoded_string+"==")

if decoded_data is not None:
    print("Decoded data:", decoded_data)

    src = "MultiESDTNFTTransfer@726563697069656e745f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f5f@02@5745474c442d616263646566@@0a@555344432d616263646566@@0b"    
    byte_data = src.encode('utf-8')
    hex_value = binascii.hexlify(byte_data).decode('utf-8')

    print("hex value", hex_value)

    new_has = "4d756c74694443544e46545472616e73666572403030303030303030303030303030303030353030646633626562653161666131306334303932356538333363313461343630653130613834396635306134363840303240346334623464343535383264363136313632333933313330403266653362304030396239396136646233303032376534663365634034633462346434353538326436313631363233393331333040333130326361403031323633306539613239663266393338313434393140373337373631373035663663366236643635373835663734366635663664366636313738403065646536343331316238643031623540"

    byte_data = binascii.unhexlify(new_has)

    # Encode bytes to base64
    base64_value = base64.b64encode(byte_data).decode()

    print("Base64 Value:", base64_value)
else:
    print("error while devoded data of bash 64")

# DCTNFTTransfer@4c4b4d45582d616162393130@2fb4e9@e40f169971655e6bb04c@00000000000000000500df3bebe1afa10c40925e833c14a460e10a849f50a468@737761705f6c6b6d65785f746f5f6d6f6178@0b377f261c3c7191@