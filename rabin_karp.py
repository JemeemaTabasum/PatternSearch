def rabin_karp_match(seq_x: str, seq_y: str):
    """
    Implements Rabin-Karp string matching algorithm to find if one DNA sequence
    is a subsequence of another.

    Args:
        seq_x: First DNA sequence
        seq_y: Second DNA sequence

    Returns:
        tuple: (text, pattern, number_of_matches, execution_time)
        where text is the longer sequence and pattern is the subsequence to find
    """
    import time
    start_time = time.perf_counter()

    # Determine which sequence is longer to identify text and pattern
    if len(seq_x) >= len(seq_y):
        text = seq_x
        pattern = seq_y
    else:
        text = seq_y
        pattern = seq_x

    text_length = len(text)
    pattern_length = len(pattern)
    matches = 0

    # Edge cases
    if pattern_length == 0 or pattern_length > text_length:
        end_time = time.perf_counter()
        return text, pattern, 0, end_time - start_time

    # Numbers for rolling hash calculation
    prime = 101  # A prime number for hash calculation
    d = 256     # Using 256 for ASCII characters

    # Calculate hash value for pattern and first window of text
    pattern_hash = 0
    text_hash = 0
    h = 1

    # Calculate h = d^(pattern_length-1) % prime
    for i in range(pattern_length - 1):
        h = (h * d) % prime

    # Calculate initial hash values
    for i in range(pattern_length):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % prime
        text_hash = (d * text_hash + ord(text[i])) % prime

    # Slide pattern over text one by one
    for i in range(text_length - pattern_length + 1):
        # Check if hash values match
        if pattern_hash == text_hash:
            # Check characters one by one
            match = True
            for j in range(pattern_length):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                matches += 1

        # Calculate hash value for next window of text
        if i < text_length - pattern_length:
            text_hash = (d * (text_hash - ord(text[i]) * h) +
                        ord(text[i + pattern_length])) % prime

            # We might get negative hash, converting it to positive
            if text_hash < 0:
                text_hash += prime

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return text, pattern, matches, execution_time

def main():
    seq_x = input("Enter first DNA sequence: ").upper()
    seq_y = input("Enter second DNA sequence: ").upper()

    # Perform matching
    text, pattern, matches, time_taken = rabin_karp_match(seq_x, seq_y)

    # Display results
    print(f"\ntext: {text}")
    print(f"pattern: {pattern}")
    print(f"number of matches: {matches}")
    print(f"execution time: {time_taken:.6f} seconds")

if __name__ == "__main__":
    main()