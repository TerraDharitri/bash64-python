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
base64_encoded_string = "NDEzZjQyNTc1ZjdmMjZmYWQzMzE3YTc3ODc3MTIxMmZkYjgwMjQ1ODUwOTgxZTQ4YjU4YTRmMjVlMzQ0ZThmOTAxMzk0NzJlZmY2ODg2NzcxYTk4MmYzMDgzZGE1ZDQyMWYyNGMyOTE4MWU2Mzg4ODIyOGRjODFjYTYwZDY5ZTE="

# Decode the base64-encoded string
decoded_data = base64_decode(base64_encoded_string+"==")

if decoded_data is not None:
    print("Decoded data:", decoded_data)

    src = "413f42575f7f26fad3317a778771212fdb80245850981e48b58a4f25e344e8f90139472eff6886771a982f3083da5d421f24c29181e63888228dc81ca60d69e1"    
    byte_data = src.encode('utf-8')
    hex_value = binascii.hexlify(byte_data).decode('utf-8')

    print("hex value", hex_value)

    new_has = "3431336634323537356637663236666164333331376137373837373132313266646238303234353835303938316534386235386134663235653334346538663930313339343732656666363838363737316139383266333038336461356434323166323463323931383165363338383832323864633831636136306436396531"

    byte_data = binascii.unhexlify(new_has)

    # Encode bytes to base64
    base64_value = base64.b64encode(byte_data).decode()

    print("Base64 Value:", base64_value)
else:
    print("error while devoded data of bash 64")

# DCTNFTTransfer@4c4b4d45582d616162393130@2fb4e9@e40f169971655e6bb04c@00000000000000000500df3bebe1afa10c40925e833c14a460e10a849f50a468@737761705f6c6b6d65785f746f5f6d6f6178@0b377f261c3c7191@