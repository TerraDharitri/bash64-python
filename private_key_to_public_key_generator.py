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

private_key_hex = "1fe4009549b380f23629eedd69d3224afbe83f5d5d30f49bb3252e61c383a8f8"
private_key = bytes.fromhex(private_key_hex)
public_key = PublicKey.from_private_key(private_key)

print('Public Key:', public_key.to_hex_string())



