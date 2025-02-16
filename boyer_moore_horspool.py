import time

def bmh_bad_character_table(pattern):
    """ Creates the bad character heuristic table for Boyer–Moore–Horspool. """
    m = len(pattern)
    bad_char = {char: m for char in set(pattern)}
    for i in range(m - 1):
        bad_char[pattern[i]] = m - 1 - i
    return bad_char

def boyer_moore_horspool_search(text, pattern):
    """ Boyer–Moore–Horspool algorithm. """
    start_time = time.perf_counter()
    m, n = len(pattern), len(text)
    bad_char = bmh_bad_character_table(pattern)
    matches, shift = 0, 0

    while shift <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
        if j < 0:
            matches += 1
            shift += bad_char.get(text[shift + m], m) if shift + m < n else 1
        else:
            shift += bad_char.get(text[shift + j], m)

    exec_time = time.perf_counter() - start_time
    return text, pattern, matches, exec_time

def main():
    # Take input from the user
    seq_x = input("Enter first DNA sequence: ").strip()
    seq_y = input("Enter second DNA sequence: ").strip()

    # Identify text and pattern
    text, pattern = (seq_x, seq_y) if len(seq_x) >= len(seq_y) else (seq_y, seq_x)

    # Run Boyer-Moore-Horspool search
    text, pattern, matches, exec_time = boyer_moore_horspool_search(text, pattern)

    # Output results
    print("\nResults:")
    print(f"text: {text}")
    print(f"pattern: {pattern}")
    print(f"number of matches: {matches}")
    print(f"Execution time: {exec_time:.6f} seconds")

if __name__ == "__main__":
    main()
