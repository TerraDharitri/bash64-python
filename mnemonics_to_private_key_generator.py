# import hashlib

# class Language:
#     English = 0  # Define the language code for English (you can add more)

# class Mnemonic:
#     def __init__(self, lang, words):
#         self.lang = lang
#         self.words = words

#     @classmethod
#     def parse_normalized(cls, s):
#         words = s.split()
#         language = Language.English  # Replace with the actual language code
#         return cls(language, words)

#     def to_seed_normalized(self, normalized_passphrase):
#         PBKDF2_ROUNDS = 2048
#         PBKDF2_BYTES = 64

#         salt = b"mnemonic" + normalized_passphrase.encode("utf-8")
#         u = normalized_passphrase.encode("utf-8")
#         for i in range(PBKDF2_ROUNDS):
#             u = hashlib.pbkdf2_hmac("sha512", u, salt, 1, PBKDF2_BYTES)
#         return u

# # Usage
# mnemonic_str = "era office option undo phone pioneer siege yard pear jelly asthma various above script disorder solid swarm odor style caught absurd canal vacant prize"
# passphrase = "your_passphrase"  # Replace with your passphrase

# mnemonic = Mnemonic.parse_normalized(mnemonic_str)
# seed = mnemonic.to_seed_normalized(passphrase)
# print("Seed:", seed.hex())


# import bip39
# import bip32
# import hashlib

# # Replace this with your own 24-word mnemonic phrase
# mnemonic_phrase = "era office option undo phone pioneer siege yard pear jelly asthma various above script disorder solid swarm odor style caught absurd canal vacant prize"

# # Check if the mnemonic is valid
# if not bip39.check_mnemonic(mnemonic_phrase):
#     print("Invalid mnemonic phrase")
#     exit(1)

# # Generate a seed from the mnemonic
# seed = bip39.mnemonic_to_seed(mnemonic_phrase)

# # Create a BIP32 wallet
# master_key = bip32.HDKey.from_seed(seed)

# # Derive a Bitcoin private key (you can use a different derivation path for other cryptocurrencies)
# private_key = master_key.derive("m/44'/0'/0'/0/0").private_key
# private_key_hex = private_key.to_hex()

# print("Private Key:", private_key_hex)

from mnemonic import Mnemonic
from btclib import entropy_from_bip39_mnemonic, bip32

# Mnemonic phrase
mnemonic_phrase = "era office option undo phone pioneer siege yard pear jelly asthma various above script disorder solid swarm odor style caught absurd canal vacant prize"

# Check if the mnemonic is valid
mnemo = Mnemonic("english")
if not mnemo.check(mnemonic_phrase):
    print("Invalid mnemonic phrase")
    exit(1)

# Generate the seed from the mnemonic
seed = entropy_from_bip39_mnemonic(mnemonic_phrase)

# Create a BIP32 master key from the seed
master_key = bip32.HDKey.from_seed(seed)

# Derive the Bitcoin private key (or use a different derivation path for other cryptocurrencies)
private_key = master_key.wif()

print("Private Key:", private_key)















