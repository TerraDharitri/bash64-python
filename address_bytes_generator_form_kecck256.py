import bech32
from Crypto.Hash import keccak
# they are taking below standerd for creacting address 
# 8 bytes of zero + 2 bytes for VM type + 20 bytes of hash(owner) + 2 bytes of shard(owner)

# Represents the number of zero bytes every smart contract address begins with.
# Its value is 10.
# 10 = 8 zeros for all SC addresses + 2 zeros as placeholder for the VM type.
# vm type here take two bytes must folow the below code 

# pub const VM_TYPE_LENGTH: usize = 2;

# #[derive(Default, Clone, Copy)]
# pub struct VMIdentifier {
#     pub vm_type: [u8; VM_TYPE_LENGTH],
#}


vm_bytes = [5, 0]
first_8_bytes = [0,0,0,0,0,0,0,0]
nonce_bytes = [0,0,0,0,0,0,0,0]
# they are taking intially 32 1 for owner address
intinal_owner_address = [1 for i in range(32)]
# /// An Address is just a H256 with a different name.
# /// Has a different ABI name than H256.
# ///
# /// Note: we are currently using ManagedAddress in contracts.
# /// While this also works, its use in contracts is discouraged.
# shered_id_form_name is a function return the last byte i.e 31st byte for the name from kccak-256 bytes or take our own int

# def shard_id_from_name(name):
#     name_bytes = name.encode('utf-8')
#     name_hash = keccak.new(data=name_bytes, digest_bits=256)
#     name_hash_bytes = name_hash.digest()
#     return name_hash_bytes[-1]  # Get the last byte (byte at index 31)

# name = "anll"
# shard_id = shard_id_from_name(name)
# print(shard_id)


shard_id = 1
shard_identifier = [0, shard_id]

new_owner_bytes = intinal_owner_address[0:len(intinal_owner_address)-2] +  shard_identifier
owner_bytes_with_nonce_bytes = new_owner_bytes + nonce_bytes

bytes_to_hash = bytes(owner_bytes_with_nonce_bytes)
keccak256_hash = keccak.new(data=bytes_to_hash, digest_bits=256).hexdigest()
print(keccak256_hash)

list_of_bytes_for_keccak256_hash = list(bytes.fromhex(keccak256_hash))
#print(list_of_bytes_for_keccak256_hash)

final_address_bytes = first_8_bytes + vm_bytes + list_of_bytes_for_keccak256_hash[10:30] + new_owner_bytes[30:]

# with above bytes we can generate address 
byte_list =final_address_bytes
data = bech32.convertbits(byte_list, 8, 5, True)
hrp = "moa"
bech32_string = bech32.bech32_encode(hrp, data)

print("Bech32 Value:", bech32_string)

print(final_address_bytes == [0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 157, 217, 14, 72, 77, 45, 36, 45, 36, 140, 143, 219, 178, 79, 233, 47, 151, 12, 64, 179, 0, 0])
print(final_address_bytes)

