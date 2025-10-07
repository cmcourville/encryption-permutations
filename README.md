# 2-Round Reduced DES Encryption

A Python implementation of the Data Encryption Standard (DES) algorithm with only 2 rounds instead of the standard 16 rounds. This implementation uses all standard DES components including permutation tables, S-boxes, and the Feistel structure.

## Overview

This project implements a reduced version of DES for educational purposes, demonstrating:
- Initial and Final Permutations (IP/FP)
- Key scheduling and round key generation
- Expansion, substitution (S-boxes), and permutation
- The Feistel cipher structure
- All standard DES tables and constants

## Files

- `des_tables.py` - All DES constants (IP, FP, E, P, S-boxes, PC-1, PC-2)
- `des_2round.py` - Core 2-round DES implementation
- `main.py` - Main script with assignment input/key values
- `verify_des.py` - Verification test suite
- `VERIFICATION_REPORT.md` - Test results and validation report
- `README.md` - This file

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Usage

### Running with Default Assignment Values

Simply run the main script:

```bash
python main.py
```

This will encrypt the assignment's input using the provided key and display:
- Input plaintext and key
- Detailed step-by-step encryption process
- Intermediate values (L0, R0, L1, R1, L2, R2, K1, K2)
- Final ciphertext in both binary and hexadecimal

### Using Custom Values

You can modify `main.py` or use the encryption function directly:

```python
from des_2round import des_encrypt_2rounds

# Your 64-bit plaintext (binary string)
plaintext = "1011001100001111111100100001011011110100001101001011111100101110"

# Your 56-bit key (binary string, parity bits already removed)
key = "00100000000111101110001001011111110101101111110111111111"

# Encrypt (verbose=True shows all intermediate steps)
ciphertext = des_encrypt_2rounds(plaintext, key, verbose=True)

print(f"Ciphertext: {ciphertext}")
```

## Assignment Input Values

**Input (64 bits):**
```
1011001100001111111100100001011011110100001101001011111100101110
```

**DES Key (56 bits, parity bits removed):**
```
00100000000111101110001001011111110101101111110111111111
```

## How It Works

### 1. Initial Permutation (IP)
The 64-bit plaintext is permuted according to the IP table.

### 2. Split into L0 and R0
The permuted block is split into two 32-bit halves.

### 3. Key Schedule
From the 56-bit key, two round keys (K1 and K2) are generated:
- Split key into C0 and D0 (28 bits each)
- Apply left circular shifts
- Use PC-2 to select 48 bits for each round key

### 4. Round 1
- L1 = R0
- R1 = L0 ⊕ f(R0, K1)

Where f is the Feistel function:
- Expand R0 from 32 to 48 bits using E table
- XOR with round key K1
- Apply S-box substitution (48 → 32 bits)
- Apply P permutation

### 5. Round 2
- L2 = R1
- R2 = L1 ⊕ f(R1, K2)

### 6. Final Steps
- Combine as R2||L2 (note the swap)
- Apply Final Permutation (FP)
- Result is the 64-bit ciphertext

## Output Format

The program displays:
1. **Input section**: Plaintext and key in binary and hex
2. **Detailed encryption process**: All intermediate values
3. **Final result**: Ciphertext in binary and hex
4. **Compact output**: Easy-to-copy format for submission

## Example Output

```
======================================================================
2-ROUND REDUCED DES ENCRYPTION - ASSIGNMENT
======================================================================

INPUT DATA:
----------------------------------------------------------------------
Plaintext (64 bits):
  Binary: 10110011 00001111 11110010 00010110 11110100 00110100 10111111 00101110
  Hex:    B30FF216F434BF2E

DES Key (56 bits, parity bits removed):
  Binary: 0010000 0000111 1011100 0100101 1111110 1011011 1111011 1111111
  Hex:    201F7097EDB7BF

======================================================================
2-ROUND REDUCED DES ENCRYPTION
======================================================================

Plaintext:  1011001100001111111100100001011011110100001101001011111100101110
Key (56b):  00100000000111101110001001011111110101101111110111111111

After IP:   ...
...
[Detailed intermediate steps]
...

FINAL RESULT:
----------------------------------------------------------------------
Ciphertext (64 bits):
  Binary: ...
  Hex:    ...
```

## Verification

The implementation has been thoroughly verified and tested:

```bash
# Activate virtual environment (if not already active)
source venv/bin/activate

# Run verification tests
python verify_des.py
```

**Verification Results:** ✓ ALL 9 TESTS PASSED (100%)

The following components have been verified:
- Initial and Final Permutations (IP/FP)
- Expansion table (E)
- All 8 S-boxes
- Permutation (P)
- Key schedule generation (PC-2, shifts)
- Feistel function
- Complete encryption with test vectors

See `VERIFICATION_REPORT.md` for detailed test results.

## Notes

- This is a **2-round reduced DES**, not the full 16-round version
- Uses all standard DES tables and operations
- Key input is 56 bits (parity bits already removed)
- All intermediate values are displayed for educational purposes
- **Implementation verified against DES specifications** ✓

## Educational Purpose

This implementation is designed for learning and understanding the DES algorithm. It demonstrates:
- How block ciphers work
- The Feistel network structure
- Permutation and substitution operations
- Key scheduling in symmetric encryption

**Note**: Reduced-round DES is NOT secure for real-world use. This is for educational purposes only.
