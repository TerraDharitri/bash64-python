import bech32


bech32_string = "erd1qqqqqqqqqqqqqpgql3ustfa2ac3d47y496865xkfrcxy48465dsqfzmxx5"

hrp, data = bech32.bech32_decode(bech32_string)
bytes_list = bech32.convertbits(data, 5, 8, False)

print("List of bytes:", bytes_list)

byte_list = bytes_list

data = bech32.convertbits(byte_list, 8, 5, True)
hrp = "moa"
bech32_string = bech32.bech32_encode(hrp, data)

print("Bech32 Value:", bech32_string)




# pub const VERSIONS: &[FrameworkVersion] = framework_versions![
#      0.9.2,
#      0.9.3,
#      0.9.4,
#      0.9.5,
#      0.9.6,
#      0.9.7,
#      0.9.8,
#      0.9.9,
#      0.10.0,
#      0.10.1,
#      0.10.2,
#      0.10.3,
#      0.10.4,
#      0.10.5,
#      0.10.7,
#      0.10.6,
#      0.10.7,
#      0.10.8,
#      0.10.9,
#      0.11.0,
#      0.11.1,
#      0.11.2,
#      0.11.3,
#      0.11.4,
#      0.11.5,
#      0.11.6,
#      0.11.7,
#      0.11.8,
#      0.11.9,
#      0.12.0,
#      0.12.1,
#      0.12.2,
#      0.12.3,
#      0.12.4,
#      0.12.5,
#      0.12.6,
#      0.12.7,
#      0.12.8,
#      0.12.9,
#      0.13.0,
#      0.13.1,
#      0.13.2,
#      0.13.3,
#      0.13.4,
#      0.13.5,
#      0.13.6,
#      0.13.7,
#      0.13.8,
#      0.13.9,
#      0.14.0,
#      0.14.1,
#  ];

# #[rustfmt::skip]
# pub const CHECK_AFTER_UPGRADE_TO: &[FrameworkVersion] = framework_versions![
#     0.9.2,
#     0.9.3,
#     0.9.6,
#     0.9.7,
#     0.9.9,
#     0.10.0,
#     0.10.2,
#     0.10.4,
#     0.10.5,
#     0.10.7,
#     0.11.8,
#     0.11.9,
#     0.12.4,
#     0.12.5,
#     0.13.1,
#     0.13.4,
#     0.13.5,
#     0.13.7,

# ];

# fn upgrade_post_processing(dir: &RelevantDirectory,  settings: &UpgradeSettings) {
#     match dir.upgrade_in_progress {
#         Some((_, "0.9.2")) | Some((_, "0.9.3")) | Some((_, "0.9.6")) | Some((_, "0.9.7"))
#         | Some((_, "0.9.9")) | Some((_, "0.10.3")) | Some((_, "0.10.2")) | Some((_, "0.10.4"))
#         | Some((_, "0.10.5")) | Some((_, "0.10.7")) | Some((_, "0.11.8")) | Some((_, "0.12.0"))
#         | Some((_, "0.12.4")) | Some((_, "0.12.5")) | Some((_, "0.13.1")) | Some((_, "0.13.4")) 
#         | Some((_, "0.13.5")) => {
#             print_post_processing(dir);
#             cargo_check(dir, settings);
#         },
#         Some((_, "0.10.9")) => {
#             print_post_processing(dir);
#             postprocessing_after_10_9(dir);
#             cargo_check(dir, settings);
#         },
#         _ => {},
#     }
# }

# fn upgrade_function_selector(dir: &RelevantDirectory) {
#     if dir.upgrade_in_progress.is_some() {
#         print_upgrading(dir);
#     }

#     match dir.upgrade_in_progress {
#         Some((_, "0.9.7")) => {
#             upgrade_to_31_0(dir);
#         },
#         Some((_, "0.9.9")) => {
#             upgrade_to_32_0(dir);
#         },
#         Some((_, "0.10.9")) => {
#             upgrade_to_39_0(dir);
#         },
#         Some((_, "0.13.2")) => {
#           upgrade_to_45_0(dir);
#         },
#         Some((from_version, to_version)) => {
#             version_bump_in_cargo_toml(&dir.path, from_version, to_version);
#         },
#         None => {},
#     }
# }


# fn upgrade_function_selector(dir: &RelevantDirectory) {
#     if dir.upgrade_in_progress.is_some() {
#         print_upgrading(dir);
#     }

#     if let Some((from_version, to_version)) = &dir.upgrade_in_progress {
#         if framework_version!(0.9.7) == *to_version {
#             upgrade_to_31_0(dir)
#         } else if framework_version!(0.9.9) == *to_version {
#             upgrade_to_32_0(dir)
#         } else if framework_version!(0.10.9) == *to_version {
#             upgrade_to_39_0(dir)
#         } else if framework_version!(0.13.2) == *to_version {
#             upgrade_to_45_0(dir)
#         } else {
#             version_bump_in_cargo_toml(&dir.path, from_version, to_version)
#         }
#     }
# }


# bech32_string = "erd1qqqqqqqqqqqqqpgqp64e3pqxwwyy93t5wp2w2jnlf4lfx3ljqqgsh8qwvz"

# hrp, data = bech32.bech32_decode(bech32_string)

