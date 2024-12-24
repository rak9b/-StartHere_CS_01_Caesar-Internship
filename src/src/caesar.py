def caesar_cipher(message: str, shift: int) -> str:
    """
    Encrypt a message using the Caesar cipher with the specified shift.

    Parameters:
    message (str): The input string to be encrypted.
    shift (int): The number of positions to shift each character.

    Returns:
    str: The encrypted message.
    """
    result = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result


def caesar_decipher(message: str, shift: int) -> str:
    """
    Decrypt a Caesar cipher message by reversing the specified shift.

    Parameters:
    message (str): The encrypted string to be decrypted.
    shift (int): The number of positions to reverse shift each character.

    Returns:
    str: The decrypted message.
    """
    return caesar_cipher(message, -shift)
