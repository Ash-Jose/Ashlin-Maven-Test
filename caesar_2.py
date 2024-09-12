num_to_alpha = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 
                 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 
                 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}

def caesar_cipher(text, shift):
    text = text.upper()
    new_text = ""
    for char in text:
        if char.isalpha():
            for key, letter in num_to_alpha.items():
                if letter == char:
                    k = key
            shift_value = shift % 26
            new_text_value = (k + shift_value) % 26
            if new_text_value == 0:
                new_text_value = 26
            new_text += num_to_alpha[new_text_value]
        else:
            new_text += char
    return new_text
      
def main():
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift key (integer): "))

    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted text: ", encrypted_text)

if __name__ == "__main__":
    main()
