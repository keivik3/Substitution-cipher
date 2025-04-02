# Encryption/Decryption Tools

This repository contains three Python scripts that implement different encryption and decryption algorithms:

## Files Overview

### 1. athenian.py
- **Algorithm**: Affine Cipher (single key)
- **Description**: 
  - Implements basic affine cipher encryption/decryption
  - Uses a single key pair (a, b) where 'a' must be coprime with 26
  - Encryption formula: `E(x) = (a*x + b) mod 26`
  - Decryption formula: `D(y) = a⁻¹*(y - b) mod 26` (where a⁻¹ is modular inverse)

### 2. athenian_rec.py
- **Algorithm**: Recursive Affine Cipher (dual-key variant)
- **Description**: 
  - Extends the affine cipher with two initial keys that recursively generate new keys
  - Each character's encryption uses a different key derived from previous keys
  - Maintains the same mathematical properties as basic affine cipher but with evolving keys

### 3. simple.py
- **Algorithm**: Simple Substitution Cipher
- **Description**: 
  - Implements a basic letter substitution cipher
  - Uses a fixed key that maps each letter to another letter
  - Provides simple character-by-character substitution

## Usage Instructions

### For all scripts:
1. Clone the repository or download the files
2. Run the desired script: `python filename.py`
3. Follow the on-screen prompts to enter text for encryption/decryption

### Key Requirements:
- **athenian.py**: 
  - Key must be a list of two numbers, e.g., `[3, 3]`
  - First number must be coprime with 26 (gcd(a,26) = 1)

- **athenian_rec.py**: 
  - Requires two initial keys (each a list of two numbers)
  - Both keys' first elements must be coprime with 26

- **simple.py**: 
  - Key must be a 26-character string representing the substitution alphabet
  - Default key is "cdefghijklmnopqrstuvwxyzab" (shift by 2)

## Example Usage

### athenian.py:
```bash
python athenian.py
> Введите текст: hello
> Основной ключ: [3, 3]
> Зашифрованный текст: dhuun
> Введите текст для расшифрования: dhuun
> Расшифрованный текст: hello
```

### simple.py:
```bash
python simple.py
> Введите открытый текст: hello
> Ключ: cdefghijklmnopqrstuvwxyzab
> Зашифрованный текст: jgnnq
> Введите зашифрованный текст: jgnnq
> Расшифрованный текст: hello
```

## Notes
- All scripts work with lowercase English alphabet only
- Non-alphabetic characters will cause errors
- The recursive affine cipher (athenian_rec.py) provides stronger security than the basic versions

Feel free to experiment with different keys and texts to see how the encryption works!
