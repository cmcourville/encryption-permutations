# AES Single Round - Parts i and ii (Avalanche Effect)

## Assignment Task
Solve part i with the original input and part ii with bit 1 changed. Use the same round key for both. Compare the output bits to demonstrate the avalanche effect in AES.

---

## 📊 Final Answers

### Part i (Original Input)
**Final Output (Hex):** `81F6DB7F314F574CC11CC8C825CBADBB`

**Final State Matrix:**
```
┌────────────────┐
│ 81  31  C1  25 │
│ F6  4F  1C  CB │
│ DB  57  C8  AD │
│ 7F  4C  C8  BB │
└────────────────┘
```

### Part ii (Bit 1 Changed: 0→1)
**Final Output (Hex):** `867855F6314F574CC11CC8C825CBADBB`

**Final State Matrix:**
```
┌────────────────┐
│ 86  31  C1  25 │
│ 78  4F  1C  CB │
│ 55  57  C8  AD │
│ F6  4C  C8  BB │
└────────────────┘
```

---

## 🎯 Avalanche Effect Analysis

### Input Comparison

| Part | Input (Hex) | Input (Binary) |
|------|-------------|----------------|
| i | `2B7083132258F9EB4079389ACFA0CE9F` | `0101...` |
| ii | `6B7083132258F9EB4079389ACFA0CE9F` | `1101...` |

