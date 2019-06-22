#!/usr/bin/env python

def get_uniq_blast_record(record, out_file):
    """
    Get unique record for blast result.

    argv:
        MIG.1547093     NW_005393270.1  5.32e-53        130     123     97.561  3       0       5       127     994492  994614  Bos mutus isolate yakQH1 unplaced 
    MIG.1547093     NW_005393270.1  3.27e-35        130     118     89.831  12      0       5       122     341260  341143  Bos mutus isolate yakQH1 unplaced
    
    return:
        MIG.1547093     NW_005393270.1  5.32e-53        130     123     97.561  3       0       5       127     994492  994614  Bos mutus isolate yakQH1 unplaced
    """
    in_h = open(record, "r")
    out_h = open(out_file, "w")
    first = in_h.readline().strip()
    preGene = first.split("\t")[0]
    for line in in_h:
        line = line.strip()
        lines = line.split("\t")
        Gene = lines[0]
        if Gene == preGene:
            continue
        else:
            out_h.write("%s\n" % line)
        preGene = Gene
    in_h.close()
    out_h.close()