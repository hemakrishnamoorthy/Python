alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    if direction == "encode":
        encrypted_text = ""
        for i in range(len(text)):
            idx = alphabet.index(text[i])
            new_idx = idx + shift

            encrypted_text += alphabet[new_idx]

        print(f"Your encoded message is {encrypted_text}")


def decrypt(text, shift):
    if direction == "decode":
        decrypted_text = ""
        for i in range(len(text)):
            idx = alphabet.index(text[i])
            new_idx = idx - shift

            decrypted_text += alphabet[new_idx]

        print(f"Your decoded message is {decrypted_text}")


if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
