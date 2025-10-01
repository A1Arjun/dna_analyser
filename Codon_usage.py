from Bio import SeqIO

# Function to split sequence into codons
def get_codons(seq):
    codons = [str(seq[i:i+3]) for i in range(0, len(seq)-2, 3)]
    return codons

# Dictionary to store codon counts
codon_counts = {}

# Read sequences from FASTA
for record in SeqIO.parse("multipleseq.fasta", "fasta"):
    seq = record.seq.upper()
    codons = get_codons(seq)
    for codon in codons:
        if codon in codon_counts:
            codon_counts[codon] += 1
        else:
            codon_counts[codon] = 1

# Print codon usage
total_codons = sum(codon_counts.values())
print("Codon\tCount\tFrequency")
for codon in codon_counts:
    frequency = codon_counts[codon] / total_codons
    print(f"{codon}\t{codon_counts[codon]}\t{frequency:.4f}")
