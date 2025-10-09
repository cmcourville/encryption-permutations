"""
AES Round Calculator - Parts i and ii with Avalanche Effect Analysis
Performs one complete AES round and compares outputs to demonstrate avalanche effect.
"""

from aes_operations import (
    binary_to_hex, hex_to_state_matrix, state_to_hex,
    sub_bytes, shift_rows, mix_columns, add_round_key,
    format_state_matrix
)


def compare_binary_strings(bin1, bin2):
    """Compare two binary strings and return difference information."""
    differences = []
    for i, (b1, b2) in enumerate(zip(bin1, bin2)):
        if b1 != b2:
            differences.append(i + 1)  # 1-indexed position
    return len(differences), differences


def hex_to_binary(hex_str):
    """Convert hex string to binary string."""
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)


def process_aes_round(input_binary, round_key_binary, part_name):
    """
    Process one complete AES round and return all results.
    
    Returns:
        dict: All intermediate and final results
    """
    results = {}
    results['input_binary'] = input_binary
    results['input_hex'] = binary_to_hex(input_binary)
    
    # Step b: Create state matrix
    state = hex_to_state_matrix(results['input_hex'])
    results['state_initial'] = [row[:] for row in state]
    
    # Step c: SubBytes
    state_after_subbytes = sub_bytes(state)
    results['state_subbytes'] = state_after_subbytes
    results['hex_subbytes'] = state_to_hex(state_after_subbytes)
    
    # Step d: ShiftRows
    state_after_shiftrows = shift_rows(state_after_subbytes)
    results['state_shiftrows'] = state_after_shiftrows
    results['hex_shiftrows'] = state_to_hex(state_after_shiftrows)
    
    # Step e: MixColumns
    state_after_mixcolumns = mix_columns(state_after_shiftrows)
    results['state_mixcolumns'] = state_after_mixcolumns
    results['hex_mixcolumns'] = state_to_hex(state_after_mixcolumns)
    
    # Step f: AddRoundKey
    round_key_hex = binary_to_hex(round_key_binary)
    round_key_state = hex_to_state_matrix(round_key_hex)
    state_final = add_round_key(state_after_mixcolumns, round_key_state)
    results['state_final'] = state_final
    results['hex_final'] = state_to_hex(state_final)
    results['binary_final'] = hex_to_binary(results['hex_final'])
    
    return results


def print_part_details(results, part_name):
    """Print detailed results for one part."""
    print("\n" + "="*80)
    print(f"{part_name.upper()} - DETAILED RESULTS")
    print("="*80)
    
    print(f"\na) Input (Hexadecimal):")
    print(f"   {results['input_hex']}")
    
    print(f"\nb) Initial State Matrix:")
    for row in range(4):
        print("   " + " ".join(f"{results['state_initial'][row][col]:02X}" for col in range(4)))
    
    print(f"\nc) After SubBytes:")
    print(f"   Hex: {results['hex_subbytes']}")
    for row in range(4):
        print("   " + " ".join(f"{results['state_subbytes'][row][col]:02X}" for col in range(4)))
    
    print(f"\nd) After ShiftRows:")
    print(f"   Hex: {results['hex_shiftrows']}")
    for row in range(4):
        print("   " + " ".join(f"{results['state_shiftrows'][row][col]:02X}" for col in range(4)))
    
    print(f"\ne) After MixColumns:")
    print(f"   Hex: {results['hex_mixcolumns']}")
    for row in range(4):
        print("   " + " ".join(f"{results['state_mixcolumns'][row][col]:02X}" for col in range(4)))
    
    print(f"\nf) After AddRoundKey (FINAL):")
    print(f"   Hex: {results['hex_final']}")
    for row in range(4):
        print("   " + " ".join(f"{results['state_final'][row][col]:02X}" for col in range(4)))


