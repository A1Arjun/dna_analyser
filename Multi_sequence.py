from Bio import SeqIO

# Read multi sequences from FASTA
for record in SeqIO.parse("multipleseq.fasta",'fasta'):
  seq = record.seq.upper()

  print(f"\n-- Analyzing: {record.id}")
  print(f"Sequence Length: {len(seq)}")

  # nucleotide count
  print(f"Nucleotide count = {{'A': {seq.count('A')}, 'T': {seq.count('T')}, 'C': {seq.count('C')}, 'G': {seq.count('G')}}}")
  
  #gc content
  gc = ((seq.count('G') + seq.count('C')) / len(seq)) * 100
  print(f'GC% = {gc:.2f}')
  
  # Reverse complement
  print(f"Reverse Complement: {seq.reverse_complement()}")
  
  # Transcription (DNA → RNA)
  print(f"RNA : {seq.transcribe()}")
  
  # Translation (DNA → Protein)
  print(f"Protein : {seq.translate()}")
