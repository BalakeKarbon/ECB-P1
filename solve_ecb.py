import sys
from collections import Counter

def solve(ciphertext):
    """
    Given ECB ciphertext, discard duplicate blocks
    and output remaining data as hex
    """
    # Split ciphertext into 16-byte blocks
    chunks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]

    # Count occurrences of each block
    counts = Counter(chunks)

    # Keep only blocks that appear exactly once, preserving order
    unique_blocks = [chunk for chunk in chunks if counts[chunk] == 1]

    # Reassemble remaining data
    remaining_data = b"".join(unique_blocks)

    # Output as hex
    print(remaining_data.hex())

if __name__ == "__main__":
    with open(sys.argv[1], "rb") as f:
        data = f.read()

solve(data)
