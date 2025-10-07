"""
2-Round Reduced DES Implementation
Implements DES encryption with only 2 rounds instead of the standard 16.
"""

from des_tables import IP, FP, E, P, PC1, PC2, S_BOXES, SHIFT_SCHEDULE


def permute(block, table):
    """
    Apply a permutation to a block of bits using the given table.
    
    Args:
        block (str): Binary string
        table (list): Permutation table (1-indexed positions)
    
    Returns:
        str: Permuted binary string
    """
    return ''.join(block[pos - 1] for pos in table)


def left_shift(bits, n):
    """
    Perform circular left shift on a bit string.
    
    Args:
        bits (str): Binary string
        n (int): Number of positions to shift
    
    Returns:
        str: Shifted binary string
    """
    return bits[n:] + bits[:n]


def xor(bits1, bits2):
    """
    Perform XOR operation on two bit strings of equal length.
    
    Args:
        bits1 (str): First binary string
        bits2 (str): Second binary string
    
    Returns:
        str: XOR result as binary string
    """
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bits1, bits2))


def generate_round_keys(key_56bit):
    """
    Generate round keys K1 and K2 from the 56-bit key.
    
    Args:
        key_56bit (str): 56-bit key (binary string)
    
    Returns:
        tuple: (K1, K2) - two 48-bit round keys
    """
    # For 56-bit key input, we don't need to apply PC-1
    # Split into two 28-bit halves
    C0 = key_56bit[:28]
    D0 = key_56bit[28:]
    
    # Generate C1, D1 for Round 1
    C1 = left_shift(C0, SHIFT_SCHEDULE[0])
    D1 = left_shift(D0, SHIFT_SCHEDULE[0])
    
    # Combine and apply PC-2 to get K1
    CD1 = C1 + D1
    K1 = permute(CD1, PC2)
    
    # Generate C2, D2 for Round 2
    C2 = left_shift(C1, SHIFT_SCHEDULE[1])
    D2 = left_shift(D1, SHIFT_SCHEDULE[1])
    
    # Combine and apply PC-2 to get K2
    CD2 = C2 + D2
    K2 = permute(CD2, PC2)
    
    return K1, K2


def s_box_substitution(bits_48):
    """
    Apply S-box substitution to 48-bit input.
    
    Args:
        bits_48 (str): 48-bit binary string
    
    Returns:
        str: 32-bit binary string after S-box substitution
    """
    result = ''
    
    # Process each 6-bit block with corresponding S-box
    for i in range(8):
        # Extract 6-bit block
        block = bits_48[i * 6:(i + 1) * 6]
        
        # Row is determined by first and last bit
        row = int(block[0] + block[5], 2)
        
        # Column is determined by middle 4 bits
        col = int(block[1:5], 2)
        
        # Look up value in S-box
        val = S_BOXES[i][row][col]
        
        # Convert to 4-bit binary string
        result += format(val, '04b')
    
    return result


def f_function(right_32bit, round_key_48bit):
    """
    DES round function (Feistel function).
    
    Args:
        right_32bit (str): 32-bit right half
        round_key_48bit (str): 48-bit round key
    
    Returns:
        str: 32-bit output
    """
    # Expand 32 bits to 48 bits
    expanded = permute(right_32bit, E)
    
    # XOR with round key
    xored = xor(expanded, round_key_48bit)
    
    # Apply S-box substitution (48 bits -> 32 bits)
    substituted = s_box_substitution(xored)
    
    # Apply P permutation
    result = permute(substituted, P)
    
    return result


def des_encrypt_2rounds(plaintext_64bit, key_56bit, verbose=False):
    """
    Perform 2-round reduced DES encryption.
    
    Args:
        plaintext_64bit (str): 64-bit plaintext (binary string)
        key_56bit (str): 56-bit key (binary string, parity bits removed)
        verbose (bool): If True, print intermediate values
    
    Returns:
        str: 64-bit ciphertext (binary string)
    """
    if verbose:
        print("\n" + "="*70)
        print("2-ROUND REDUCED DES ENCRYPTION")
        print("="*70)
        print(f"\nPlaintext:  {plaintext_64bit}")
        print(f"Key (56b):  {key_56bit}")
    
    # Apply Initial Permutation
    permuted = permute(plaintext_64bit, IP)
    if verbose:
        print(f"\nAfter IP:   {permuted}")
    
    # Split into left and right halves
    L0 = permuted[:32]
    R0 = permuted[32:]
    if verbose:
        print(f"\nL0:         {L0}")
        print(f"R0:         {R0}")
    
    # Generate round keys
    K1, K2 = generate_round_keys(key_56bit)
    if verbose:
        print(f"\nK1:         {K1}")
        print(f"K2:         {K2}")
    
    # Round 1
    if verbose:
        print("\n" + "-"*70)
        print("ROUND 1")
        print("-"*70)
    
    L1 = R0
    f_output_1 = f_function(R0, K1)
    R1 = xor(L0, f_output_1)
    
    if verbose:
        print(f"f(R0, K1):  {f_output_1}")
        print(f"L1:         {L1}")
        print(f"R1:         {R1}")
    
    # Round 2
    if verbose:
        print("\n" + "-"*70)
        print("ROUND 2")
        print("-"*70)
    
    L2 = R1
    f_output_2 = f_function(R1, K2)
    R2 = xor(L1, f_output_2)
    
    if verbose:
        print(f"f(R1, K2):  {f_output_2}")
        print(f"L2:         {L2}")
        print(f"R2:         {R2}")
    
    # Combine R2 || L2 (note the swap!)
    combined = R2 + L2
    if verbose:
        print(f"\nR2||L2:     {combined}")
    
    # Apply Final Permutation
    ciphertext = permute(combined, FP)
    
    if verbose:
        print(f"\nAfter FP (Ciphertext):")
        print(f"            {ciphertext}")
        print("="*70 + "\n")
    
    return ciphertext


def format_binary_string(binary_str, group_size=8):
    """
    Format binary string with spaces for readability.
    
    Args:
        binary_str (str): Binary string
        group_size (int): Number of bits per group
    
    Returns:
        str: Formatted binary string
    """
    return ' '.join(binary_str[i:i+group_size] 
                    for i in range(0, len(binary_str), group_size))


def binary_to_hex(binary_str):
    """
    Convert binary string to hexadecimal.
    
    Args:
        binary_str (str): Binary string
    
    Returns:
        str: Hexadecimal string
    """
    return hex(int(binary_str, 2))[2:].upper().zfill(len(binary_str) // 4)

