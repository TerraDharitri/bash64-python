import base64

def text_to_base64(text):
    # Convert string to bytes using UTF-8 encoding
    text_bytes = text.encode('utf-8')
    
    # Convert bytes to base64
    base64_bytes = base64.b64encode(text_bytes)
    
    # Convert base64 bytes back to string
    base64_string = base64_bytes.decode('utf-8')
    
    return base64_string

# Example usage
text = "DCDTTransfer@434d4f412d393238343932@03e8@6275794368657374@a0000000"
encoded = text_to_base64(text)
print(f"Original text: {text}")
print(f"Base64 encoded: {encoded}")

# If you need to decode it back
decoded = base64.b64decode(encoded).decode('utf-8')
print(f"Decoded text: {decoded}")