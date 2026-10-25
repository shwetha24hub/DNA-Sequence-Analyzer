
print("=== DNA Sequence Analyzer ===")

dna = input("Enter your DNA sequence: ").upper().strip()

if not dna:
    print("Please enter a DNA sequence.")

elif any(base not in "ATGC" for base in dna):
    print("Invalid DNA sequence! Use only A, T, G, C.")

else:
    length = len(dna)

    print("\n--- DNA Analysis ---")
    print("Sequence length:", length)
    print("Adenine (A):", dna.count("A"))
    print("Thymine (T):", dna.count("T"))
    print("Guanine (G):", dna.count("G"))
    print("Cytosine (C):", dna.count("C"))

    gc_content = ((dna.count("G") + dna.count("C")) / length) * 100
    print("GC Content:", round(gc_content, 2), "%")

    rna = dna.replace("T", "U")
    print("RNA Sequence:", rna)

    complement_table = str.maketrans("ATGC", "TACG")
    complement = dna.translate(complement_table)
    reverse_complement = complement[::-1]

    print("Complementary DNA:", complement)
    print("Reverse Complement:", reverse_complement)

