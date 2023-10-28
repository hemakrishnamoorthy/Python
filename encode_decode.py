alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def cypher(text, shift, direction):
    cypher_text = ""
    for i in range(len(text)):
        idx = alphabet.index(text[i])
        if direction == 'encode':
            new_idx = idx + shift
        elif direction == 'decode':
            new_idx = idx - shift
        cypher_text += alphabet[new_idx]

    print(f"Your {direction}d message is {cypher_text}")


cypher(text, shift, direction)
