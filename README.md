# Password Generator

A simple Python script to generate secure passwords.

## Features

- Generate passwords of specified length
- Optionally include/exclude uppercase letters, lowercase letters, digits, and symbols
- Command-line interface for easy use

## Usage

Run the script with optional arguments:

```bash
python password_generator.py [options]
```

### Options

- `-l, --length LENGTH`: Length of the password (default: 12)
- `-u, --uppercase`: Include uppercase letters (default: on)
- `-U, --no-uppercase`: Exclude uppercase letters
- `-l, --lowercase`: Include lowercase letters (default: on)
- `-L, --no-lowercase`: Exclude lowercase letters
- `-d, --digits`: Include digits (default: on)
- `-D, --no-digits`: Exclude digits
- `-s, --symbols`: Include symbols (default: on)
- `-S, --no-symbols`: Exclude symbols

### Examples

Generate a 16-character password with all character types:

```bash
python password_generator.py -l 16
```

Generate a 10-character password without symbols:

```bash
python password_generator.py -l 10 -S
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.