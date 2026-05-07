#!/usr/bin/env python3
"""
A simple password generator script.

Generate secure passwords with optional inclusion of uppercase, lowercase, digits, and symbols.
"""

import argparse
import random
import string


def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    """Generate a password of given length with specified character sets."""
    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Build the character set based on user options
    characters = ''
    if use_lowercase:
        characters += lowercase
    if use_uppercase:
        characters += uppercase
    if use_digits:
        characters += digits
    if use_symbols:
        characters += symbols

    if not characters:
        raise ValueError("At least one character set must be selected.")

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    parser = argparse.ArgumentParser(description="Generate a secure password.")
    parser.add_argument(
        "-l", "--length", type=int, default=12, help="Length of the password (default: 12)"
    )
    parser.add_argument(
        "-u", "--uppercase", action="store_true", help="Include uppercase letters (default: on)"
    )
    parser.add_argument(
        "-U", "--no-uppercase", dest="uppercase", action="store_false", help="Exclude uppercase letters"
    )
    parser.add_argument(
        "-l", "--lowercase", action="store_true", help="Include lowercase letters (default: on)"
    )
    parser.add_argument(
        "-L", "--no-lowercase", dest="lowercase", action="store_false", help="Exclude lowercase letters"
    )
    parser.add_argument(
        "-d", "--digits", action="store_true", help="Include digits (default: on)"
    )
    parser.add_argument(
        "-D", "--no-digits", dest="digits", action="store_false", help="Exclude digits"
    )
    parser.add_argument(
        "-s", "--symbols", action="store_true", help="Include symbols (default: on)"
    )
    parser.add_argument(
        "-S", "--no-symbols", dest="symbols", action="store_false", help="Exclude symbols"
    )
    # Set defaults for the boolean flags
    parser.set_defaults(uppercase=True, lowercase=True, digits=True, symbols=True)
    args = parser.parse_args()

    try:
        password = generate_password(
            length=args.length,
            use_uppercase=args.uppercase,
            use_lowercase=args.lowercase,
            use_digits=args.digits,
            use_symbols=args.symbols,
        )
        print(password)
    except ValueError as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    main()