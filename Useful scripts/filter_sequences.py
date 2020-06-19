import sys
from Bio import SeqIO

# In the study it has not been taken into account the clustering of sequences neither if
# one sequece was part of the other because we considered that the databases from where the sequences
# came from were strongly curated however, it might be a good point in the future to cosider this aspects in future versions
# of the database   

def sequence_cleaner(fasta_file, min_length=0, por_n=100):
    # Create our hash table to add the sequences
    sequences={}

    # We use the Biopython fasta parse to read our fasta input
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
        # Takes the current sequence
        sequence = str(seq_record.seq).upper()
        # Checks if the current sequence is according to the parameters
	# We first check if the sequence is shorter than 100bp
        if (len(sequence) >= min_length and
            (float(sequence.count("N"))/float(len(sequence)))*100 <= por_n):
        # If the sequence passed in the test and it isn't in the
        # hash table, the sequence and its id are going to be in the hash
	# This is made in order to remove identical sequences
            if sequence not in sequences:
                sequences[sequence] = seq_record.id
       # If it is already in the hash table, we're just gonna concatenate the ID
       # of the current sequence to another one that is already in the hash table
            else:
                sequences[sequence] += "_" + seq_record.id


    # Write the clean sequences

    # Create a file in the same directory where the script is run
    with open("clear_" + fasta_file, "w+") as output_file:
        # Just read the hash table and write on the file as a fasta format
        for sequence in sequences:
            output_file.write(">" + sequences[sequence] + "\n" + sequence + "\n")

    print("CLEAN!!!\nPlease check clear_" + fasta_file)


userParameters = sys.argv[1:]

# sys.argv[1] is the name of the fasta file with all the sequences concatenated from the four reference databases (NDARO, CARD, MEGARes and INTEGRALL)
# sys.argv[2] is the minimum sequence length in the resulting fasta in our case 100bp

try:
    if len(userParameters) == 1:
        sequence_cleaner(userParameters[0])
    elif len(userParameters) == 2:
        sequence_cleaner(userParameters[0], float(userParameters[1]))
    elif len(userParameters) == 3:
        sequence_cleaner(userParameters[0], float(userParameters[1]),
                         float(userParameters[2]))
    else:
        print("There is a problem!")
except:
    print("There is a problem!")