def main():
    """Run AES calculator for parts i and ii with comparison."""
    
    # Part i - Original input
    input_i = "0101011011100001000001100010011001000100101100011111001111010110100000001111001001110001001101011001111101000001100111010011111"
    
    # Part ii - Bit 1 changed (0→1)
    input_ii = "1101011011100001000001100010011001000100101100011111001111010110100000001111001001110001001101011001111101000001100111010011111"
    
    # Round key (same for both)
    round_key = "0011010000000010011100010110111001110110101000011111000001001011110110100001000110000100001011011111000111010111000110010011101"
    
    print("="*80)
    print("AES SINGLE ROUND CALCULATOR - PARTS i AND ii")
    print("="*80)
    print("\nDemonstrating Avalanche Effect in AES")
    print("Comparing outputs when input differs by a single bit")
    
    # Verify input difference
    diff_count, diff_pos = compare_binary_strings(input_i, input_ii)
    print(f"\nInput Difference: {diff_count} bit(s) changed at position(s): {diff_pos}")
    
    # Process Part i
    print("\n" + "="*80)
    print("PROCESSING PART i (Original Input)")
    print("="*80)
    results_i = process_aes_round(input_i, round_key, "Part i")
    print_part_details(results_i, "Part i")
    
    # Process Part ii
    print("\n" + "="*80)
    print("PROCESSING PART ii (Bit 1 Changed: 0→1)")
    print("="*80)
    results_ii = process_aes_round(input_ii, round_key, "Part ii")
    print_part_details(results_ii, "Part ii")
    
    # Comparison and Avalanche Effect Analysis
    print("\n" + "="*80)
    print("AVALANCHE EFFECT ANALYSIS")
    print("="*80)
    
    print("\nInput Comparison:")
    print(f"  Part i  Input: {results_i['input_hex']}")
    print(f"  Part ii Input: {results_ii['input_hex']}")
    print(f"  Difference: {diff_count} bit(s) at position(s) {diff_pos}")
    
    # Compare outputs at each step
    print("\nOutput Comparison at Each Step:")
    
    steps = [
        ("a) Input", results_i['input_hex'], results_ii['input_hex']),
        ("b) Initial State", results_i['input_hex'], results_ii['input_hex']),
        ("c) After SubBytes", results_i['hex_subbytes'], results_ii['hex_subbytes']),
        ("d) After ShiftRows", results_i['hex_shiftrows'], results_ii['hex_shiftrows']),
        ("e) After MixColumns", results_i['hex_mixcolumns'], results_ii['hex_mixcolumns']),
        ("f) After AddRoundKey", results_i['hex_final'], results_ii['hex_final'])
    ]
    
    print(f"\n{'Step':<25} {'Part i':<35} {'Part ii':<35}")
    print("-" * 95)
    for step_name, hex_i, hex_ii in steps:
        print(f"{step_name:<25} {hex_i:<35} {hex_ii:<35}")
    
    # Detailed comparison of final outputs
    print("\n" + "="*80)
    print("FINAL OUTPUT COMPARISON")
    print("="*80)
    
    final_i_bin = results_i['binary_final']
    final_ii_bin = results_ii['binary_final']
    output_diff_count, output_diff_pos = compare_binary_strings(final_i_bin, final_ii_bin)
    
    print(f"\nPart i  Final Output (Hex):    {results_i['hex_final']}")
    print(f"Part ii Final Output (Hex):    {results_ii['hex_final']}")
    
    print(f"\nAvalanche Effect:")
    print(f"  Input difference:  {diff_count} bit (0.78% of 128 bits)")
    print(f"  Output difference: {output_diff_count} bits ({output_diff_count/128*100:.2f}% of 128 bits)")
    print(f"  Amplification:     {output_diff_count}x")
    
    if len(output_diff_pos) <= 20:
        print(f"  Changed bit positions: {output_diff_pos}")
    else:
        print(f"  Changed bit positions: {output_diff_pos[:20]}... (showing first 20)")
    
    # Summary table
    print("\n" + "="*80)
    print("SUMMARY TABLE")
    print("="*80)
    
    print(f"\n{'Metric':<30} {'Part i':<35} {'Part ii':<35}")
    print("-" * 100)
    print(f"{'Input (Hex)':<30} {results_i['input_hex']:<35} {results_ii['input_hex']:<35}")
    print(f"{'Output (Hex)':<30} {results_i['hex_final']:<35} {results_ii['hex_final']:<35}")
    print(f"{'Bits Changed from Part i':<30} {'-':<35} {f'{output_diff_count} ({output_diff_count/128*100:.2f}%)':<35}")
    
    # State matrices side by side
    print("\n" + "="*80)
    print("FINAL STATE MATRICES")
    print("="*80)
    
    print(f"\n{'Part i':<40} {'Part ii':<40}")
    print("-" * 80)
    for row in range(4):
        state_i = " ".join(f"{results_i['state_final'][row][col]:02X}" for col in range(4))
        state_ii = " ".join(f"{results_ii['state_final'][row][col]:02X}" for col in range(4))
        print(f"{state_i:<40} {state_ii:<40}")
    
    print("\n" + "="*80)
    print("AES ROUNDS COMPLETE - AVALANCHE EFFECT DEMONSTRATED")
    print("="*80)
    print(f"\nConclusion: A single-bit change in the input resulted in")
    print(f"{output_diff_count} bits changing in the output ({output_diff_count/128*100:.2f}% of all bits).")
    print("This demonstrates strong diffusion properties in AES.\n")


if __name__ == "__main__":
    main()

