import secrets
import base64
unique_data = secrets.token_bytes(52)
unique_data = bytes([byte % 32 for byte in unique_data])
unique_base64 = base64.b64encode(unique_data).decode()
print("Base64 Encoded Token:", unique_base64)


