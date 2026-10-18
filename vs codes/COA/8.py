import math

# 1. Define memory parameters as shown in the experiment illustration
main_memory_size = 4 * 1024 * 1024  # 4 MB
cache_size = 16 * 1024              # 16 KB
block_size = 8                      # 8 Bytes

# 2. Calculate bits using standard log base 2 logic
address_bits = int(math.log2(main_memory_size))  # 22 bits
num_cache_lines = cache_size // block_size     # 2048 lines
line_bits = int(math.log2(num_cache_lines))    # 11 bits
block_offset_bits = int(math.log2(block_size)) # 3 bits
tag_bits = address_bits - (line_bits + block_offset_bits)

# --- Print Parameters matching the PDF Output ---
print(f"Total Address Bits: {address_bits} bits")
print("\n--- Cache Parameters ---")
print(f"Main Memory Size: {main_memory_size / (1024 * 1024)} MB")
print(f"Cache Size: {cache_size / 1024} KB")
print(f"Block Size: {block_size} Bytes")
print(f"Number of Lines: {num_cache_lines} (2**{line_bits})")
print(f"Address Bits: {address_bits}")
print(f"Tag Bits: {tag_bits}")
print(f"Line Bits: {line_bits}")
print(f"Block Offset Bits: {block_offset_bits}")

# Direct Mapping Section
print("\n--- DIRECT MAPPING ---")
print("Address Format: | TAG (8 bits) | LINE NO (11 bits) | BLOCK OFFSET (3 bits) |")

def direct_map(address):
    # Using easy math: Modulo for offset, division & modulo for line, division for tag
    block_offset = address % block_size
    line_no = (address // block_size) % num_cache_lines
    tag = address // (block_size * num_cache_lines)
    return tag, line_no, block_offset

# Example address from the PDF / code
address = 0b1010011101011010110011
tag, line_no, offset = direct_map(address)
print(f"\nExample Address: {bin(address)}")
print(f"Tag: {tag:08b} | Line No: {line_no:011b} | Offset: {offset:03b}")

# --- Fully Associative Mapping Section ---
print("\n--- FULLY ASSOCIATIVE MAPPING ---")
print("No line number field (all blocks can go anywhere)")
fully_tag_bits = address_bits - block_offset_bits
print(f"Tag Bits: {fully_tag_bits} | Block Offset Bits: {block_offset_bits}")

# --- K-Way Set Associative Mapping Section ---
K = 4
num_sets = num_cache_lines // K
set_bits = int(math.log2(num_sets))
tag_bits_kway = address_bits - (set_bits + block_offset_bits)

print("\n--- K-WAY SET ASSOCIATIVE MAPPING ---")
print(f"K = {K}")
print(f"Number of Sets = {num_sets}")
print(f"Tag Bits = {tag_bits_kway}")
print(f"Set Bits = {set_bits}")
print(f"Block Offset Bits = {block_offset_bits}")
print(f"Address Format: | TAG ({tag_bits_kway} bits) | SET NO ({set_bits} bits) | OFFSET ({block_offset_bits} bits) |")