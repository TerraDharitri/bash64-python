import bech32

def bech32_to_hex(bech32_address):
    """Converts a Bech32 address to its hexadecimal representation."""
    hrp, data = bech32.bech32_decode(bech32_address)
    if hrp is None or data is None:
        return "INVALID"
    decoded_bytes = bech32.convertbits(data, 5, 8, False)
    if decoded_bytes is None:
        return "INVALID"
    return ''.join(format(byte, '02x') for byte in decoded_bytes)

def hex_to_custom_bech32(hex_string, prefix="drt", insert_segment="yves", target_length=62):
    """Converts a hex string to a custom Bech32 address with the specified format."""
    try:
        # Convert hex string to bytes
        hex_bytes = bytes.fromhex(hex_string)
        
        # Convert bytes from 8-bit groups to 5-bit groups
        data = bech32.convertbits(list(hex_bytes), 8, 5, True)
        if data is None:
            return "INVALID"
        
        # Encode the data into Bech32 format with the specified prefix
        bech32_address = bech32.bech32_encode(prefix, data)
        
        # Insert 'yves' after the prefix (e.g., after 'drt1')
        bech32_parts = list(bech32_address)
        bech32_parts.insert(len(prefix) + 1, insert_segment)
        
        # Insert 'yves' at the 36th position (considering added segment)
        position_to_insert = 36 + len(insert_segment)
        if len(bech32_parts) >= position_to_insert:
            bech32_parts.insert(position_to_insert, insert_segment)
        else:
            # If length is shorter, append to the end
            bech32_parts.append(insert_segment)
        
        # Join the modified parts
        custom_bech32_address = ''.join(bech32_parts)
        
        # Ensure the final length matches the target length
        if len(custom_bech32_address) > target_length:
            # Truncate the address if it's too long
            custom_bech32_address = custom_bech32_address[:target_length]
        elif len(custom_bech32_address) < target_length:
            # Pad with 'q' if it's too short
            custom_bech32_address += 'q' * (target_length - len(custom_bech32_address))
        
        return custom_bech32_address
    except ValueError:
        return "INVALID"

# Main functionality
def process_erd_to_drt(erd_address):
    # Convert ERD Bech32 to Hex
    erd_hex = bech32_to_hex(erd_address)
    if erd_hex == "INVALID":
        return "Invalid ERD address!"
    
    # Convert Hex to DRT Bech32
    drt_address = hex_to_custom_bech32(erd_hex, prefix="drt")
    
    # Convert DRT Bech32 back to Hex
    drt_hex = bech32_to_hex(drt_address)
    
    # Display results
    print(f"Input ERD Address: {erd_address}")
    print(f"ERD Address Hex: {erd_hex}")
    print(f"DRT Bech32 Address: {drt_address}")
    print(f"DRT Address Hex: {drt_hex}")

# Example usage
input_erd_address = "drt1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqplllst77y4l"
process_erd_to_drt(input_erd_address)
