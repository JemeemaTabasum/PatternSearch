import time
import random
import matplotlib.pyplot as plt
import numpy as np
from Bio import SeqIO
from naive_matching import *
from rabin_karp import *
from double_hash_rabin_karp import *
from improved_rabin_karp import *

# Function to read the genome sequence from a FASTA file
def read_genome_from_fasta(file_path):
    with open(file_path, "r") as file:
        # Parse the FASTA file and extract the sequence
        record = SeqIO.read(file, "fasta")
        return str(record.seq)

# Generate random substrings as patterns
def generate_patterns(genome, lengths, num_patterns=5):
    patterns = {length: [] for length in lengths}
    genome_length = len(genome)
    for length in lengths:
        for _ in range(num_patterns):
            start = random.randint(0, genome_length - length)
            patterns[length].append(genome[start:start + length])
    return patterns

# Measure execution time of a function
def measure_time(func, text, pattern):
    start_time = time.perf_counter()
    _, _, _, exec_time = func(text, pattern)
    return exec_time

# Define wrapper functions for each algorithm
def naive_match(text, pattern):
    return naive_string_match(text, pattern)

def rabin_single_match(text, pattern):
    return rabin_karp_match(text, pattern)

def rabin_double_match(text, pattern):
    return double_hash_rabin_karp(text, pattern)

def improved_rabin_match(text, pattern):
    return irk_search(text, pattern, 256, 101)

# Main experiment function
def run_experiment(genome, pattern_lengths):
    patterns = generate_patterns(genome, pattern_lengths)
    results = {algo: [] for algo in ["Naive", "Rabin Single", "Rabin Double", "Improved Rabin"]}

    for length in pattern_lengths:
        naive_times, rabin_single_times, rabin_double_times, improved_rabin_times = [], [], [], []
        
        for pattern in patterns[length]:
            naive_times.append(measure_time(naive_match, genome, pattern))
            rabin_single_times.append(measure_time(rabin_single_match, genome, pattern))
            rabin_double_times.append(measure_time(rabin_double_match, genome, pattern))
            improved_rabin_times.append(measure_time(improved_rabin_match, genome, pattern))
        
        results["Naive"].append(np.mean(naive_times))
        results["Rabin Single"].append(np.mean(rabin_single_times))
        results["Rabin Double"].append(np.mean(rabin_double_times))
        results["Improved Rabin"].append(np.mean(improved_rabin_times))
    
    return results

# Plot results
def plot_results(pattern_lengths, results):
    plt.figure(figsize=(10, 6))
    for algo, times in results.items():
        plt.plot(pattern_lengths, times, marker="o", label=algo)
    
    plt.xlabel("Pattern Length")
    plt.ylabel("Avg. Execution Time (seconds)")
    plt.title("Pattern Matching Algorithm Performance on E. coli Genome")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    fasta_file_path = "./U00096.3.fasta"  
    genome = read_genome_from_fasta(fasta_file_path)  # Read the genome sequence from the FASTA file
    pattern_lengths = list(range(4, 20, 2))  # Testing pattern lengths from 4 to 20
    results = run_experiment(genome, pattern_lengths)
    plot_results(pattern_lengths, results)
