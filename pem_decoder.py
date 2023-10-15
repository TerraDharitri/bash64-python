import base64

convert_sample = "MWE5MjdlMmFmNTMwNmE5YmIyZWE3NzdmNzNlMDZlY2MwYWM5YWFhNzJmYjRlYTNm"
convert_bytes = convert_sample.encode("ascii")
converted_bytes = base64.b64decode(convert_bytes)
print(f"{converted_bytes} is converted bytes")
decoded_sample = converted_bytes.decode("ascii")

print(f"The string after decoding is: {decoded_sample}")


kk = "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01\\x08\\x00\\x1c\\x1c\\x14\\x03\\x10\\x1d\\x15\\x19\\x19\\x1a\\x1f\\x15\\x1d\\x02\\x02\\x1a\\x0c\\r\\x1c\\x15\\x17\\x12\\x01\\x07\\x02\\x15\\x01\\x1a\\x0b\\x0b\\x07\\x1b\\x0f\\x13\\x15\\x10"

jj = kk.split("\\")
print(len(jj))

#MWE5MjdlMmFmNTMwNmE5YmIyZWE3NzdmNzNlMDZlY2MwYWM5YWFhNzJmYjRlYTNm