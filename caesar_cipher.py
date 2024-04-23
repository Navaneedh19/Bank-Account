alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
code = input("Type 'Encode' to encrypt, type decrypt to 'Decode': \n")
text = input("Type your message :\n").lower()
shift = int(input("Type the shift number: \n"))
# Encryption
# def encrpyt(plain_text, shift_amount):
#   cipher_text = " "
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter

#   print(f"The encoded text is {cipher_text}.")

# encrpyt(plain_text=text, shift_amount=shift)


#Decryption

# def decrypt (plain_text, shift_amount):
#     cipher_text = " "
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         cipher_text += alphabet[new_position]
#     print (f"The decode text is {cipher_text}.")


# decrypt(plain_text=text, shift_amount=shift)

# For both Encryption and Decryption

def ceaser_cipher(start_text, shift_amount, direction):
    print(code.lower())
    end_text = " "
    if direction == "decode":
        shift_amount *= -1
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The direction is {direction} and the result is {end_text}.")

ceaser_cipher(start_text= text, shift_amount=shift, direction=code.lower())            