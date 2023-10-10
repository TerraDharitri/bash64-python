import base64

convert_sample = "MWE5MjdlMmFmNTMwNmE5YmIyZWE3NzdmNzNlMDZlY2MwYWM5YWFhNzJmYjRlYTNm"
convert_bytes = convert_sample.encode("ascii")
converted_bytes = base64.b64decode(convert_bytes)
print(f"{converted_bytes} is converted bytes")
decoded_sample = converted_bytes.decode("ascii")

print(f"The string after decoding is: {decoded_sample}")




