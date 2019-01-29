from Bio import pairwise2, SeqIO
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


id_list = []
seq_list = []
score_list = []

path = input("\nFASTA input file path => ")

with open(path, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
                id_list.append(record.id)
                seq_list.append(record.seq)

for a_element in seq_list:

    len_a = len(a_element)

    for b_element in seq_list:
        
        list_seq_cov = []
        len_b = len(b_element)

        list_seq_cov.append(len_b)
        list_seq_cov.append(len_a)

        lenght = max(list_seq_cov)

        score = pairwise2.align.globalms(a_element, b_element, 2, -1, -0.5, -0.1, score_only=True)
        max_score = lenght * 2
        Similarity = score/max_score
        score_list.append(Similarity)

array_scores = np.array(score_list)
dime = len(id_list)

array_scores = array_scores.reshape((dime, dime))
df_seq = pd.DataFrame(data = array_scores, columns = id_list, index = id_list)

print("\nSimilarity matrix\n")
print(df_seq)

sns.clustermap(df_seq, cmap="coolwarm", annot=True)

plt.tight_layout()
plt.show()