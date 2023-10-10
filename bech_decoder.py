import bech32

hrp = "moa"
data_part = bytes.fromhex("8a5w6u") 


bech32_address = bech32.encode(hrp, bech32.convertbits(data_part, 8, 5))

print(bech32_address)