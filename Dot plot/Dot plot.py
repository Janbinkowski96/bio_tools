"""Dot plot na podstawie sekwencji własnych lub pobranych z NCBI"""

from Bio import SeqIO, Entrez, AlignIO, pairwise2
import pylab
seq_one_desc = ""
seq_two_desc = ""

Entrez.email = "contact@gene-calc.pl"

coverage_list = list()
name = list()
seq = list()
len_list = list()
dict_one = dict()
dict_two = dict()
x = list()
y = list()

type_of_data = input("Type of data: raw sequences [1] or sequences from GenBank [2] > ")

if type_of_data == "1": 
    seq_one_name = input("sequence 1 name: ")
    seq_one = input("sequence 1: ")

    seq_two_name = input("sequence 2 name: ")
    seq_two = input("sequence 2: ")

elif type_of_data == "2":
    seq_id_one = input("ID of sequence 1: ")
    seq_id_two = input("ID of sequence 2: ")
    
    with Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id=seq_id_one) as handle:
        seq_record_one = SeqIO.read(handle, "gb")
        seq_one_name = seq_record_one.id
        seq_one = seq_record_one.seq
        seq_one_desc = seq_record_one.description

    with Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id=seq_id_two) as handle:
         seq_record_two = SeqIO.read(handle, "gb")
         seq_two_name = seq_record_two.id
         seq_two = seq_record_two.seq
         seq_two_desc = seq_record_two.description

else:
    print("Error")

seq_one_name = str(seq_one_name)
seq_two_name = str(seq_two_name)
seq_one = str(seq_one)
seq_two = str(seq_two)

name = [seq_one_name, seq_two_name] # lista z nazwami sekwencji
seq = [seq_one, seq_two] # lista z sekwencjami

file = open("seq_file.fasta", "w") # otrzymane sekwencje przechowywane są w pliku seq_file w formacie FASTA dla dot plot

for data in range(len(seq)): # przekształcenie danych do formatu FASTA
    file.write(">" + name[data] + "\n" + seq[data] + "\n")
file.close()

file = open("seq_alignment_one.txt", "w") # otrzymane sekwencje przechowywane są w pliku seq_file w formacie FASTA dla alignmentu seq_one
file.write(">" + seq_one_name + "\n" + seq_one + "\n")
file.close()

file = open("seq_alignment_two.txt", "w") # otrzymane sekwencje przechowywane są w pliku seq_file w formacie FASTA dla alignmentu seq_two
file.write(">" + seq_two_name + "\n" + seq_two + "\n")
file.close()

seq1 = SeqIO.read("seq_alignment_one.txt", "fasta")
seq2 =SeqIO.read("seq_alignment_two.txt", "fasta")

alignments = pairwise2.align.globalxx(seq1.seq, seq2.seq)

ident =  pairwise2.format_alignment(*alignments[0]).count("|")
print(ident)
average_lenght = (len(seq1.seq) + len(seq2.seq))/2
average_identifity = (ident / average_lenght) * 100

len_list.append(len(seq1.seq))
len_list.append(len(seq2.seq))

frag_identifity = (ident / min(len_list)) * 100

coverage1 = len(seq1.seq) / len(seq2.seq) * 100
coverage2 = len(seq2.seq) / len(seq1.seq) * 100
coverage_list.append(coverage1)
coverage_list.append(coverage2)

print("coverage {}%".format(round(min(coverage_list), 1)))
print("average identity {}%".format(round(average_identifity, 1)))
print("fragmental identity {}%".format(round(frag_identifity, 1)))

with open("seq_file.fasta") as in_handle:  # dot plot
    record_iterator = SeqIO.parse(in_handle, "fasta")
    rec_one = next(record_iterator)
    rec_two = next(record_iterator)

window = 8

for (seq, section_dict) in [(str(rec_one.seq).upper(), dict_one),
                            (str(rec_two.seq).upper(), dict_two)]:
   for i in range(len(seq)-window):
        section = seq[i:i+window]
        try:
            section_dict[section].append(i)
        except KeyError:
                section_dict[section] = [i]

matches = set(dict_one).intersection(dict_two)

for section in matches:
    for i in dict_one[section]:
        for j in dict_two[section]:
            x.append(i)
            y.append(j)

pylab.cla() 
pylab.gray()
pylab.scatter(x,y)
pylab.xlim(0, len(rec_one)-window)
pylab.ylim(0, len(rec_two)-window)
pylab.xlabel("{}s (length {} bp)\n{} ...".format(rec_one.id, len(rec_one), seq_one_desc[:50]))
pylab.ylabel("{}s (length {} bp)\n{} ...".format(rec_two.id, len(rec_two), seq_two_desc[:50]))
pylab.title("Dot plot\nGene-Calc")
pylab.show()


