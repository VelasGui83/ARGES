# ARGES
## Folding the catalogue<br/>
ARGES catalogue is composed by Antibiotic Resistant Gene (ARG) sequences obtained from different 
databases. 
First of all, ARGs were obtained from the National Database of 
Antibiotic Resistant Organisms (NDARO) [1](#NDARO) using the data version 2019-09-06.1. Composed of 5120 sequences of ARGs.<br/>
Once this genes were included, the Comprehensive Antibiotic Resistance 
Database (CARD) \cite{card} was used to enrich the number of ARGs inside 
the catalogue. From this database, the selection of the ARGs was hand-
made just choosing different ARGs families according to the antibiotics they 
generate resistance to. It is important to know that all the families of 
antibiotics selected are important groups of antibiotics used in present 
medicine. The families selected were: Aminoglycosides (Phospho (APH), 
Adenyl(AAD) and Acetyl (AAC)), beta-lactamases (Extended spectrum 
$\beta$-lactamases, carbapenems), Chloramphenicol, Colistine, Fosfomycin,
Fluoroquinolone (QNR and QRDR), Glycopeptides, Lincosamide, Macrolides, 
Syntetic drugs (Nitrofurantoin and Sulfonamides), Tetracycline. After the 
selection the number of sequences included was of 1564.<br/>
Then it was included the MEGARes database \cite{megares}. The version 
database used in this study is the 1.0.1 (December 2016). It includes 
manually-curated sequences and annotations of multiple antimicrobial 
resistant genes. Composed of 3824 antimicrobial resistance genes.<br/>
Finally, in order to have information of integrons, integrases and gene 
cassettes that may include parallel information of the transmission of this 
ARGs, it was included all the sequences from INTEGRALL database 
\cite{integrall}. Composed of 10022 sequences.<br/>
After concatenating all the sequences from the four databases redundancy 
was eliminated using a python script that concatenated headers of identical sequences. Also sequences shorter than 5 
nucleotides and also wrongly annotated were removed. After curation the 
ARGs catalogue contained 11715 sequences.<br/>
## Format<br/>
Gene entries were named as "AMRG.gc.v3.gene_X" where X represents a unique numerical identifier. In file "AMRG.gc.v3.correspondance.headers" is composed of two columns, the first one determines the original header (previous to unique numerical identifier) and a second column corresponding the numerical identifier in order to be able to know the original name if needed.
## ARGES Team<br/>
ARGES catalogue is maintained by a group of researchers. Can be contacted:
- Daniel Velasco Guisado
- Ramiro Logares
- Yuly López
## References<br/>
1. <a name="NDARO"></a> National Database of Antibiotic Resistant Organisms;.  Available from:
www.ncbi.nlm.nih.gov/pathogens/antimicrobial-resistance/
.
2. Alcock BP, Raphenya AR, Lau TTY, Tsang KK, Bouchard M,
Edalatmand A, et al.  CARD 2020: antibiotic resistome surveillance with
the comprehensive antibiotic resistance database.  Nucleic Acids
Research. 2019 10;48(D1):D517–D525.  Available from:
https://doi.org/10.1093/nar/gkz935
.
3. Lakin SM, Dean C, Noyes NR, Dettenwanger A, Ross AS, Doster E,
et al.  MEGARes: an antimicrobial resistance database for high
throughput sequencing.  Nucleic Acids Research. 2016
11;45(D1):D574–D580.  Available from:
https://doi.org/10.1093/nar/gkw1009
.
