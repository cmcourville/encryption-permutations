"""
AES Operations Module
Implements all AES transformations: SubBytes, ShiftRows, MixColumns, AddRoundKey
"""

from aes_tables import SBOX, MIX_COLUMNS_MATRIX, AES_POLYNOMIAL, sbox_lookup
import copy


def binary_to_hex(binary_str):
    """
    Convert binary string to hexadecimal string.
    
    Args:
        binary_str (str): Binary string (e.g., 128 bits)
    
    Returns:
        str: Hexadecimal string
    """
    # Convert to integer, then to hex
    num = int(binary_str, 2)
    hex_str = hex(num)[2:].upper()
    # Pad to correct length
    expected_len = len(binary_str) // 4
    return hex_str.zfill(expected_len)


def hex_to_state_matrix(hex_str):
    """
    Convert hex string to 4x4 state matrix (column-major order).
    In AES, the state is filled column by column.
    
    Args:
        hex_str (str): 32-character hex string (128 bits)
    
    Returns:
        list: 4x4 matrix of integers
    """
    # Convert hex string to list of bytes
    bytes_list = [int(hex_str[i:i+2], 16) for i in range(0, len(hex_str), 2)]
    
    # Create 4x4 matrix in column-major order
    # state[row][col]
    state = [[0] * 4 for _ in range(4)]
    
    idx = 0
    for col in range(4):
        for row in range(4):
            state[row][col] = bytes_list[idx]
            idx += 1
    
    return state


def state_to_hex(state):
    """
    Convert 4x4 state matrix back to hex string (column-major).
    
    Args:
        state (list): 4x4 matrix
    
    Returns:
        str: Hexadecimal string
    """
    hex_str = ""
    for col in range(4):
        for row in range(4):
            hex_str += format(state[row][col], '02x').upper()
    return hex_str


def sub_bytes(state):
    """
    Apply SubBytes transformation using AES S-box.
    
    Args:
        state (list): 4x4 state matrix
    
    Returns:
        list: New 4x4 state matrix after SubBytes
    """
    new_state = [[0] * 4 for _ in range(4)]
    
    for row in range(4):
        for col in range(4):
            byte_val = state[row][col]
            new_state[row][col] = sbox_lookup(byte_val)
    
    return new_state


def shift_rows(state):
    """
    Apply ShiftRows transformation.
    Row 0: no shift
    Row 1: shift left by 1
    Row 2: shift left by 2
    Row 3: shift left by 3
    
    Args:
        state (list): 4x4 state matrix
    
    Returns:
        list: New 4x4 state matrix after ShiftRows
    """
    new_state = [[0] * 4 for _ in range(4)]
    
    for row in range(4):
        for col in range(4):
            # Shift left by 'row' positions
            new_col = (col - row) % 4
            new_state[row][new_col] = state[row][col]
    
    return new_state


def gf_mult(a, b):
    """
    Multiply two numbers in GF(2^8) using AES irreducible polynomial.
    Polynomial: x^8 + x^4 + x^3 + x + 1 (0x11b)
    
    Uses the shift-and-XOR method explained in class.
    
    Args:
        a (int): First operand (0-255)
        b (int): Second operand (0-255)
    
    Returns:
        int: Product in GF(2^8)
    """
    p = 0
    
    for _ in range(8):
        # If lowest bit of b is 1, XOR with a
        if b & 1:
            p ^= a
        
        # Check if high bit of a is set
        high_bit_set = a & 0x80
        
        # Shift a left by 1
        a <<= 1
        
        # If high bit was set, reduce by XOR with polynomial
        if high_bit_set:
            a ^= AES_POLYNOMIAL
        
        # Shift b right by 1
        b >>= 1
    
    return p & 0xFF


def mix_columns(state):
    """
    Apply MixColumns transformation.
    Each column is multiplied by the MixColumns matrix in GF(2^8).
    
    Matrix:
    [02 03 01 01]
    [01 02 03 01]
    [01 01 02 03]
    [03 01 01 02]
    
    Args:
        state (list): 4x4 state matrix
    
    Returns:
        list: New 4x4 state matrix after MixColumns
    """
    new_state = [[0] * 4 for _ in range(4)]
    
    for col in range(4):
        # Extract the column
        column = [state[row][col] for row in range(4)]
        
        # Multiply by MixColumns matrix
        for row in range(4):
            new_val = 0
            for i in range(4):
                new_val ^= gf_mult(MIX_COLUMNS_MATRIX[row][i], column[i])
            new_state[row][col] = new_val
    
    return new_state


def add_round_key(state, round_key_state):
    """
    Apply AddRoundKey transformation (XOR with round key).
    
    Args:
        state (list): 4x4 state matrix
        round_key_state (list): 4x4 round key matrix
    
    Returns:
        list: New 4x4 state matrix after AddRoundKey
    """
    new_state = [[0] * 4 for _ in range(4)]
    
    for row in range(4):
        for col in range(4):
            new_state[row][col] = state[row][col] ^ round_key_state[row][col]
    
    return new_state


def format_state_matrix(state, title="State Matrix"):
    """
    Format state matrix as a pretty table.
    
    Args:
        state (list): 4x4 state matrix
        title (str): Title for the matrix
    
    Returns:
        str: Formatted string representation
    """
    output = f"\n{title}:\n"
    output += "┌" + "─" * 35 + "┐\n"
    for row in range(4):
        output += "│ "
        for col in range(4):
            output += f"{state[row][col]:02X} "
        output += "│\n"
    output += "└" + "─" * 35 + "┘\n"
    return output
