# ls = [
#     "mx-chain-vm-excutor",
#     "mx-sdk-rs",
#     "mx-exchange-sc",
#     "mx-metabonding-sc",
#     "mx-exchange-tools-sc",
#     "mx-bridge-eth-rs",
#     "mx-subscription-fee-rs",
#     "mx-vm-executor-rs",
#     "mx-contract-sc",
#     "xBulk",
#     "wasmer",
#     "mx-nft-collection-minter-sc",
#     "mx-reproducible-contract-build-example-sc",
#     "mx-digital-cash-sc",
#     "mx-ping-pong-sc",
#     "mx-launchpad-sc",
#     "mx-liquid-stking-sc",
#     "mx-lend-sc"

# ]

# print("" in ls)

#[payment_nonce] endpoint argument annotation
#[payable] annotation no longer allowed without argument

#repos 
# open-modules
#xmodules
#raphtory
#raphtory-graphql
#elrond-rust
#feruca


# hexv = {
#    "MULTIVERSX" :"4d554c54495645525358",
#    "MultiversX": "4d756c74697665727358",
#    "multiversx": "6d756c74697665727378",
#    "elrond": "656c726f6e64",
#    "Elrond": "456c726f6e64",
#    "ELROND": "454c524f4e44",
#    "DHARITRI": "4448415249545249"
#    "Esdt" : "45736474",
#    "ESDT" : "45534454",
#    "DCT" : "444354",
#    "esdt" : "65736474",
#    "dct"  : "646374"
#    "egld" : "65676c64",
#    "moax" : "6d6f6178"
#    "Egld" : "45676c64",
#    "Moax" : "4d6f6178",
#    "EGLD" : "45474c44",
#    "MOAX" : "4d4f4158"
#    "mandos": "6d616e646f73"
#    "Mandos": "4d616e646f73"
#    "MANDOS": "4d414e444f53"
#    "erdpy": 6572647079
#    "Erdpy": 4572647079
#    "ERDPY": 4552445059
#    "erdjs": 6572646a73

# }
#crates.io api tocken ciorFtnJRK1N6z3y4SLbak07GHhgtHFTg1S
# print(len("aaaaaaaaaaaaaaaaaaaaaaaaaa.dharitri"))


# (t,c,s) = [int(i) for i in input().split()]

# print(min(t//4, c//1, s//4))




# no_employes = int(input())
# donations = [int(i) for i in input().split(" ")]
# no_donations = int(input())
# least_donations = []
# if no_employes > 3:
#     is_grater = True
#     for i in donations:
#         if i <= 0:
#             is_grater = False
#     if is_grater:
#         if no_donations < no_employes:
        
#             for i in range(no_donations):
#                 least_donations.a
#     final_money *= i 
# print(final_money)ppend(min(donations))
#                 donations.remove(min(donations))

#                 final_money = 1
# for i in  least_donations:
#     final_money *= i 
# print(final_money)


# n = int(input())
# passwords = [input() for i in range(n)]
# validator = []
# for password in passwords:
#     if len(password) < 10:
#         validator.append("INVALID")
#     else:
#         password_parts = []
#         for i in range(len(password)):
#             try:
#                 part = password[i: i+4]
#                 if len(part) == 4:
#                     password_parts.append(part)
#             except:
#                 pass
#         ord_parts = []
#         for j in password_parts:
#             ords = []
#             for k in j:
#                 ords.append(ord(k))
#             ord_parts.append(ords)
#         print(ord_parts)
#         for p in ord_parts:
#             is_week = 0
#             for h in range(len(p)):
#                 try:
#                     if p[h+1] - p[h] == 1:
#                         is_week += 1 
#                 except:
#                     pass
#             if is_week == 4:
#                 validator.append(True)

# if "INVALID" in validator:
#     print("Invalid")
# elif True in validator:
#     print("WEEK")
# else:
#     print("STRONG")


# count = 0
# for i in range(1, 5):
#     factors = 0
#     for j in range(1, i+1):
#         if i%j == 0:
#             factors += 1 
#     if factors % 2 == 1:
#        count += 1
# print(count)


# p = "Anil"






from collections import Counter

def count_equal_substrings(input_str):
    count = 0
    length = len(input_str)
    for i in range(length):
        for j in range(i + 1, length + 1):
            substring = input_str[i:j]
            mid = len(substring) // 2
            first_half = substring[:mid]
            second_half = substring[mid:]
            if Counter(first_half) == Counter(second_half):
                count += 1
    return count

input_str = "373733"
output = count_equal_substrings(input_str)
print( output)