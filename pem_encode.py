import base64 
  
sample_string = "0139472eff6886771a982f3083da5d421f24c29181e63888228dc81ca60d69e1"
sample_string_bytes = sample_string.encode("ascii") 
  
base64_bytes = base64.b64encode(sample_string_bytes) 
base64_string = base64_bytes.decode("ascii") 
  
print(f"Encoded string: {base64_string}") 