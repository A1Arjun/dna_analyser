from bio import SeqIO

#read single sequence from Fasta
record=SeqIO.read("sequence.fasta.txt",'fasta')
seq=record.seq.upper()

#Nucleotide count
print(f"nucleotide count= ['A' : {seq.count('A')},'T' : {seq.count('T')},'C' : {seq.count('C')},'G' : {seq.count('G')}]")

#GC content
gc=((seq.count('G')+seq.count('C'))/len(seq))*100
print(f'GC% = {gc :.2f}')

#Reverse complement
print(f'Reverse Complement: {seq.reverse_complement()}')

#Transcription (dna to rna)
print(f'RNA : {seq.transcribe()}')

#Translation (dna to protein)
print(f'Protein : {seq.translate()}')
