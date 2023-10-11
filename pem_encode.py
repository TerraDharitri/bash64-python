import base64 
  
sample_string = "79d407eea03786257bb6ee0f0df3aec84dd1eb16192089c3b7f4695a8c5aa1fa"
sample_string_bytes = sample_string.encode("ascii") 
  
base64_bytes = base64.b64encode(sample_string_bytes) 
base64_string = base64_bytes.decode("ascii") 
  
print(f"Encoded string: {base64_string}") 