from __future__ import division
from tinyfasta import FastaParser

def fasta_low_base_ratio(fasta_file):
    lenAll = []
    lowerAll = []
    for record in FastaParser(fasta_file):
        seq = str(record.sequence)
        seqLen = len(seq)
        lenAll.append(seqLen)
        lowCount = 0
        for s in seq:
            if s.islower():
                lowCount += 1
        lowerAll.append(lowCount)
    lowerRatio = sum(lowerAll) / sum(lenAll)
    return lowerRatio

