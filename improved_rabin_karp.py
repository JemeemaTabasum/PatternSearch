import time

def irk_search(text, pattern, d, q):
    n = len(text)  # Length of the text
    m = len(pattern)  # Length of the pattern
    h = pow(d, m-1, q)  # Precomputed h value (d^(m-1) % q)
    p = 0  # Hash value for pattern
    t = 0  # Hash value for text window
    q_p = 0  # Quotient for pattern
    q_t = 0  # Quotient for text
    matches = 0
    start_time = time.perf_counter()

    # Preprocessing: Compute initial hash values and quotients
    for i in range(m):
        temp_p = (d * p + ord(pattern[i])) % q
        p = temp_p % q  # Compute remainder for pattern
        q_p = temp_p // q  # Compute quotient for pattern

        temp_t = (d * t + ord(text[i])) % q
        t = temp_t % q  # Compute remainder for text
        q_t = temp_t // q  # Compute quotient for text

    # Pattern matching
    for s in range(n - m + 1):
        # Check if both remainder and quotient match
        if p == t and q_p == q_t:
            if text[s:s+m] == pattern:
                matches += 1
                print(f"Pattern occurs with shift {s}")

        # Compute hash and quotient for next window
        if s < n - m:
            temp_t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q
            if temp_t < 0:  # Ensure non-negative hash
                temp_t += q
            t = temp_t % q  # Compute new remainder
            q_t = temp_t // q  # Compute new quotient

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return text, pattern, matches, execution_time

def main():
    seq_x = input("Enter first sequence: ").upper()
    seq_y = input("Enter second sequence: ").upper()

    # Determine which sequence is longer
    if len(seq_x) >= len(seq_y):
        text = seq_x
        pattern = seq_y
    else:
        text = seq_y
        pattern = seq_x

    d = 256  # ASCII characters as base
    test_prime = 101  # Prime number for hashing

    # Perform matching
    text, pattern, matches, time_taken = irk_search(text, pattern, d, test_prime)

    # Display results
    print(f"\nText: {text}")
    print(f"Pattern: {pattern}")
    print(f"Number of matches: {matches}")
    print(f"Execution time: {time_taken:.6f} seconds")

if __name__ == "__main__":
    main()
