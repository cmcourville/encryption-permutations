# AES Single Round - Assignment Results

## Assignment Task
Compute the given steps for one AES round. Show work and present results in tables for easy following.

---

## Input Data

### 128-bit Input (Binary)
```
0101011011100001000001100010011001000100101100011111001111010110
1000000001111001001110001001101011001111101000001100111010011111
```

### Round Key (Binary)
```
0011010000000010011100010110111001110110101000011111000001001011
1101101000010001100001000010110111110001110101110001100100111101
```

---

## Step-by-Step Results

### Step a) Convert 128-bit Input to Hexadecimal

**Input (Binary):**
```
01010110 11100001 00000110 00100110 01000100 10110001 11110011 11010110
10000000 01111001 00111000 10011010 11001111 10100000 11001110 10011111
```

**Input (Hexadecimal):**
```
2B 70 83 13 22 58 F9 EB 40 79 38 9A CF A0 CE 9F
```

**Compact form:** `2B7083132258F9EB4079389ACFA0CE9F`

---

### Step b) State Matrix (4×4, Column-Major Order)

In AES, the state matrix is filled **column-by-column** (top to bottom, left to right).

**Mapping:**
- Bytes 0-3 → Column 0
- Bytes 4-7 → Column 1  
- Bytes 8-11 → Column 2
- Bytes 12-15 → Column 3

**State Matrix:**
```
┌────────────────┐
│ 2B  22  40  CF │
│ 70  58  79  A0 │
│ 83  F9  38  CE │
│ 13  EB  9A  9F │
└────────────────┘
```

---

### Step c) Apply SubBytes (S-box Substitution)

Each byte is replaced using the AES S-box lookup table.
For byte value `XY` (hex), lookup `S-box[X][Y]`.

**Example lookups:**
- `2B` → `S-box[2][B]` = `F1`
- `70` → `S-box[7][0]` = `51`
- `83` → `S-box[8][3]` = `EC`
- `13` → `S-box[1][3]` = `7D`

**Before SubBytes:**
```
┌────────────────┐
│ 2B  22  40  CF │
│ 70  58  79  A0 │
│ 83  F9  38  CE │
│ 13  EB  9A  9F │
└────────────────┘
```

**After SubBytes:**
```
┌────────────────┐
│ F1  93  09  8A │
│ 51  6A  B6  E0 │
│ EC  99  07  8B │
│ 7D  E9  B8  DB │
└────────────────┘
```

**Hex:** `F151EC7D936A99E909B607B88AE08BDB`

---

### Step d) Apply ShiftRows

Rows are shifted cyclically to the left:
- **Row 0:** No shift
- **Row 1:** Shift left by 1
- **Row 2:** Shift left by 2
- **Row 3:** Shift left by 3

**Transformations:**
```
Row 0: [F1 93 09 8A] → [F1 93 09 8A]  (no shift)
Row 1: [51 6A B6 E0] → [6A B6 E0 51]  (shift 1)
Row 2: [EC 99 07 8B] → [07 8B EC 99]  (shift 2)
Row 3: [7D E9 B8 DB] → [DB 7D E9 B8]  (shift 3)
```

**Before ShiftRows:**
```
┌────────────────┐
│ F1  93  09  8A │
│ 51  6A  B6  E0 │
│ EC  99  07  8B │
│ 7D  E9  B8  DB │
└────────────────┘
```

**After ShiftRows:**
```
┌────────────────┐
│ F1  93  09  8A │
│ 6A  B6  E0  51 │
│ 07  8B  EC  99 │
│ DB  7D  E9  B8 │
└────────────────┘
```

**Hex:** `F16A07DB93B68B7D09E0ECE98A5199B8`

---

### Step e) Apply MixColumns

Each column is multiplied by the MixColumns matrix in GF(2^8):

```
┌            ┐
│ 02 03 01 01│
│ 01 02 03 01│
│ 01 01 02 03│
│ 03 01 01 02│
└            ┘
```

