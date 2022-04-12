alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = raw_input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = raw_input("Type your message:\n").lower()
shift = int(raw_input("Type the shift number:\n"))

def encrypt(text, shift):
    encryptedString = ""
    for letter in text:
        index = alphabet.index(letter)
        newIndex = index + shift
        if(newIndex > len(alphabet) - 1):
            newIndex = newIndex - len(alphabet)
        encryptedString += alphabet[newIndex]
    print(encryptedString)

def decrypt(text, shift):
    decryptedString = ""
    for letter in text:
        index = alphabet.index(letter)
        newIndex = index - shift
        if(newIndex < 0):
            newIndex = newIndex + len(alphabet)
        decryptedString += alphabet[newIndex]
    print(decryptedString)


if(direction == "encode"):
    encrypt(text, shift)
if(direction == "decode"):
    decrypt(text, shift)