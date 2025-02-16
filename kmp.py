import time

def compute_lps(pattern):
    """ Compute LPS array for KMP algorithm. """
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    """ KMP algorithm to find pattern in text. """
    start_time = time.perf_counter()
    lps = compute_lps(pattern)
    i = j = 0
    matches = 0

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            matches += 1
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    exec_time = time.perf_counter() - start_time
    return text, pattern, matches, exec_time

def main():
    # Take input from the user
    seq_x = input("Enter first DNA sequence: ").strip()
    seq_y = input("Enter second DNA sequence: ").strip()

    # Identify text and pattern
    text, pattern = (seq_x, seq_y) if len(seq_x) >= len(seq_y) else (seq_y, seq_x)

    # Run KMP search
    text, pattern, matches, exec_time = kmp_search(text, pattern)

    # Output results
    print("\nResults:")
    print(f"text: {text}")
    print(f"pattern: {pattern}")
    print(f"number of matches: {matches}")
    print(f"Execution time: {exec_time:.6f} seconds")

if __name__ == "__main__":
    main()
