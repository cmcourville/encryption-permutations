<!-- 8b4b8743-18b4-474e-a0f9-f23b21eaea6b 4c506e23-357b-47dc-add3-bafc99460e55 -->
# 2-Round Reduced DES Implementation

## Overview

Create a Python implementation of DES with only 2 rounds instead of the standard 16, using all standard DES components (permutation tables, S-boxes, etc.).

## Implementation Steps

### 1. Create DES Tables Module

Create `des_tables.py` containing all standard DES constants:

- Initial Permutation (IP) table
- Final Permutation (FP) table
- Expansion (E) table
- Permutation (P) table
- All 8 S-boxes (S1-S8)
- Permuted Choice 1 (PC-1) for key scheduling
- Permuted Choice 2 (PC-2) for round key generation
- Left shift schedule (will use only first 2 values)

### 2. Create Core DES Implementation

Create `des_2round.py` with the following functions:

- `permute(block, table)`: Apply permutation using given table
- `left_shift(bits, n)`: Circular left shift
- `xor(bits1, bits2)`: XOR two bit strings
- `generate_round_keys(key_56bit)`: Generate 2 round keys (K1, K2) from the 56-bit key
  - Apply PC-1 to split into C0 and D0
  - Apply left shifts for rounds 1 and 2
  - Apply PC-2 to generate K1 and K2
- `s_box_substitution(bits_48)`: Apply S-box substitution
- `f_function(right_32bit, round_key_48bit)`: DES round function
  - Expand 32 bits to 48 bits using E table
  - XOR with round key
  - Apply S-box substitution to get 32 bits
  - Apply P permutation
- `des_encrypt_2rounds(plaintext_64bit, key_56bit)`: Main encryption function
  - Apply Initial Permutation (IP)
  - Split into L0 and R0
  - Round 1: L1 = R0, R1 = L0 XOR f(R0, K1)
  - Round 2: L2 = R1, R2 = L1 XOR f(R1, K2)
  - Combine R2 || L2 (note the swap)
  - Apply Final Permutation (FP)
  - Return ciphertext

### 3. Create Main Script

Create `main.py` with:

- Input handling for 64-bit plaintext and 56-bit key
- Support for various input formats (binary string, hex)
- Call encryption function and display result
- Optional verbose mode to show intermediate values (L0, R0, K1, K2, L1, R1, L2, R2)

### 4. Add Example Usage

Include example with:

- Sample 64-bit input
- Sample 56-bit key
- Expected output for verification

## File Structure

```
encryption-simulator/
├── des_tables.py       # All DES constants and tables
├── des_2round.py       # Core 2-round DES implementation
├── main.py            # Main entry point with I/O handling
└── README.md          # Usage instructions and examples
```

### To-dos

- [ ] Create des_tables.py with all DES permutation tables and S-boxes
- [ ] Implement des_2round.py with key scheduling and round functions
- [ ] Create main.py with input handling and output display
- [ ] Add README.md with usage instructions and examples