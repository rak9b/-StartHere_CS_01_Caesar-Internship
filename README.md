

# StartHere_CS_01_Caesar

## Caesar Cipher Implementation

This project provides a Python implementation of the Caesar cipher for encryption and decryption. It includes both library functions for programmatic use and a command-line interface (CLI) demo for interactive usage.

### Features:
- **Encryption**: Shift the letters in the input message to generate the corresponding ciphertext.
- **Decryption**: Reverse the encryption process to recover the original plaintext message.
- **Support for Special Characters**: Non-alphabetical characters (e.g., punctuation, spaces) remain unaffected by the cipher.
- **Testing**: Includes comprehensive unit tests to verify the correctness and integrity of the cipher functions.

### Setup

To get started with this project, follow these steps:

1. **Clone the Repository**:  
   Clone the project to your local machine using Git:
   ```bash
   git clone https://github.com/your-username/StartHere_CS_01_Caesar.git
   ```

2. **Install Dependencies**:  
   Navigate to the project directory and install the required Python dependencies listed in `requirements.txt`:
   ```bash
   cd StartHere_CS_01_Caesar
   pip install -r requirements.txt
   ```

3. **Usage**:  
   After installation, you can use the Caesar cipher functions programmatically in your own scripts or run the interactive CLI demo:
   
   - **For Programmatic Use**:
     ```python
     from src.caesar import caesar_cipher, caesar_decipher
     
     message = "Hello World!"
     shift = 3
     encrypted = caesar_cipher(message, shift)
     decrypted = caesar_decipher(encrypted, shift)
     print(f"Encrypted: {encrypted}")
     print(f"Decrypted: {decrypted}")
     ```

   - **For Command-Line Interface (CLI) Demo**:
     You can run the demo for an interactive experience:
     ```bash
     python examples/demo.py
     ```

### Testing

To run the unit tests and ensure that everything is working as expected, use the following command:
```bash
python -m pytest tests/
```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

