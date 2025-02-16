def double_hash_rabin_karp(seq_x: str, seq_y: str):
    import time
    start_time = time.perf_counter()

    if len(seq_x) >= len(seq_y):
        text, pattern = seq_x, seq_y
    else:
        text, pattern = seq_y, seq_x

    text_length = len(text)
    pattern_length = len(pattern)
    matches = 0

    if pattern_length == 0 or pattern_length > text_length:
        end_time = time.perf_counter()
        return text, pattern, matches, end_time - start_time

    prime1, prime2 = 101, 103
    d = 256

    # First hash (left to right)
    pattern_hash1 = 0
    text_hash1 = 0
    h1 = 1

    # Second hash (right to left)
    pattern_hash2 = 0
    text_hash2 = 0
    h2 = 1

    # Calculate powers
    for i in range(pattern_length - 1):
        h1 = (h1 * d) % prime1
        h2 = (h2 * d) % prime2

    # Calculate initial hash values for pattern and first window
    for i in range(pattern_length):
        pattern_hash1 = (d * pattern_hash1 + ord(pattern[i])) % prime1
        text_hash1 = (d * text_hash1 + ord(text[i])) % prime1

        pattern_hash2 = (d * pattern_hash2 + ord(pattern[pattern_length-1-i])) % prime2
        text_hash2 = (d * text_hash2 + ord(text[i])) % prime2

    # Slide pattern over text
    for i in range(text_length - pattern_length + 1):
        if pattern_hash1 == text_hash1:  # First check the forward hash
            # Now calculate backward hash for the current window
            text_hash2 = 0
            for j in range(pattern_length):
                text_hash2 = (d * text_hash2 + ord(text[i + pattern_length-1-j])) % prime2

            if pattern_hash2 == text_hash2:  # If both hashes match, check characters
                match = True
                for j in range(pattern_length):
                    if text[i + j] != pattern[j]:
                        match = False
                        break
                if match:
                    matches += 1

        if i < text_length - pattern_length:
            # Update forward hash for next window
            text_hash1 = (d * (text_hash1 - ord(text[i]) * h1) +
                         ord(text[i + pattern_length])) % prime1
            if text_hash1 < 0:
                text_hash1 += prime1

    end_time = time.perf_counter()
    execution_time = end_time - start_time

    return text, pattern, matches, execution_time

def main():
    seq_x = input("Enter first sequence: ").upper()
    seq_y = input("Enter second sequence: ").upper()

    text, pattern, matches, time_taken = double_hash_rabin_karp(seq_x, seq_y)

    print(f"\ntext: {text}")
    print(f"pattern: {pattern}")
    print(f"number of matches: {matches}")
    print(f"execution time: {time_taken:.6f} seconds")

if __name__ == "__main__":
    main()