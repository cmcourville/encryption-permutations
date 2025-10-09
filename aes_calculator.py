"""
AES Round Calculator - Parts i and ii
Performs one complete AES round with detailed step-by-step output.
Demonstrates avalanche effect by comparing two inputs differing by 1 bit.
"""

from aes_operations import (
    binary_to_hex, hex_to_state_matrix, state_to_hex,
    sub_bytes, shift_rows, mix_columns, add_round_key,
    format_state_matrix
)


def compare_binary_strings(bin1, bin2):
    """
    Compare two binary strings and return difference information.
    
    Args:
        bin1 (str): First binary string
        bin2 (str): Second binary string
    
    Returns:
        tuple: (number_of_differences, list_of_positions)
    """
    differences = []
    for i, (b1, b2) in enumerate(zip(bin1, bin2)):
        if b1 != b2:
            differences.append(i + 1)  # 1-indexed position
    return len(differences), differences


def hex_to_binary(hex_str):
    """
    Convert hex string to binary string.
    
    Args:
        hex_str (str): Hexadecimal string
    
    Returns:
        str: Binary string
    """
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)


def print_step_header(step_letter, step_name):
    """Print a formatted step header."""
    print("\n" + "="*80)
    print(f"STEP {step_letter}: {step_name}")
    print("="*80)


def print_state_comparison(state1, state2, title1, title2):
    """Print two states side by side for comparison."""
    print(f"\n{title1:40} {title2:40}")
    print("-" * 80)
    for row in range(4):
        line1 = " ".join(f"{state1[row][col]:02X}" for col in range(4))
        line2 = " ".join(f"{state2[row][col]:02X}" for col in range(4))
        print(f"{line1:40} {line2:40}")


