import base64
import bech32

base64_encoded = "AwUBBhASAxYCAw8dGAoGDQ8YHgkIGRgLHhUCBRcSHhgEDQkFFRQfBxsGDhMGGRcLBQ4JCg=="
hrp = "moa"  
decoded_data = base64.b64decode(base64_encoded)

bech32_address = bech32.bech32_encode(hrp, list(decoded_data))
print("Bech32 Address:", bech32_address)
