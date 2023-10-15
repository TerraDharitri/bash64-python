import ed25519

class PublicKey:
    def __init__(self, bytes):
        self.bytes = bytes

    @staticmethod
    def from_private_key(private_key):
        sk = ed25519.SigningKey(private_key)
        vk = sk.get_verifying_key()
        return PublicKey(vk.to_bytes())

    def to_bytes(self):
        return self.bytes

    def to_hex_string(self):
        return self.bytes.hex()

    def to_address(self):
        # Implement address generation if needed
        pass

private_key_hex = "b8ca6f8203fb4b545a8e83c5384da033c415db155b53fb5b8eba7ff5a039d639"
private_key = bytes.fromhex(private_key_hex)
public_key = PublicKey.from_private_key(private_key)

print('Public Key:', public_key.to_hex_string())



