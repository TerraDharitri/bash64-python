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
#    "egld" : "65676c64",
#    "Egld" : "45676c64",
#    "EGLD" : "45474c44",
#    "Moax" : "4d6f6178",
#    "MOAX" : "4d4f4158"
# }

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


no_bunks = int(input())
bike_with_intial_petrol = input().split()
oil_bunks = list(map(int, input().split()))

print(oil_bunks)

