from Bio import SeqIO

# Function to find ORFs in a sequence
def find_orfs(seq):
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    orfs = []

    for frame in range(3):
        for i in range(frame, len(seq)-2, 3):
            codon = str(seq[i:i+3])
            if codon == start_codon:
                for j in range(i+3, len(seq)-2, 3):
                    stop_codon = str(seq[j:j+3])
                    if stop_codon in stop_codons:
                        orfs.append((i+1, j+3, seq[i:j+3]))
                        break
    return orfs

# Read multi-sequence FASTA file
for record in SeqIO.parse("multipleseq.fasta", "fasta"):
    seq = record.seq.upper()
    orfs = find_orfs(seq)
    print(f"\nSequence ID: {record.id}")
    if orfs:
        for start, end, orf_seq in orfs:
            print(f"ORF from {start} to {end}, Length: {len(orf_seq)}")
    else:
        print("No ORFs found.")
