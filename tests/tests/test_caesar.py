import pytest
from src.caesar import caesar_cipher, caesar_decipher

def test_encryption():
    """
    Test the encryption function with a sample message.
    """
    message = "Hello World!"
    shift = 3
    expected = "Khoor Zruog!"  # Expected result after shifting each letter by 3
    encrypted_message = caesar_cipher(message, shift)
    assert encrypted_message == expected, f"Expected {expected}, but got {encrypted_message}"

def test_decryption():
    """
    Test the decryption function with a sample encrypted message.
    """
    encrypted_message = "Khoor Zruog!"
    shift = 3
    expected = "Hello World!"  # Expected result after reversing the encryption
    decrypted_message = caesar_decipher(encrypted_message, shift)
    assert decrypted_message == expected, f"Expected {expected}, but got {decrypted_message}"

def test_round_trip():
    """
    Test that encryption and then decryption restores the original message.
    """
    message = "Testing123!"  # Includes a mix of letters, numbers, and punctuation
    shift = 5
    encrypted_message = caesar_cipher(message, shift)
    decrypted_message = caesar_decipher(encrypted_message, shift)
    assert decrypted_message == message, f"Expected {message}, but got {decrypted_message}"

def test_non_alpha_characters():
    """
    Test that non-alphabet characters (spaces, punctuation, etc.) are preserved during encryption and decryption.
    """
    message = "Hello, World!"
    shift = 3
    expected_encryption = "Khoor, Zruog!"
    encrypted_message = caesar_cipher(message, shift)
    assert encrypted_message == expected_encryption, f"Expected {expected_encryption}, but got {encrypted_message}"

    # Ensure decryption also works correctly
    decrypted_message = caesar_decipher(encrypted_message, shift)
    assert decrypted_message == message, f"Expected {message}, but got {decrypted_message}"
