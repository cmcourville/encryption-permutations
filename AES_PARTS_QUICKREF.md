# AES Assignment - Quick Reference (Parts i and ii)

## Your Answers

### Part i
**Final Output:** `81F6DB7F314F574CC11CC8C825CBADBB`

**Final State Matrix:**
```
81  31  C1  25
F6  4F  1C  CB
DB  57  C8  AD
7F  4C  C8  BB
```

### Part ii
**Final Output:** `867855F6314F574CC11CC8C825CBADBB`

**Final State Matrix:**
```
86  31  C1  25
78  4F  1C  CB
55  57  C8  AD
F6  4C  C8  BB
```

---

## Avalanche Effect Summary

| Metric | Value |
|--------|-------|
| Input Difference | 1 bit (bit #1: 0→1) |
| Output Difference | 14 bits changed |
| Percentage Changed | 10.94% of 128 bits |
| Amplification Factor | 14x |

**Changed Bit Positions:** 6, 7, 8, 9, 13, 14, 15, 17, 21, 22, 23, 25, 29, 32

---

## Step-by-Step Results

### Part i Transformations

| Step | Result (Hex) |
|------|--------------|
| a) Input | `2B7083132258F9EB4079389ACFA0CE9F` |
| c) SubBytes | `F151EC7D936A99E909B607B88AE08BDB` |
| d) ShiftRows | `F16A07DB93B68B7D09E0ECE98A5199B8` |
| e) MixColumns | `9BF7E3C80A1FAF692C140ADEDD202126` |
| **f) Final** | **`81F6DB7F314F574CC11CC8C825CBADBB`** |

### Part ii Transformations

| Step | Result (Hex) |
|------|--------------|
| a) Input | `6B7083132258F9EB4079389ACFA0CE9F` |
| c) SubBytes | `7F51EC7D936A99E909B607B88AE08BDB` |
| d) ShiftRows | `7F6A07DB93B68B7D09E0ECE98A5199B8` |
| e) MixColumns | `9C796D410A1FAF692C140ADEDD202126` |
| **f) Final** | **`867855F6314F574CC11CC8C825CBADBB`** |

---

## Comparison Table

| Part | Input (Hex) | Output (Hex) |
|------|-------------|--------------|
| i | `2B7083132258F9EB4079389ACFA0CE9F` | `81F6DB7F314F574CC11CC8C825CBADBB` |
| ii | `6B7083132258F9EB4079389ACFA0CE9F` | `867855F6314F574CC11CC8C825CBADBB` |

---

## How to Run

```bash
cd /Users/corrincourville/Documents/development/encryption-simulator
python3 aes_calculator_v2.py
```

---

## Files

- `aes_calculator_v2.py` - Main calculator
- `AES_PARTS_i_ii_RESULTS.md` - Detailed results
- `AES_PARTS_QUICKREF.md` - This file

---

**Ready for submission!** ✓
