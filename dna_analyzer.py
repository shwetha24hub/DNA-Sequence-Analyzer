print("=== DNA Sequence Analyzer ===")

dna = input("Enter your DNA sequence: ").upper().strip()

if not dna:
    print("Please enter a DNA sequence.")

elif any(base not in "ATGC" for base in dna):
    print("Invalid DNA sequence! Use only A, T, G, C.")

else:
    length = len(dna)

    a = dna.count("A")
    t = dna.count("T")
    g = dna.count("G")
    c = dna.count("C")

    gc_content = ((g + c) / length) * 100

    print("\n--- Results ---")
    print("Sequence length:", length)
    print("Adenine (A):", a)
    print("Thymine (T):", t)
    print("Guanine (G):", g)
    print("Cytosine (C):", c)
    print("GC Content:", round(gc_content, 2), "%")