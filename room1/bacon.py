mapping = {
"00000": "A",
"00001": "B",
"00010": "C",
"00011": "D",
"00100": "E",
"00101": "F",
"00110": "G",
"00111": "H",
"01000": "I",
"01001": "J",
"01010": "K",
"01011": "L",
"01100": "M",
"01101": "N",
"01110": "O",
"01111": "P",
"10000": "Q",
"10001": "R",
"10010": "S",
"10011": "T",
"10100": "U",
"10101": "V",
"10110": "W",
"10111": "X",
"11000": "Y",
"11001": "Z",
"11010": " "
}


def decode(message: str) -> str:
    formatted_message = message.replace(" ", "").replace(",", "").replace(".", "").replace("'", "").replace(";", "") # todo improve this replace

    decoded_message = "".join(["1" if l.isupper() else "0" for l in formatted_message])
    result = ""
    for i in range(0, len(decoded_message), 5):
        if l := mapping.get(decoded_message[i: i+5]):
            result += l

    return result

if __name__ == "__main__":  # pragma: no cover
    with open("../message.txt") as f:
        print(decode(f.read()))