# # Extract witness version and program
# witver, witprog = data[0], data[1:]

# # Convert back to bech32
# encoded_address = bech32.bech32_encode("moa", witprog)
# print("Re-encoded address:", encoded_address)


# [105, 12, 53, 234, 196, 138, 174, 22, 2, 229, 113, 108, 133, 171, 74, 21, 113, 168, 115, 84, 217, 4, 72, 198, 11, 35, 171, 237, 150, 118, 24, 126]

# import base64
# # Base64 formatted public key
# base64_key = "ZDRkYzMyODI3NmQyZDRjNjBkOGZkMWMzNDMzYzM


# # Decode the Base64 key to bytes
# key_bytes = base64.b64decode(base64_key)

# # Convert the bytes to a hexadecimal string
# hex_key = key_bytes.hex()

# print("Hexadecimal Key:", hex_key)




# git clone https://github.com/multiversx/wasmer.git
# git clone https://github.com/multiversx/wasmparser.rs.git
# git clone https://github.com/multiversx/xBulk.git
# git clone https://github.com/multiversx/signalapp-libsignal.git
# git clone https://github.com/multiversx/mx-vm-executor-rs.git
# git clone https://github.com/multiversx/mx-template-sc.git
# git clone https://github.com/multiversx/mx-stablecoin-sc.git
# git clone https://github.com/multiversx/mx-subscription-fee-rs.git
# git clone https://github.com/multiversx/mx-sovereign-sc.git
# git clone https://github.com/multiversx/mx-sdk-rs.git
# git clone https://github.com/multiversx/mx-sdk-dapp-sc-explorer.git

# git clone https://github.com/multiversx/mx-reproducible-contract-build-example-sc.git v0.2.1 v0.2.0

# git clone https://github.com/multiversx/mx-savings-account-sc.git
# git clone https://github.com/multiversx/mx-sc-actions.git
# git clone https://github.com/multiversx/mx-sc-interaction-scripts.git
# git clone https://github.com/multiversx/mx-sdk-abi.git
# git clone https://github.com/multiversx/mx-sdk-clang-contract-builder.git
# git clone https://github.com/multiversx/mx-polynetwork-bridge-sc.git
# git clone https://github.com/multiversx/mx-pre-staking-sc.git
# git clone https://github.com/multiversx/mx-ping-pong-sc.git
# git clone https://github.com/multiversx/mx-liquid-staking-sc.git

# git clone https://github.com/multiversx/mx-metabonding-sc.git v1.1.1  rev = "dc3b67f"

# git clone https://github.com/multiversx/mx-nft-collection-minter-sc.git
# git clone https://github.com/multiversx/mx-nft-marketplace-sc.git
# git clone https://github.com/multiversx/mx-lend-sc.git

# git clone https://github.com/multiversx/mx-exchange-sc.git rev=0c7f45e rev=1fb9a1d

# git clone https://github.com/multiversx/mx-exchange-tools-sc.git
# git clone https://github.com/multiversx/mx-flash-mint-sc.git
# git clone https://github.com/multiversx/mx-human-sc.git
# git clone https://github.com/multiversx/mx-launchpad-sc.git
# git clone https://github.com/multiversx/mx-digital-cash-sc.git
# git clone https://github.com/multiversx/mx-distribution-sc.git
# git clone https://github.com/multiversx/mx-dns-sc.git
# git clone https://github.com/multiversx/mx-energy-competition-winners-extraction-sc.git

# git clone https://github.com/multiversx/mx-contracts-rs.git rev=038a6d8 v0.45.2.1 v0.45.2.2

# git clone https://github.com/multiversx/mx-delegation-sc.git
# git clone https://github.com/multiversx/mx-chainlink-sc.git
# git clone https://github.com/multiversx/mx-bridge-eth-sc-rs.git
# git clone https://github.com/multiversx/mx-attestation-sc.git
# git clone https://github.com/multiversx/mx-band-bridge-sc.git









# fn upgrade_function_selector(dir: &RelevantDirectory) {
#     if dir.upgrade_in_progress.is_some() {
#         print_upgrading(dir);
#     }

#     if let Some((from_version, to_version)) = &dir.upgrade_in_progress {
#         if framework_version!(0.9.7) == *to_version {
#             upgrade_to_9_7(dir)
#         } else if framework_version!(0.9.9) == *to_version {
#             upgrade_to_9_9(dir)
#         } else if framework_version!(0.10.9) == *to_version {
#             upgrade_to_10_9(dir)
#         } else if framework_version!(0.13.2) == *to_version {
#             upgrade_to_13_2(dir)
#         } else {
#             version_bump_in_cargo_toml(&dir.path, from_version, to_version)
#         }
#     }
# }

# fn upgrade_post_processing(dir: &RelevantDirectory, settings: &UpgradeSettings) {
#     if let Some((_, to_version)) = &dir.upgrade_in_progress {
#         if CHECK_AFTER_UPGRADE_TO.contains(to_version) {
#             print_post_processing(dir);
#             cargo_check(dir, settings);
#         } else if framework_version!(0.10.9) == *to_version {
#             print_post_processing(dir);
#             postprocessing_after_10_9(dir);
#             cargo_check(dir, settings);
#         }
#     }
# }
