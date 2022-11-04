
def decode(message: str) -> str:
    return_string = ''
    message = message.replace(' ', '')
    message = message.replace(',', '')
    message = message.replace('.', '')
    message = message.replace(';', '')
    for n in range(0, len(message), 5):
        return_string += decode_one(message[n:n+5])
        
    return return_string

def decode_one(chunk: str) -> str:
    lookup = "abcdefghijklmnopqrstuvwxyz "
    idx = bitmask(chunk)
    if idx >= len(lookup):
        return ""
    return lookup[idx]

# aaaaA -> 00001 -> 1
# aaaAa -> 00010 -> 2
def bitmask(chunk: str) -> int:
    binary_string = "".join(['1' if x == x.upper() else '0' for x in chunk])
    return int(binary_string,2)
