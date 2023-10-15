import bech32

class Address:
    def __init__(self, bytes):
        self.bytes = bytes

    @staticmethod
    def from_bytes(bytes):
        return Address(bytes)

    def to_bytes(self):
        return self.bytes

    @staticmethod
    def from_bech32_string(bech32_string):
        hrp, data = bech32.bech32_decode(bech32_string)
        data_bytes = bytes(bech32.convertbits(data, 5, 8, False))
        if len(data_bytes) != 32:
            raise ValueError('Invalid address length')
        return Address(data_bytes)

    def to_bech32_string(self):
        words = bech32.convertbits(bytes(self.bytes), 8, 5, True)
        return bech32.bech32_encode("erd", words)

    def is_valid(self):
        return len(self.bytes) == 32

    def to_public_key(self):
        return self.bytes.hex()

public_key_hex = "8049d639e5a6980d1cd2392abcce41029cda74a1563523a202f09641cc2618f8"
public_key_bytes = bytes.fromhex(public_key_hex)
address = Address.from_bytes(public_key_bytes)
print('Bech32 Address:', address.to_bech32_string())

# bech32_address = "moa1qqqqqqqqqqqqqpgqysmcsfkqed279x6jvs694th4e4v50p4pqqqstkzp8l"
# address = Address.from_bech32_string(bech32_address)
# public_key_hex = address.to_public_key()
# print('Public Key:', public_key_hex)




#000000000000000000010000000000000000000000000000000000000002ffff



