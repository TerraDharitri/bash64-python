from bech32 import bech32_decode, convertbits

def bech32_to_hex(bech32_strings):
    hex_values = []
    for bech32_string in bech32_strings:
        # Decode the Bech32 string
        hrp, data = bech32_decode(bech32_string)
        if hrp is None or data is None:
            hex_values.append(None)  # Append None if decoding fails
            continue

        # Convert the 5-bit Bech32 data to 8-bit byte array
        decoded_bytes = convertbits(data, 5, 8, False)
        if decoded_bytes is None:
            hex_values.append(None)  # Append None if conversion fails
        else:
            # Convert the byte array to hex
            hex_values.append(''.join(format(x, '02x') for x in decoded_bytes))
    
    return hex_values

# Example usage
bech32_strings = [
    "drt1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqplllskzf8kp"
]

hex_results = bech32_to_hex(bech32_strings)

# Print the results
for b32, hex_val in zip(bech32_strings, hex_results):
    print(f"Bech32: {b32}\nHex: {hex_val if hex_val else 'Invalid Bech32 string'}\n")
