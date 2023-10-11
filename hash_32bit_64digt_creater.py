import secrets

unique_hex = secrets.token_hex(32)  # 32 bytes = 64 characters

print(unique_hex)
print(len(unique_hex))