"""
Main script for 2-Round Reduced DES Encryption
Compares three different plaintexts (parts i, ii, iii) to demonstrate avalanche effect
"""

from des_2round import des_encrypt_2rounds, format_binary_string, binary_to_hex


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


def main():
    """Main function to run 2-round DES encryption for parts i, ii, and iii."""
    
    # Part i - Original input (bit 1 = 1, bit 2 = 0)
    plaintext_i = "1011001100001111111100100001011011110100001101001011111100101110"
    
    # Part ii - Bit 2 changed from 0 to 1
    plaintext_ii = "1111001100001111111100100001011011110100001101001011111100101110"
    
    # Part iii - Bit 1 changed from 1 to 0
    plaintext_iii = "0011001100001111111100100001011011110100001101001011111100101110"
    
    # DES Key from assignment (56 bits, parity bits already removed)
    # Same key for all three parts
    key = "00100000000111101110001001011111110101101111110111111111"
    
    print("\n" + "="*80)
    print("2-ROUND REDUCED DES ENCRYPTION - AVALANCHE EFFECT DEMONSTRATION")
    print("="*80)
    
    # Validate key
    if len(key) != 56:
        print(f"Error: Key must be 56 bits (got {len(key)} bits)")
        return
    
    print("\nDES Key (Same for all three parts):")
    print("-" * 80)
    print(f"  Binary: {format_binary_string(key, 7)}")
    print(f"  Hex:    {binary_to_hex(key)}")
    
    # Process Part i
    print("\n" + "="*80)
    print("PART i - ORIGINAL INPUT")
    print("="*80)
    print(f"Plaintext i (64 bits):")
    print(f"  Binary: {format_binary_string(plaintext_i)}")
    print(f"  Hex:    {binary_to_hex(plaintext_i)}")
    
    ciphertext_i = des_encrypt_2rounds(plaintext_i, key, verbose=False)
    
    print(f"\nCiphertext i:")
    print(f"  Binary: {format_binary_string(ciphertext_i)}")
    print(f"  Hex:    {binary_to_hex(ciphertext_i)}")
    
    # Process Part ii
    print("\n" + "="*80)
    print("PART ii - BIT 2 CHANGED (0 → 1)")
    print("="*80)
    print(f"Plaintext ii (64 bits):")
    print(f"  Binary: {format_binary_string(plaintext_ii)}")
    print(f"  Hex:    {binary_to_hex(plaintext_ii)}")
    
    # Show input difference
    diff_count, diff_positions = compare_binary_strings(plaintext_i, plaintext_ii)
    print(f"\nInput difference from Part i: {diff_count} bit(s) at position(s): {diff_positions}")
    
    ciphertext_ii = des_encrypt_2rounds(plaintext_ii, key, verbose=False)
    
    print(f"\nCiphertext ii:")
    print(f"  Binary: {format_binary_string(ciphertext_ii)}")
    print(f"  Hex:    {binary_to_hex(ciphertext_ii)}")
    
    # Process Part iii
    print("\n" + "="*80)
    print("PART iii - BIT 1 CHANGED (1 → 0)")
    print("="*80)
    print(f"Plaintext iii (64 bits):")
    print(f"  Binary: {format_binary_string(plaintext_iii)}")
    print(f"  Hex:    {binary_to_hex(plaintext_iii)}")
    
    # Show input difference
    diff_count, diff_positions = compare_binary_strings(plaintext_i, plaintext_iii)
    print(f"\nInput difference from Part i: {diff_count} bit(s) at position(s): {diff_positions}")
    
    ciphertext_iii = des_encrypt_2rounds(plaintext_iii, key, verbose=False)
    
    print(f"\nCiphertext iii:")
    print(f"  Binary: {format_binary_string(ciphertext_iii)}")
    print(f"  Hex:    {binary_to_hex(ciphertext_iii)}")
    
    # Comparison Section
    print("\n" + "="*80)
    print("AVALANCHE EFFECT ANALYSIS")
    print("="*80)
    
    # Compare i vs ii
    diff_count_i_ii, diff_positions_i_ii = compare_binary_strings(ciphertext_i, ciphertext_ii)
    print(f"\nCiphertext i vs ii:")
    print(f"  Input difference:  1 bit changed (bit 2: 0→1)")
    print(f"  Output difference: {diff_count_i_ii} bits changed ({diff_count_i_ii/64*100:.2f}%)")
    print(f"  Changed bit positions: {diff_positions_i_ii[:10]}{'...' if len(diff_positions_i_ii) > 10 else ''}")
    
    # Compare i vs iii
    diff_count_i_iii, diff_positions_i_iii = compare_binary_strings(ciphertext_i, ciphertext_iii)
    print(f"\nCiphertext i vs iii:")
    print(f"  Input difference:  1 bit changed (bit 1: 1→0)")
    print(f"  Output difference: {diff_count_i_iii} bits changed ({diff_count_i_iii/64*100:.2f}%)")
    print(f"  Changed bit positions: {diff_positions_i_iii[:10]}{'...' if len(diff_positions_i_iii) > 10 else ''}")
    
    # Compare ii vs iii
    diff_count_ii_iii, diff_positions_ii_iii = compare_binary_strings(ciphertext_ii, ciphertext_iii)
    print(f"\nCiphertext ii vs iii:")
    print(f"  Input difference:  2 bits changed (bits 1 and 2)")
    print(f"  Output difference: {diff_count_ii_iii} bits changed ({diff_count_ii_iii/64*100:.2f}%)")
    print(f"  Changed bit positions: {diff_positions_ii_iii[:10]}{'...' if len(diff_positions_ii_iii) > 10 else ''}")
    
    # Summary table
    print("\n" + "="*80)
    print("SUMMARY TABLE")
    print("="*80)
    print(f"\n{'Part':<8} {'Plaintext (Hex)':<20} {'Ciphertext (Hex)':<20}")
    print("-" * 80)
    print(f"{'i':<8} {binary_to_hex(plaintext_i):<20} {binary_to_hex(ciphertext_i):<20}")
    print(f"{'ii':<8} {binary_to_hex(plaintext_ii):<20} {binary_to_hex(ciphertext_ii):<20}")
    print(f"{'iii':<8} {binary_to_hex(plaintext_iii):<20} {binary_to_hex(ciphertext_iii):<20}")
    
    print("\n" + "="*80)
    print("COMPACT OUTPUT FOR SUBMISSION")
    print("="*80)
    print(f"\nKey: {key}")
    print(f"\nPart i:")
    print(f"  Plaintext:  {plaintext_i}")
    print(f"  Ciphertext: {ciphertext_i}")
    print(f"  Ciphertext (Hex): {binary_to_hex(ciphertext_i)}")
    print(f"\nPart ii:")
    print(f"  Plaintext:  {plaintext_ii}")
    print(f"  Ciphertext: {ciphertext_ii}")
    print(f"  Ciphertext (Hex): {binary_to_hex(ciphertext_ii)}")
    print(f"\nPart iii:")
    print(f"  Plaintext:  {plaintext_iii}")
    print(f"  Ciphertext: {ciphertext_iii}")
    print(f"  Ciphertext (Hex): {binary_to_hex(ciphertext_iii)}")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()

