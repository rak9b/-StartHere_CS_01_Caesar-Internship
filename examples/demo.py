from src.caesar import caesar_cipher, caesar_decipher

def main():
    """
    Interactive demo for Caesar cipher encryption and decryption.
    """
    # Get user input for message and shift
    message = input("Enter message to encrypt: ")
    shift = int(input("Enter shift value (1-25): "))

    # Encrypt the message
    encrypted = caesar_cipher(message, shift)
    print(f"Encrypted message: {encrypted}")

    # Decrypt the message
    decrypted = caesar_decipher(encrypted, shift)
    print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()


