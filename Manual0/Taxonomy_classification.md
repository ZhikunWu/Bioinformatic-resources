
# Taxonomy classification (from usearch)

## [Taxonomy overclassification and underclassification errors](https://www.drive5.com/usearch/manual/tax_overclass.html)

### Lowest Common Rank (LCR)

The lowest common rank is defined to be the lowest level (genus, family etc.) that is present in the reference set (training set). For example, if the genus is not present but the family is present, then the lowest common level is family. Predicting the LCR is the most difficult challenge for a taxonomy classification algorithm. For example, if the identity of the top hit is 88%, should be LCR be class, family, genus or what?

### Overclassification error

If a classifier predicts a level lower than the LCR, then this is an overclassification error. For example, the lowest common level is family but a genus is predicted.

### Underclassification error

If a classifier predicts higher levels but does not predict the LCR, then this is an underclassification error. For example, the lowest common level is family but the lowest predicted level is order. All false negatives are underclassification errors so there is really no need for a new term.

## [Taxonomy confidence measures](https://www.drive5.com/usearch/manual/tax_conf.html)

Most taxonomy prediction algorithms don't provide a confidence estimate, including [GAST](http://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1000255), the default QIIME method ([assign_taxonomy.py](http://qiime.org/scripts/assign_taxonomy.html) ‑m uclust) and the mothur [Classify_seqs command](http://www.mothur.org/wiki/Classify.seqs) with method=knn. A notable exception is the [RDP Naive Bayesian Classifier (RDP)](https://rdp.cme.msu.edu/classifier/class_help.jsp) which reports a confidence value obtained by [boostrapping](https://en.wikipedia.org/wiki/Bootstrapping_(statistics). This was an important improvement over previous methods and is a good reason why RDP is currently the most widely-used algorithm for 16S taxonomy prediction.


The SINTAX algorithm generates taxonomy predictions with confidence estimates specified as a bootstrap value.

The SINTAX boostrap value has similar accuracy to RDP on V4 sequences. On ITS sequences and full-length 16S sequences, the SINTAX boostrap value is significantly better (see [SINTAX paper](https://www.drive5.com/usearch/manual/citation.html))

## [Taxonomy annotations](https://www.drive5.com/usearch/manual/tax_annot.html)

## [Taxonomy predictions](https://www.drive5.com/usearch/manual/tax_pred.html)

The format of a taxonomy prediction is the same as the names in a  taxonomy annotation except that a confidence level is specified for some or all of the names. For example:

d:Bacteria(1.00),p:Firmicutes(0.98),c:Clostridia,o:Halanaerobiales,f:Halobacteroidaceae(0.75)

A confidence level appears parentheses following the taxon name and is in the range 0.0 to 1.0.

If a confidence threshold is used then a resolved prediction is generated which keeps only names with confidences meeting the threshold. For example, with a threshold of 0.9 the resolved prediction for the above example is:

d:Bacteria,p:Firmicutes