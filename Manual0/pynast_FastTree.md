
### pynast lignment
```
$ align_seqs.py --i result/rep_seqs.fa  -m pynast -o result/temp.pynast_alignment
```

output three files
```
rep_seqs_aligned.fasta
rep_seqs_failures.fasta
rep_seqs_log.txt
```

### run pynast
```
$ FastTree  -nt result/temp.pynast_alignment/rep_seqs_aligned.fasta > result/temp.pynast_alignment/rep_seqs_aligned.tree
FastTree Version 2.1.3 SSE3

Alignment: result/temp.pynast_alignment/rep_seqs_aligned.fasta
Nucleotide distances: Jukes-Cantor Joins: balanced Support: SH-like 1000
Search: Normal +NNI +SPR (2 rounds range 10) +ML-NNI opt-each=1
TopHits: 1.00*sqrtN close=default refresh=0.80
ML Model: Jukes-Cantor, CAT approximation with 20 rate categories
Initial topology in 5.13 seconds0 of    972   975 seqs (at seed    900)   
Refining topology: 40 rounds ME-NNIs, 2 rounds ME-SPRs, 20 rounds ML-NNIs
Total branch-length 51.543 after 21.17 sec 701 of 973 splits, 2 changes (max delta 0.000)   
ML-NNI round 1: LogLk = -127317.154 NNIs 179 max delta 14.18 Time 35.51s (max delta 14.185)   
Switched to using 20 rate categories (CAT approximation)20 of 20   
Rate categories were divided by 0.674 so that average rate = 1.0
CAT-based log-likelihoods may not be comparable across runs
Use -gamma for approximate but comparable Gamma(20) log-likelihoods
ML-NNI round 2: LogLk = -104779.650 NNIs 110 max delta 10.96 Time 46.79s (max delta 10.959)   
ML-NNI round 3: LogLk = -104666.690 NNIs 34 max delta 16.27 Time 52.62s (max delta 16.268)   
ML-NNI round 4: LogLk = -104631.650 NNIs 8 max delta 10.01 Time 56.01s (max delta 10.006)   
ML-NNI round 5: LogLk = -104624.261 NNIs 4 max delta 1.32 Time 57.50es (max delta 1.320)   
ML-NNI round 6: LogLk = -104617.091 NNIs 1 max delta 6.52 Time 58.10
ML-NNI round 7: LogLk = -104609.352 NNIs 3 max delta 3.33 Time 58.29
ML-NNI round 8: LogLk = -104608.596 NNIs 1 max delta 0.22 Time 58.48
ML-NNI round 9: LogLk = -104608.588 NNIs 0 max delta 0.00 Time 58.62
Turning off heuristics for final round of ML NNIs (converged)
ML-NNI round 10: LogLk = -104371.224 NNIs 9 max delta 0.88 Time 69.97 (final)delta 0.876)   
Optimize all lengths: LogLk = -104363.628 Time 72.61
Total time: 97.72 seconds Unique: 975/975 Bad splits: 4/972 Worst delta-LogLk 1.114

```
output file:
```
result/temp.pynast_alignment/rep_seqs_aligned.tree
```

### plot tree using [graphlan](https://bitbucket.org/nsegata/graphlan/wiki/Home)

```
graphlan_annotate.py result/temp.pynast_alignment/rep_seqs_aligned.tree result/temp.pynast_alignment/rep_seqs_aligned.tree.xml

graphlan.py result/temp.pynast_alignment/rep_seqs_aligned.tree.xml result/temp.pynast_alignment/rep_seqs_aligned.tree.svg --dpi 300 --size 10
```

