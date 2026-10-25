
import streamlit as st

st.set_page_config(
    page_title="DNA Sequence Analyzer",
    page_icon="🧬",
    layout="centered"
)

st.title("🧬 DNA Sequence Analyzer")
st.write("Analyze DNA sequences using simple bioinformatics tools.")

dna = st.text_area(
    "Enter your DNA sequence",
    placeholder="Example: ATGCGATCGATC"
)

if st.button("Analyze DNA"):
    dna = "".join(dna.upper().split())

    if not dna:
        st.error("Please enter a DNA sequence.")

    elif any(base not in "ATGC" for base in dna):
        st.error("Invalid sequence! Use only A, T, G and C.")

    else:
        length = len(dna)
        a = dna.count("A")
        t = dna.count("T")
        g = dna.count("G")
        c = dna.count("C")

        gc_content = ((g + c) / length) * 100
        rna = dna.replace("T", "U")

        complement_table = str.maketrans("ATGC", "TACG")
        complement = dna.translate(complement_table)
        reverse_complement = complement[::-1]

        st.success("DNA sequence analyzed successfully!")

        st.subheader("📊 Analysis Results")

        col1, col2 = st.columns(2)

        col1.metric("Sequence Length", length)
        col2.metric("GC Content", f"{gc_content:.2f}%")

        st.write("### Nucleotide Counts")

        st.write(f"Adenine (A): {a}")
        st.write(f"Thymine (T): {t}")
        st.write(f"Guanine (G): {g}")
        st.write(f"Cytosine (C): {c}")

        st.write("### 🔬 Sequence Conversions")

        st.write("**Original DNA:**")
        st.code(dna)

        st.write("**RNA Sequence:**")
        st.code(rna)

        st.write("**Complementary DNA:**")
        st.code(complement)

        st.write("**Reverse Complement:**")
        st.code(reverse_complement)


        st.subheader("📈 Nucleotide Composition")

        import pandas as pd

        chart_data = pd.DataFrame({
            "Nucleotide": ["A", "T", "G", "C"],
            "Count": [a, t, g, c]
        })

    st.bar_chart(chart_data.set_index("Nucleotide"))



st.caption("DNA Sequence Analyzer | Built with Python and Streamlit")

