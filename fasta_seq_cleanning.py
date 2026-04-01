# Import files
import sys

#Input file
Input=sys.argv[1]

valid_base=set("ATGC")

sequence={}
seq_id=""
seq=""

#read fasta
with open(Input,"r")as f:
        for line in f:
                line=line.strip()
                if line.startswith(">"):
                        if seq_id:
                                sequence[seq_id]=seq
                        seq_id=line[1:]
                        seq=""
                else:
                        seq+=line.upper()
        if seq_id:
                sequence[seq_id]=seq
#cleaned seq
cleanned_seq={}
for id, sequence in sequence.items():
        cleanned=""
        for base in sequence:
                if base in valid_base:
                        cleanned+=base
                        cleanned_seq[id]=cleanned
#save new fasta file
with open("cleanned_seq.fasta","w")as out:
        for id,sequence in cleanned_seq.items():
                out.write(f">{id}\n")
                out.write(sequence +"\n")
print("cleaned fasta file is created")
