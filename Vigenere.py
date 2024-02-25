# -*- coding: UTF-8 -*-
'''
Vigenere.py - A script for Vigenere cipher encryption and decryption.
'''

import argparse

class Vigenere:
    def __init__(self, message: str, key: str, decrypt_mode: bool) -> None:
        self.message = message
        self.key = key.upper()  # Ensure key is uppercase for consistency
        self.decrypt_mode = decrypt_mode

    def encrypt(self) -> str:
        result = ""
        for i in range(len(self.message)):
            char = self.message[i]
            if not char.isalpha():
                result += char
                continue
            offset = 65 if char.isupper() else 97
            shift = ord(self.key[i % len(self.key)]) - 65
            result += chr((ord(char) - offset + shift) % 26 + offset)
        return result

    def decrypt(self) -> str:
        result = ""
        for i in range(len(self.message)):
            char = self.message[i]
            if not char.isalpha():
                result += char
                continue
            offset = 65 if char.isupper() else 97
            shift = ord(self.key[i % len(self.key)]) - 65
            result += chr((ord(char) - offset - shift) % 26 + offset)
        return result


def main():
    parser = argparse.ArgumentParser(description="Vigenere cipher script")
    parser.add_argument("message", metavar="MESSAGE", type=str, help="Message to be encrypted or decrypted")
    parser.add_argument("key", metavar="KEY", type=str, help="Key for encryption or decryption")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Use decryption mode")
    args = parser.parse_args()

    vigenere = Vigenere(args.message, args.key, args.decrypt)

    if args.decrypt:
        print("Decrypted:", vigenere.decrypt())
    else:
        print("Encrypted:", vigenere.encrypt())


if __name__ == "__main__":
    main()