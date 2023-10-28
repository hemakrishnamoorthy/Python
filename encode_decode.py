alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def cypher(text, shift, direction):
    cypher_text = ""
    for c in text:
        if c in alphabet:
            idx = alphabet.index(c)
            if direction == 'encode':
                new_idx = idx + shift
            elif direction == 'decode':
                new_idx = idx - shift
            cypher_text += alphabet[new_idx]

        else:
            cypher_text += c

    print(f"Your {direction}d message is {cypher_text}")

repeat = 'Y'
while repeat == 'Y':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    cypher(text, shift, direction)
    repeat = input("Do you want to restart the cipher program? Y/N: ").upper()
