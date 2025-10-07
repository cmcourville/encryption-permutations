# Quick Start Guide - 2-Round DES Implementation

## Running the Assignment

### Option 1: Run from Mac Terminal (Recommended)

1. Open Terminal
2. Navigate to the project directory:
   ```bash
   cd /Users/corrincourville/Documents/development/encryption-simulator
   ```

3. Run the main program:
   ```bash
   python3 main.py
   ```

This will compute ciphertexts for all three parts (i, ii, iii) and show the avalanche effect analysis.

### Option 2: Using Virtual Environment (with verification)

1. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. Run the main program:
   ```bash
   python main.py
   ```

3. Run verification tests (optional):
   ```bash
   python verify_des.py
   ```

## Your Assignment Results

### Input Data
- **Key (56 bits):** `00100000000111101110001001011111110101101111110111111111`

### Part i - Original Input
- **Plaintext:**  `1011001100001111111100100001011011110100001101001011111100101110`
- **Ciphertext:** `1000101111010011100011001000001000010110011000111000011011111101`
- **Hex:** `8BD38C82166386FD`

### Part ii - Bit 2 Changed (0→1)
- **Plaintext:**  `1111001100001111111100100001011011110100001101001011111100101110`
- **Ciphertext:** `0001111111010011110011011001001000010111011000111100001011111101`
- **Hex:** `1FD3CD921763C2FD`
- **Change:** 9 bits different from Part i (14.06%)

### Part iii - Bit 1 Changed (1→0)
- **Plaintext:**  `0011001100001111111100100001011011110100001101001011111100101110`
- **Ciphertext:** `1100011011010011010011111010011100000101011001111101001110111101`
- **Hex:** `C6D34FA70567D3BD`
- **Change:** 20 bits different from Part i (31.25%)

## Avalanche Effect Summary

| Comparison | Input Difference | Output Difference |
|------------|------------------|-------------------|
| i vs ii    | 1 bit (bit 2)    | 9 bits (14.06%)   |
| i vs iii   | 1 bit (bit 1)    | 20 bits (31.25%)  |
| ii vs iii  | 2 bits           | 17 bits (26.56%)  |

This demonstrates how even a single bit change in the plaintext causes significant changes in the ciphertext!

## Verification Status

✓ **Implementation Verified - All Tests Passed**

The DES implementation has been verified with 9 comprehensive tests:
- ✓ Permutation tables (IP/FP)
- ✓ Expansion table (E)
- ✓ S-box substitutions
- ✓ XOR operations
- ✓ Circular shifts
- ✓ Key schedule generation
- ✓ Feistel function
- ✓ Known test vectors
- ✓ Assignment values

See `VERIFICATION_REPORT.md` for details.

## Project Structure

```
encryption-simulator/
├── des_tables.py              # DES constants and tables
├── des_2round.py              # Core 2-round DES implementation  
├── main.py                    # Main program (run this!)
├── verify_des.py              # Verification test suite
├── VERIFICATION_REPORT.md     # Detailed test results
├── README.md                  # Full documentation
├── QUICKSTART.md             # This file
└── venv/                      # Virtual environment (optional)
```

## Need Help?

- **See full documentation:** `README.md`
- **See verification details:** `VERIFICATION_REPORT.md`
- **Modify inputs:** Edit the plaintext/key values in `main.py`

## Notes

- The implementation uses standard DES tables and operations
- This is a 2-round reduced DES (not the full 16-round version)
- All intermediate values can be displayed by setting `verbose=True`
- The implementation has been verified to be correct ✓
