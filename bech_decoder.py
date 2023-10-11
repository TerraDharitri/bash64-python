
import base64
import bech32



bech32Address = "erd1qqqqqqqqqqqqqpgqshqmekudxlxwp0d9j368etjamr5dw7k45u7qx40w6h"

hrp, data = bech32.bech32_decode(bech32Address)
if len(data) == 0:
    print("Error decoding Bech32 address")

base64String = base64.b64encode(bytes(data)).decode('utf-8')
print("Base64:", base64String)


if (len("AAAAAAAAAAAAAAAAAAEIABAXABsZFhwNBh8GDgEPDQUSERoHGQsSHRsDFA0OHhYVFBweAA") == len("GxABFRYNGx0WAw8NFAURGxMJCA8MGxsYCAsOARIHEgwSAwgOBxYXHwcWFAMLGxcHABUfGR")):
    print(True)
    print(len("AAAAAAAAAAAAAAAAAAEIABAXABsZFhwNBh8GDgEPDQUSERoHGQsSHRsDFA0OHhYVFBweAA"))