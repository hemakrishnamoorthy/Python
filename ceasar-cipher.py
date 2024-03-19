logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP""" """"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""" """" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
exit_prog = False
print(logo)


def encrypt_decrypt(direction, text, shift):
    cipher_text = ""
    to_shift = 0
    for c in text:
        if c in alphabet:
            index = alphabet.index(c)
            if direction == "encode":
                to_shift = (index + shift) % 26
            else:
                to_shift = (index - shift)
                if to_shift < 0:
                    to_shift = 26 + to_shift
            cipher_text += alphabet[to_shift]
        else:
            cipher_text += c
    print(f"The {direction}d text is: {cipher_text}\n")


while not exit_prog:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt the text:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    encrypt_decrypt(direction, text, shift)
    restart = input("Do you waant to restart the program? (y/n)\n: ").lower()
    if restart == 'n':
        exit_prog = True
        print("Goodbye")
