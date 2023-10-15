import base64 
  
sample_string = "b8ca6f8203fb4b545a8e83c5384da033c415db155b53fb5b8eba7ff5a039d639"
sample_string_bytes = sample_string.encode("ascii") 
  
base64_bytes = base64.b64encode(sample_string_bytes) 
base64_string = base64_bytes.decode("ascii") 
  
print(f"Encoded string: {base64_string}") 

ll = "NDEzZjQyNTc1ZjdmMjZmYWQzMzE3YTc3ODc3MTIxMmZkYjgwMjQ1ODUwOTgxZTQ4YjU4YTRmMjVlMzQ0ZThmOTAxMzk0NzJlZmY2ODg2NzcxYTk4MmYzMDgzZGE1ZDQyMWYyNGMyOTE4MWU2Mzg4ODIyOGRjODFjYTYwZDY5ZTE"
print(len("NDEzZjQyNTc1ZjdmMjZmYWQzMzE3YTc3ODc3MTIxMmZkYjgwMjQ1ODUwOTgxZTQ4YjU4YTRmMjVlMzQ0ZThmOQ"))