**Irreducible Polynomial:** P(x) = x^8 + x^4 + x^3 + x + 1 (0x11B)

Multiplication is performed using Galois Field arithmetic with the shift-and-XOR method.

**Example (Column 0):**
```
Input:  [F1, 6A, 07, DB]
Output: [9B, F7, E3, C8]

Calculation for first byte:
  02·F1 ⊕ 03·6A ⊕ 01·07 ⊕ 01·DB = 9B
```

**Before MixColumns:**
```
┌────────────────┐
│ F1  93  09  8A │
│ 6A  B6  E0  51 │
│ 07  8B  EC  99 │
│ DB  7D  E9  B8 │
└────────────────┘
```

**After MixColumns:**
```
┌────────────────┐
│ 9B  0A  2C  DD │
│ F7  1F  14  20 │
│ E3  AF  0A  21 │
│ C8  69  DE  26 │
└────────────────┘
```

**Hex:** `9BF7E3C80A1FAF692C140ADEDD202126`

---

### Step f) Apply AddRoundKey

XOR each byte with the corresponding round key byte.

**Round Key (Hex):** `1A0138B73B50F825ED08C216F8EB8C9D`

**Round Key Matrix:**
```
┌────────────────┐
│ 1A  3B  ED  F8 │
│ 01  50  08  EB │
│ 38  F8  C2  8C │
│ B7  25  16  9D │
└────────────────┘
```

**XOR Operation (Row 0 example):**
```
9B ⊕ 1A = 81
0A ⊕ 3B = 31
2C ⊕ ED = C1
DD ⊕ F8 = 25
```

**Before AddRoundKey:**
```
┌────────────────┐
│ 9B  0A  2C  DD │
│ F7  1F  14  20 │
│ E3  AF  0A  21 │
│ C8  69  DE  26 │
└────────────────┘
```

**After AddRoundKey:**
```
┌────────────────┐
│ 81  31  C1  25 │
│ F6  4F  1C  CB │
│ DB  57  C8  AD │
│ 7F  4C  C8  BB │
└────────────────┘
```

**Hex:** `81F6DB7F314F574CC11CC8C825CBADBB`

---

## Summary Table

| Step | Transformation | Result (Hexadecimal) |
|------|---------------|---------------------|
| a | Input | `2B7083132258F9EB4079389ACFA0CE9F` |
| b | Initial State Matrix | `2B7083132258F9EB4079389ACFA0CE9F` |
| c | After SubBytes | `F151EC7D936A99E909B607B88AE08BDB` |
| d | After ShiftRows | `F16A07DB93B68B7D09E0ECE98A5199B8` |
| e | After MixColumns | `9BF7E3C80A1FAF692C140ADEDD202126` |
| **f** | **After AddRoundKey (FINAL)** | **`81F6DB7F314F574CC11CC8C825CBADBB`** |

---

## Final Answer

### Final State Matrix (4×4):
```
┌────────────────┐
│ 81  31  C1  25 │
│ F6  4F  1C  CB │
│ DB  57  C8  AD │
│ 7F  4C  C8  BB │
└────────────────┘
```

### Final Output:
- **Hexadecimal:** `81F6DB7F314F574CC11CC8C825CBADBB`
- **Binary:** `10000001111101101101101101111111001100010100111101010111010011001100000100011100110010001100100000100101110010111010110110111011`

---

## Notes

1. **Column-Major Order:** AES uses column-major order when converting between hex strings and state matrices.

2. **GF(2^8) Arithmetic:** All arithmetic in MixColumns is performed in the Galois Field GF(2^8) using the irreducible polynomial P(x) = x^8 + x^4 + x^3 + x + 1.

3. **S-box Lookup:** The S-box substitution uses the row (high nibble) and column (low nibble) of each byte to find the replacement value.

4. **ShiftRows Pattern:** The shift pattern (0, 1, 2, 3) is fixed for AES and provides diffusion across columns.

---

**Implementation:** All calculations were performed using a Python AES calculator (`aes_calculator.py`) that implements standard AES transformations according to the FIPS 197 specification.