def process_aes_part(input_binary, round_key_binary, part_name, verbose=True):
    """
    Process one AES round for a given input.
    
    Args:
        input_binary (str): 128-bit input as binary string
        round_key_binary (str): 128-bit round key as binary string
        part_name (str): Name of the part (e.g., "Part i")
        verbose (bool): If True, show detailed output
    
    Returns:
        dict: Dictionary containing all intermediate results
    """
    results = {}
    
    if verbose:
        print("\n" + "="*80)
        print(f"{part_name.upper()}")
        print("="*80)
    
    print("="*80)
    print("AES SINGLE ROUND CALCULATOR")
    print("="*80)
    print("\nAssignment: Compute AES transformations step-by-step")
    print("Show work and present results in tables for easy following")
    
    # =========================================================================
    # STEP A: Convert 128-bit input to Hexadecimal
    # =========================================================================
    print_step_header("a", "Convert 128-bit Input to Hexadecimal")
    
    print(f"\nInput (Binary, 128 bits):")
    # Print in groups of 8 for readability
    for i in range(0, 128, 32):
        print(f"  Bits {i+1:3d}-{i+32:3d}: {input_binary[i:i+32]}")
    
    input_hex = binary_to_hex(input_binary)
    print(f"\nInput (Hexadecimal, 32 hex digits):")
    print(f"  {input_hex}")
    
    # Also show in groups of 8 hex digits (32 bits each)
    print(f"\nFormatted (4 groups of 8 hex digits):")
    for i in range(0, 32, 8):
        print(f"  {input_hex[i:i+8]}")
    
    # =========================================================================
    # STEP B: Write input in state diagram (4x4 matrix)
    # =========================================================================
    print_step_header("b", "Arrange Input as 4x4 State Matrix (Column-Major Order)")
    
    print("\nNote: AES fills the state matrix in COLUMN-MAJOR order.")
    print("This means we fill top-to-bottom, then move to the next column.")
    
    state = hex_to_state_matrix(input_hex)
    
    print("\nByte positions in hex string → matrix positions:")
    print("  Bytes 0-3   → Column 0 (top to bottom)")
    print("  Bytes 4-7   → Column 1 (top to bottom)")
    print("  Bytes 8-11  → Column 2 (top to bottom)")
    print("  Bytes 12-15 → Column 3 (top to bottom)")
    
    print(format_state_matrix(state, "Initial State Matrix"))
    
    print("Verification:")
    for col in range(4):
        bytes_in_col = [f"{state[row][col]:02X}" for row in range(4)]
        byte_indices = list(range(col*4, col*4+4))
        print(f"  Column {col}: {' '.join(bytes_in_col)} (bytes {byte_indices})")
    
    # =========================================================================
    # STEP C: Apply SubBytes
    # =========================================================================
    print_step_header("c", "Apply SubBytes (S-box Substitution)")
    
    print("\nSubBytes replaces each byte using the AES S-box lookup table.")
    print("For each byte value XY (hex), look up S-box[X][Y]")
    
    state_after_subbytes = sub_bytes(state)
    
    print("\nSample S-box lookups:")
    for row in range(2):  # Show first 2 rows as examples
        for col in range(4):
            old_val = state[row][col]
            new_val = state_after_subbytes[row][col]
            x = (old_val >> 4) & 0x0F
            y = old_val & 0x0F
            print(f"  {old_val:02X} → S-box[{x:X}][{y:X}] = {new_val:02X}")
    print("  ...")
    
    print_state_comparison(state, state_after_subbytes, 
                          "Before SubBytes", "After SubBytes")
    
    print(format_state_matrix(state_after_subbytes, "State After SubBytes"))
    
    # =========================================================================
    # STEP D: Apply ShiftRows
    # =========================================================================
    print_step_header("d", "Apply ShiftRows")
    
    print("\nShiftRows cyclically shifts each row to the left:")
    print("  Row 0: No shift")
    print("  Row 1: Shift left by 1 position")
    print("  Row 2: Shift left by 2 positions")
    print("  Row 3: Shift left by 3 positions")
    
    state_after_shiftrows = shift_rows(state_after_subbytes)
    
    print("\nRow transformations:")
    for row in range(4):
        before = [f"{state_after_subbytes[row][col]:02X}" for col in range(4)]
        after = [f"{state_after_shiftrows[row][col]:02X}" for col in range(4)]
        print(f"  Row {row}: [{' '.join(before)}] → [{' '.join(after)}]")
    
    print(format_state_matrix(state_after_shiftrows, "State After ShiftRows"))
    
    # =========================================================================
    # STEP E: Apply MixColumns
    # =========================================================================
    print_step_header("e", "Apply MixColumns (Galois Field Multiplication)")
    
    print("\nMixColumns multiplies each column by a fixed matrix in GF(2^8):")
    print("  [02 03 01 01]")
    print("  [01 02 03 01]")
    print("  [01 01 02 03]")
    print("  [03 01 01 02]")
    print("\nIrreducible Polynomial: P(x) = x^8 + x^4 + x^3 + x + 1 (0x11B)")
    print("Using shift-and-XOR approach for GF multiplication.")
    
    state_after_mixcolumns = mix_columns(state_after_shiftrows)
    
    print("\nColumn transformations (showing column 0 as example):")
    print(f"  Input column:  [{' '.join(f'{state_after_shiftrows[r][0]:02X}' for r in range(4))}]")
    print(f"  Output column: [{' '.join(f'{state_after_mixcolumns[r][0]:02X}' for r in range(4))}]")
    
    print_state_comparison(state_after_shiftrows, state_after_mixcolumns,
                          "Before MixColumns", "After MixColumns")
    
    print(format_state_matrix(state_after_mixcolumns, "State After MixColumns"))
    
    # =========================================================================
    # STEP F: Apply AddRoundKey
    # =========================================================================
    print_step_header("f", "Apply AddRoundKey (XOR with Round Key)")
    
    print(f"\nRound Key (Binary, 128 bits):")
    for i in range(0, 128, 32):
        print(f"  Bits {i+1:3d}-{i+32:3d}: {round_key_binary[i:i+32]}")
    
    round_key_hex = binary_to_hex(round_key_binary)
    print(f"\nRound Key (Hexadecimal):")
    print(f"  {round_key_hex}")
    
    round_key_state = hex_to_state_matrix(round_key_hex)
    print(format_state_matrix(round_key_state, "Round Key Matrix"))
    
    print("\nAddRoundKey XORs each byte of the state with the corresponding round key byte:")
    
    state_final = add_round_key(state_after_mixcolumns, round_key_state)
    
    print("\nXOR operation (showing first row as example):")
    for col in range(4):
        state_val = state_after_mixcolumns[0][col]
        key_val = round_key_state[0][col]
        result_val = state_final[0][col]
        print(f"  {state_val:02X} ⊕ {key_val:02X} = {result_val:02X}")
    
    print_state_comparison(state_after_mixcolumns, state_final,
                          "State Before AddRoundKey", "State After AddRoundKey")
    
    print(format_state_matrix(state_final, "FINAL State After AddRoundKey"))
    
    # =========================================================================
    # SUMMARY TABLE
    # =========================================================================
    print("\n" + "="*80)
    print("SUMMARY TABLE - ALL TRANSFORMATION STEPS")
    print("="*80)
    
    final_hex = state_to_hex(state_final)
    
    print(f"\n{'Step':<30} {'Result (Hex)':<50}")
    print("-" * 80)
    print(f"{'a) Input (Hex)':<30} {input_hex}")
    print(f"{'b) Initial State Matrix':<30} {state_to_hex(state)}")
    print(f"{'c) After SubBytes':<30} {state_to_hex(state_after_subbytes)}")
    print(f"{'d) After ShiftRows':<30} {state_to_hex(state_after_shiftrows)}")
    print(f"{'e) After MixColumns':<30} {state_to_hex(state_after_mixcolumns)}")
    print(f"{'f) After AddRoundKey (FINAL)':<30} {final_hex}")
    print("=" * 80)
    
    # Display all state matrices in a compact format
    print("\n" + "="*80)
    print("COMPLETE STATE MATRICES AT EACH STEP")
    print("="*80)
    
    states = [
        ("Input", state),
        ("After SubBytes", state_after_subbytes),
        ("After ShiftRows", state_after_shiftrows),
        ("After MixColumns", state_after_mixcolumns),
        ("After AddRoundKey", state_final)
    ]
    
    for title, s in states:
        print(f"\n{title}:")
        for row in range(4):
            print("  " + " ".join(f"{s[row][col]:02X}" for col in range(4)))
    
    print("\n" + "="*80)
    print("AES ROUND COMPLETE")
    print("="*80)
    print(f"\nFinal Output (Hexadecimal): {final_hex}")
    print(f"Final Output (Binary):      {bin(int(final_hex, 16))[2:].zfill(128)}")
    print("\n")


if __name__ == "__main__":
    run_aes_round()
