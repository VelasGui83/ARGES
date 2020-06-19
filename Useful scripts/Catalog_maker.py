import sys
from Bio import SeqIO

# We create four files that will contain different information:
# 'AMRG.gc.v3.fasta' will contain the fasta including the short header + the original header
# 'AMRG.gc.v3.headers' will contain only the headers previously mentioned
# 'AMRG.gc.v3.geneID.only.headers.fasta' will contain is a fasta with short headers 
# 'AMRG.gc.v3.correspondance.headers' will contain a file that separated by a tab the original header and the short header
with open('AMRG.gc.v3.fasta', 'w') as new_headers_fasta, open('AMRG.gc.v3.headers', 'w') as headers, open('AMRG.gc.v3.geneID.only.headers.fasta', 'w') as short_headers_fasta, open('AMRG.gc.v3.correspondance.headers', 'w') as correspondance:
    gene_number=0
    # sys.argv[1] is the name of the fasta file with all the sequences concatenated from the four reference databases (NDARO, CARD, MEGARes and INTEGRALL) after applying filter_sequences.py
    # sys.argv[2] is the called prefix that will be added to the original header in order to create a unique short identifier in our case "AMRG.gc.v3.gene_"
    for seq_record in SeqIO.parse(sys.argv[1], "fasta"):
        gene_number+=1
        new_headers_fasta.write(">" + sys.argv[2] + str(gene_number) + "__" + str(seq_record.id) + "\n" + str(seq_record.seq).upper() + "\n")
        headers.write(">" + sys.argv[2] + str(gene_number) + "__" + str(seq_record.id) + "\n")
        short_headers_fasta.write(">" + sys.argv[2] + str(gene_number) + "\n" + str(seq_record.seq).upper() + "\n")
        correspondance.write(">" + sys.argv[2] + str(gene_number) + "__" + str(seq_record.id) + "\t" + ">" + sys.argv[2] + str(gene_number) + "\n")
