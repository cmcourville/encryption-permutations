# AES Assignment - Quick Reference

## Your Answer

### Final Output (Hexadecimal)
```
81F6DB7F314F574CC11CC8C825CBADBB
```

### Final State Matrix (4×4)
```
┌────────────────┐
│ 81  31  C1  25 │
│ F6  4F  1C  CB │
│ DB  57  C8  AD │
│ 7F  4C  C8  BB │
└────────────────┘
```

---

## Complete Step-by-Step Results

| Step | Transformation | Result (Hex) |
|:----:|:--------------|:------------|
| a | Input (Binary to Hex) | `2B7083132258F9EB4079389ACFA0CE9F` |
| b | State Matrix (4×4) | `2B7083132258F9EB4079389ACFA0CE9F` |
| c | SubBytes | `F151EC7D936A99E909B607B88AE08BDB` |
| d | ShiftRows | `F16A07DB93B68B7D09E0ECE98A5199B8` |
| e | MixColumns | `9BF7E3C80A1FAF692C140ADEDD202126` |
| **f** | **AddRoundKey (Final)** | **`81F6DB7F314F574CC11CC8C825CBADBB`** |

---

## All State Matrices

### Initial State (Step b)
```
2B  22  40  CF
70  58  79  A0
83  F9  38  CE
13  EB  9A  9F
```

### After SubBytes (Step c)
```
F1  93  09  8A
51  6A  B6  E0
EC  99  07  8B
7D  E9  B8  DB
```

### After ShiftRows (Step d)
```
F1  93  09  8A
6A  B6  E0  51
07  8B  EC  99
DB  7D  E9  B8
```

### After MixColumns (Step e)
```
9B  0A  2C  DD
F7  1F  14  20
E3  AF  0A  21
C8  69  DE  26
```

### After AddRoundKey (Step f - FINAL)
```
81  31  C1  25
F6  4F  1C  CB
DB  57  C8  AD
7F  4C  C8  BB
```

---

## How to Run

### On Mac Terminal
```bash
cd /Users/corrincourville/Documents/development/encryption-simulator
python3 aes_calculator.py
```

This will display:
- All transformation steps
- Detailed explanations
- Before/after comparisons
- Complete state matrices

---

## Files

- `aes_tables.py` - AES S-box and constants
- `aes_operations.py` - Transformation functions
- `aes_calculator.py` - Main calculator (run this!)
- `AES_ASSIGNMENT_RESULTS.md` - Complete detailed results

---

## Key Points

1. **Column-Major Order**: State matrix is filled column-by-column (top to bottom)

2. **SubBytes**: Each byte replaced using S-box[row][col] where row=high nibble, col=low nibble

3. **ShiftRows**: Rows shifted left by 0, 1, 2, 3 positions respectively

4. **MixColumns**: Matrix multiplication in GF(2^8) using polynomial x^8 + x^4 + x^3 + x + 1

5. **AddRoundKey**: XOR each byte with corresponding round key byte

---

**Ready for submission!** ✓