**Input Difference:** 
- **1 bit** changed (bit #1: 0→1)
- This is **0.78%** of 128 bits

### Output Comparison

| Part | Output (Hex) |
|------|--------------|
| i | `81F6DB7F314F574CC11CC8C825CBADBB` |
| ii | `867855F6314F574CC11CC8C825CBADBB` |

**Output Difference:**
- **14 bits** changed
- This is **10.94%** of 128 bits
- **14x amplification** from 1 input bit to 14 output bits

**Changed Bit Positions:** 6, 7, 8, 9, 13, 14, 15, 17, 21, 22, 23, 25, 29, 32

---

## 📋 Complete Step-by-Step Comparison

### Part i Results

| Step | Transformation | Result (Hex) |
|:----:|:--------------|:------------|
| a | Input | `2B7083132258F9EB4079389ACFA0CE9F` |
| b | Initial State | `2B7083132258F9EB4079389ACFA0CE9F` |
| c | SubBytes | `F151EC7D936A99E909B607B88AE08BDB` |
| d | ShiftRows | `F16A07DB93B68B7D09E0ECE98A5199B8` |
| e | MixColumns | `9BF7E3C80A1FAF692C140ADEDD202126` |
| **f** | **AddRoundKey** | **`81F6DB7F314F574CC11CC8C825CBADBB`** |

### Part ii Results

| Step | Transformation | Result (Hex) |
|:----:|:--------------|:------------|
| a | Input | `6B7083132258F9EB4079389ACFA0CE9F` |
| b | Initial State | `6B7083132258F9EB4079389ACFA0CE9F` |
| c | SubBytes | `7F51EC7D936A99E909B607B88AE08BDB` |
| d | ShiftRows | `7F6A07DB93B68B7D09E0ECE98A5199B8` |
| e | MixColumns | `9C796D410A1FAF692C140ADEDD202126` |
| **f** | **AddRoundKey** | **`867855F6314F574CC11CC8C825CBADBB`** |

---

## 🔍 Detailed Transformation Comparison

### Initial State Matrices

**Part i:**
```
2B  22  40  CF
70  58  79  A0
83  F9  38  CE
13  EB  9A  9F
```

**Part ii:**
```
6B  22  40  CF
70  58  79  A0
83  F9  38  CE
13  EB  9A  9F
```

**Difference:** Only position [0,0] changed (`2B` → `6B`)

---

### After SubBytes

**Part i:**
```
F1  93  09  8A
51  6A  B6  E0
EC  99  07  8B
7D  E9  B8  DB
```

**Part ii:**
```
7F  93  09  8A
51  6A  B6  E0
EC  99  07  8B
7D  E9  B8  DB
```

**Difference:** Only position [0,0] changed (`F1` → `7F`)

---

### After ShiftRows

**Part i:**
```
F1  93  09  8A
6A  B6  E0  51
07  8B  EC  99
DB  7D  E9  B8
```

**Part ii:**
```
7F  93  09  8A
6A  B6  E0  51
07  8B  EC  99
DB  7D  E9  B8
```

**Difference:** Only position [0,0] changed (`F1` → `7F`)

---

### After MixColumns

**Part i:**
```
9B  0A  2C  DD
F7  1F  14  20
E3  AF  0A  21
C8  69  DE  26
```

**Part ii:**
```
9C  0A  2C  DD
79  1F  14  20
6D  AF  0A  21
41  69  DE  26
```

**Difference:** Entire first column changed!
- [0,0]: `9B` → `9C`
- [1,0]: `F7` → `79`
- [2,0]: `E3` → `6D`
- [3,0]: `C8` → `41`

**Key Observation:** MixColumns spreads the single-byte difference throughout the entire column!

---

### After AddRoundKey (Final)

**Part i:**
```
81  31  C1  25
F6  4F  1C  CB
DB  57  C8  AD
7F  4C  C8  BB
```

**Part ii:**
```
86  31  C1  25
78  4F  1C  CB
55  57  C8  AD
F6  4C  C8  BB
```

**Difference:** First column changed
- [0,0]: `81` → `86`
- [1,0]: `F6` → `78`
- [2,0]: `DB` → `55`
- [3,0]: `7F` → `F6`

---

## 📊 Summary Comparison Table

| Metric | Part i | Part ii | Difference |
|--------|--------|---------|------------|
| **Input (Hex)** | `2B70...` | `6B70...` | 1 bit |
| **After SubBytes** | `F151...` | `7F51...` | 1 byte |
| **After ShiftRows** | `F16A...` | `7F6A...` | 1 byte |
| **After MixColumns** | `9BF7...` | `9C79...` | 4 bytes (1 column) |
| **Final Output** | `81F6...` | `8678...` | **14 bits** |
| **Percentage Changed** | — | — | **10.94%** |

---

## 💡 Key Observations

1. **SubBytes:** The single bit difference causes one byte to change (`2B` → `6B` becomes `F1` → `7F`)

2. **ShiftRows:** The difference remains in the same position since row 0 doesn't shift

3. **MixColumns:** This is where **diffusion** happens!
   - The single-byte difference spreads to the entire column
   - All 4 bytes in column 0 are now different

4. **AddRoundKey:** The column difference persists, affecting 4 bytes in the final output

5. **Avalanche Effect:**
   - Input: 1 bit changed (0.78%)
   - Output: 14 bits changed (10.94%)
   - **14x amplification** demonstrates strong diffusion

---

## 🎓 Conclusion

### Avalanche Effect in AES

**Input Difference:** 1 bit (0.78% of 128 bits)  
**Output Difference:** 14 bits (10.94% of 128 bits)

This demonstrates that:
- A small change in input (1 bit) causes significant change in output (14 bits)
- **MixColumns** is the primary source of diffusion in a single round
- Even one round of AES shows noticeable avalanche effect
- Full AES (10-14 rounds) would show much stronger avalanche (~50% bits changed)

The avalanche effect is a critical security property that ensures:
- Similar plaintexts produce very different ciphertexts
- It's difficult to find relationships between input and output
- The cipher has good **confusion** and **diffusion**

---

## 📁 Files

- `aes_calculator_v2.py` - Calculator for parts i and ii
- `aes_tables.py` - AES S-box and constants
- `aes_operations.py` - AES transformations

## 🚀 How to Run

```bash
cd /Users/corrincourville/Documents/development/encryption-simulator
python3 aes_calculator_v2.py
```

---

**Both parts complete!** ✓  
**Avalanche effect successfully demonstrated!** ✓
