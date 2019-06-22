
blastn -query C03/UID_R0.t1.cf.fastq -db database/SILVA_NCBI_16SrDNA_Rename.fasta -outfmt "6 qseqid sseqid  evalue qlen length pident mismatch gapopen qstart qend sstart send  stitle"  -max_target_seqs 5 -out blast/C03_blast.txt -num_threads 6

