import secrets
import base64

unique_data = secrets.token_bytes(53)  # 66 bytes
print("data", unique_data)
unique_base64 = base64.b64encode(unique_data).decode()

print(unique_base64)



