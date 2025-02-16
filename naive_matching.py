def naive_string_match(seq_x: str, seq_y: str):
    """
    Implements naive string matching algorithm to find if one DNA sequence
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

    # Iterate through all possible positions in text
    for i in range(text_length - pattern_length + 1):
        match = True

        # For each position, check if pattern matches
        for j in range(pattern_length):
            if text[i + j] != pattern[j]:
                match = False
                break

        if match:
            matches += 1

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return text, pattern, matches, execution_time

def main():
    seq_x = input("Enter first DNA sequence: ").upper()
    seq_y = input("Enter second DNA sequence: ").upper()

    # Perform matching
    text, pattern, matches, time_taken = naive_string_match(seq_x, seq_y)

    # Display results
    print(f"\ntext: {text}")
    print(f"pattern: {pattern}")
    print(f"number of matches: {matches}")
    print(f"execution time: {time_taken:.6f} seconds")

if __name__ == "__main__":
    main()