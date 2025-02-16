import time

def bad_character_heuristic(pattern):
    """ Bad character heuristic for Boyer-Moore. """
    bad_char = [-1] * 256
    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i
    return bad_char

def boyer_moore_search(text, pattern):
    """ Boyer-Moore string matching algorithm. """
    start_time = time.perf_counter()
    m, n = len(pattern), len(text)
    bad_char = bad_character_heuristic(pattern)
    matches, shift = 0, 0

    while shift <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
        if j < 0:
            matches += 1
            shift += (m - bad_char[ord(text[shift + m])] if shift + m < n else 1)
        else:
            shift += max(1, j - bad_char[ord(text[shift + j])])
    
    exec_time = time.perf_counter() - start_time
    return text, pattern, matches, exec_time

def main():
    # Take input from the user
    seq_x = input("Enter first DNA sequence: ").strip()
    seq_y = input("Enter second DNA sequence: ").strip()

    # Identify text and pattern
    text, pattern = (seq_x, seq_y) if len(seq_x) >= len(seq_y) else (seq_y, seq_x)

    # Run Boyer-Moore search
    text, pattern, matches, exec_time = boyer_moore_search(text, pattern)

    # Output results
    print("\nResults:")
    print(f"text: {text}")
    print(f"pattern: {pattern}")
    print(f"number of matches: {matches}")
    print(f"Execution time: {exec_time:.6f} seconds")

if __name__ == "__main__":
    main()