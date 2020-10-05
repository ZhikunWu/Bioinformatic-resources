# [Multiple sequence alignment](https://en.wikipedia.org/wiki/Multiple_sequence_alignment)

A **multiple sequence alignment (MSA)** is a sequence alignment of three or more biological
sequences, generally protein, DNA, or RNA. In many cases, the input set of query sequences 
are assumed to have an evolutionary relationship by which they share a linkage and are 
descended from a common ancestor.


## [An Overview of Multiple Sequence Alignments and Cloud Computing in Bioinformatics](https://www.hindawi.com/journals/isrn/2013/615630/)

Progressive alignment is the foundation
procedure of several popular alignment algorithms such as:

* ClustalW
* Clustal Omega
* MAFFT
* Kalign
* Probalign
* MUSCLE
* DIALIGN
* PRANK
* FSA
* T-Coﬀee
* ProbCons
* MSAProbs


## MSA with [muscle](http://www.drive5.com/muscle/)

Accurate MSA tool, especially good with proteins. Suitable for medium alignments.


#### install muscle
```
$ conda install -c bioconda muscle
```

#### run muscle with fasta format of output
```
$ muscle -in  B120_test.fa  -out B120_test_out.fa
```

output
```
$ cat  B120_test_out.fa
>OTU_2
GTGTGGTGA--------------CCCCGATTAGAATAGAGAACAGTGA-TGAGAGCAGGA
AGT---GCCCCATGGCCGTGCTGTCCCAGCGCATCCTAGCCAGTTTCTGAGGCATGACTA
TGGCTTGATTCTTGACTCATTAGACTAC-------AGTGCTTCCTGGCTGATTCGAGTCT
AGTTCTTAATCCTCCCCAAATGTTTGTATCTTTTCAAAACATTCTTCTTCTGCTTAAATT
AGAGTTT-----GGTTCTGTTATTTAA----AACCCATAACCTTGTCTGGAACTTCTTAT
TCAGTAAGAAGAT--CAGCACCACCAGCGTGT
>OTU_3
GTGTGGTGAGTAGATGTGACAATGCTTGGCCAGATGACGAAACTGAGATTGAACCCAGAC
AGTCTGGCCCCAGGGCCAACCTGT--------------GACGGCTGCATAGACACAAAGC
AGGCAAGTCCCCGCATGTGACAAACGGCCAGGAGAGACGCTT--TGGGGGACTGGAG---
------GGAGCAACGC--AGTGTGTGGAAAGGGGCGATAGGGCCACCCTGGGCATCAGGA
AGGCCTCCCTGAGGAGGCGACGTTCAAGCTGAGCCCGACAGGGTG-CAGGAGC----AGT
CCTGTGAGATGGTGCCAGCAATAGATGC----
```

#### run muscle with clw format of output

```
$ muscle -in  B120_test.fa  -out B120_test_out.fa -clw

```

output
```
$ cat  B120_test_out.fa 
MUSCLE (3.8) multiple sequence alignment


OTU_2           GTGTGGTGA--------------CCCCGATTAGAATAGAGAACAGTGA-TGAGAGCAGGA
OTU_3           GTGTGGTGAGTAGATGTGACAATGCTTGGCCAGATGACGAAACTGAGATTGAACCCAGAC
                *********               *  *   ***  *   *** * ** ***   ***  

OTU_2           AGT---GCCCCATGGCCGTGCTGTCCCAGCGCATCCTAGCCAGTTTCTGAGGCATGACTA
OTU_3           AGTCTGGCCCCAGGGCCAACCTGT--------------GACGGCTGCATAGACACAAAGC
                ***   ****** ****   ****              * * * * *  ** **  *   

OTU_2           TGGCTTGATTCTTGACTCATTAGACTAC-------AGTGCTTCCTGGCTGATTCGAGTCT
OTU_3           AGGCAAGTCCCCGCATGTGACAAACGGCCAGGAGAGACGCTT--TGGGGGACTGGAG---
                 ***  *   *   *      * **  *          ****  ***  ** * ***   

OTU_2           AGTTCTTAATCCTCCCCAAATGTTTGTATCTTTTCAAAACATTCTTCTTCTGCTTAAATT
OTU_3           ------GGAGCAACGC--AGTGTGTGGAAAGGGGCGATAGGGCCACCCTGGGCATCAGGA
                        * *  * *  * *** ** *      * * *    *  * *  ** * *   

OTU_2           AGAGTTT-----GGTTCTGTTATTTAA----AACCCATAACCTTGTCTGGAACTTCTTAT
OTU_3           AGGCCTCCCTGAGGAGGCGACGTTCAAGCTGAGCCCGACAGGGTG-CAGGAGC----AGT
                **   *      **    *   ** **    * ***   *   ** * *** *      *

OTU_2           TCAGTAAGAAGAT--CAGCACCACCAGCGTGT
OTU_3           CCTGTGAGATGGTGCCAGCAATAGATGC----
                 * ** *** * *  *****  *   **   
```

#### run muscle with msf format of output

```
$ muscle -in  B120_test.fa  -out B120_test_out.fa -msf
```

output:

```
$ cat  B120_test_out.fa 
PileUp

  MSF: 332  Type: N  Check: 0000  ..

 Name: OTU_2  Len: 332  Check:  5405  Weight: 0.5
 Name: OTU_3  Len: 332  Check:  7356  Weight: 0.5

//

OTU_2    GTGTGGTGA. .......... ...CCCCGAT TAGAATAGAG AACAGTGA.T
OTU_3    GTGTGGTGAG TAGATGTGAC AATGCTTGGC CAGATGACGA AACTGAGATT

OTU_2    GAGAGCAGGA AGT...GCCC CATGGCCGTG CTGTCCCAGC GCATCCTAGC
OTU_3    GAACCCAGAC AGTCTGGCCC CAGGGCCAAC CTGT...... ........GA

OTU_2    CAGTTTCTGA GGCATGACTA TGGCTTGATT CTTGACTCAT TAGACTAC..
OTU_3    CGGCTGCATA GACACAAAGC AGGCAAGTCC CCGCATGTGA CAAACGGCCA

OTU_2    .....AGTGC TTCCTGGCTG ATTCGAGTCT AGTTCTTAAT CCTCCCCAAA
OTU_3    GGAGAGACGC TT..TGGGGG ACTGGAG... ......GGAG CAACGC..AG

OTU_2    TGTTTGTATC TTTTCAAAAC ATTCTTCTTC TGCTTAAATT AGAGTTT...
OTU_3    TGTGTGGAAA GGGGCGATAG GGCCACCCTG GGCATCAGGA AGGCCTCCCT

OTU_2    ..GGTTCTGT TATTTAA... .AACCCATAA CCTTGTCTGG AACTTCTTAT
OTU_3    GAGGAGGCGA CGTTCAAGCT GAGCCCGACA GGGTG.CAGG AGC....AGT

OTU_2    TCAGTAAGAA GAT..CAGCA CCACCAGCGT GT
OTU_3    CCTGTGAGAT GGTGCCAGCA ATAGATGC.. ..

```


### MSA with [mafft](http://align.bmr.kyushu-u.ac.jp/mafft/online/server/)

MSA tool that uses Fast Fourier Transforms. Suitable for medium-large alignments.

#### run mafft with fasta format of output
```
$ mafft  --thread 1 B120_test.fa   > B120_test_out.fa
```

output
```
$ cat B120_test_out.fa
>OTU_2
gtgtggtga--------------ccccgattagaatagagaacagtga-tgagagcagga
agt---gccccatggccgtgctgt--------------cccagcgcatcctag--ccagt
ttctgaggcatgactatggcttgattcttgactcattaga--------------------
-------ctacagtgcttcctggctgattcgagtctagttcttaatcctccccaa-----
--atgtttgtatcttttcaaaacattcttcttctgcttaaattagagtttggttctgtta
tttaaaacccataaccttgtctggaacttcttattcagtaagaagatcagcaccaccagc
gtgt--
>OTU_3
gtgtggtgagtagatgtgacaatgcttggccagatgacgaaactgagattgaacccagac
agtctggccccagggccaacctgtgacggctgcatagacacaaagcaggcaagtccccgc
atgtgacaaacggccaggagagacgctttgggggactggagggagcaacgcagtgtgtgg
aaaggggcgatagggccaccctgggcatcagga----------aggcctccctgaggagg
cgacgtt---------------caagctgagcccgacagggtgcaggagcagtcctgt--
-------------------------------------------gagatggtgccagcaat
agatgc
```

#### run mafft with clustal format of output
```
$ mafft  --thread 1 --clustalout B120_test.fa   > B120_test_out.fa
```

output

```
CLUSTAL format alignment by MAFFT FFT-NS-1 (v7.313)


OTU_2           gtgtggtga--------------ccccgattagaatagagaacagtga-tgagagcagga
OTU_3           gtgtggtgagtagatgtgacaatgcttggccagatgacgaaactgagattgaacccagac
                *********               *..*...***  * ..*** * ** ***.  ***. 

OTU_2           agt---gccccatggccgtgctgt--------------cccagcgcatcctag--ccagt
OTU_3           agtctggccccagggccaacctgtgacggctgcatagacacaaagcaggcaagtccccgc
                ***   ****** ****.  ****              * **. ***  * **  ** *.

OTU_2           ttctgaggcatgactatggcttgattcttgactcattaga--------------------
OTU_3           atgtgacaaacggccaggagagacgctttgggggactggagggagcaacgcagtgtgtgg
                 * *** . *.*.*.* *.   .  ..***.   *.*.**                    

OTU_2           -------ctacagtgcttcctggctgattcgagtctagttcttaatcctccccaa-----
OTU_3           aaaggggcgatagggccaccctgggcatcagga----------aggcctccctgaggagg
                       * *.** **. **. *   **. *..          *. ******..*     

OTU_2           --atgtttgtatcttttcaaaacattcttcttctgcttaaattagagtttggttctgtta
OTU_3           cgacgtt---------------caagctgagcccgacagggtgcaggagcagtcctgt--
                  *.***               **  **   .*.* . ...*  ..*  ..**.****  

OTU_2           tttaaaacccataaccttgtctggaacttcttattcagtaagaagatcagcaccaccagc
OTU_3           -------------------------------------------gagatggtgccagcaat
                                                           ... ..*..*** **..

OTU_2           gtgt--
OTU_3           agatgc
                . .*  

```



## MSA with [kalign](http://msa.cgb.ki.se)

Very fast MSA tool that concentrates on local regions. Suitable for large alignments.


#### install kalign
```
$ conda install -c etetoolkit kalign
```

#### run kalign
```
$ kalign -in B120_test.fa -out B120_test_out.fa  -format clu
```

the output format: fasta, msf, aln, clu, macsim

```
$ cat  B120_test_out.fa
Kalign (2.0) alignment in ClustalW format


OTU_2     GTGTGGTGACCCCGATTAGAATAGAGAACAGTGATGA--GAGCAGGAAGTGCCCCATGGC
OTU_3     GTGTGGTGAGTAGATGTGACAATGCTTGGCCAGATGACGAAACTGAGATTGAACCCAGAC


OTU_2     CGTGCTGTCCCAGCGC--ATCCTAGCCAGTTTCTGAGGCATGACTATGGCTTGATTCTTG
OTU_3     AGTCTGGCCCCAGGGCCAACCTGTGACGGCTGCATAGACACAAAGCAGGCAAGTCCCCGC


OTU_2     ACTCATTAGACTACAGTGCTTCCTGGCTGATTCGAGTCTAGTTCTTAATCCTCCCCAAAT
OTU_3     ATGTGACAAACGGCCAGGAGAGACGCTTTGGGGGACTGGAGGGAGCAACGC------AGT


OTU_2     GTTTGTATCTTTTCAAAACATTCTTCTTCTGCTTAAATTAGAGTT---TGGTTCTGTTAT
OTU_3     GTGTGGAAAGGGGCGATAGGGCCACCCTGGGCATCAGGAAGGCCTCCCTGAGGAGGCGAC


OTU_2     -TTAAAACCCATAACCTTGTCTGGAACTTCTTATTCAGTAAGAAGATCAGCACCACCAGC
OTU_3     GTTCAAGCTGAGCCCGACAGGGTGCAGGAGCAGTCCTGTGAGATGGT-GCCAGCAATAG-


OTU_2     GTGT
OTU_3     ATGC
```


## MSA with [Clustal Omega](http://www.clustal.org/omega/)

New MSA tool that uses seeded guide trees and HMM profile-profile techniques to generate alignments. Suitable for medium-large alignments.

#### install Clustal Omega
```
conda install -c biobuilds clustalomega
```

#### run clustalo
```
$ clustalo --in B120_test.fa  --seqtype DNA  --outfmt  clu  --threads 1 --out B120_test_out.fa --force
```

output
```
$ cat  B120_test_out.fa
CLUSTAL O(1.2.4) multiple sequence alignment


OTU_2      GTGTGGTGACCC-------------------CGATTAGAATAGAGAACAGTGATGAGAGC
OTU_3      GTGTGGTGAGTAGATGTGACAATGCTTGGCCAGATGACGAAACT-GAGATTGAACCCAGA
           *********                       *** *  * *    * * ***    ** 

OTU_2      AGGAAGTGCCCCATGGCCGTGCTGTCCCAGCGCATCCTAGCCAGTTTCTGAGGCATGACT
OTU_3      CAGTCTGGCCCCAGGGCCAACCTGTGACGGCT--------------GCATAGACACAAAG
             *    ****** ****   ****  * **                *  ** **  *  

OTU_2      ATGGCTTGATTCTTGACTCATTAGACTACAGTGCTTCCTGGCTGATTCGAGTCTAGTTCT
OTU_3      CAGGCAA----GTCCCCGCATGTGACAAACGGCCAGGAGAGACGCTTTGGGGGACTGGAG
             ***       *   * ***  *** *  *  *      *  * ** * *         

OTU_2      TAATCCTCCCCAAATGTTTGTATCTTTTCAAAACATTCTTCTTCTGCTTAAATTAGAGTT
OTU_3      GGAGC--AACGCAGTGTGTGGAAAGGGGCGATAGGGCCACCCTGGGCATCAGGAAGGCCT
             * *    *  * *** ** *      * * *    *  * *  ** * *   **   *

OTU_2      TG---------GTTCTGTTATTTAAAACCCATAACCTTGTCTGGAACTTCTTATTCAGTA
OTU_3      CCCTGAGGAGGCGACGTTCAAGCTGAGCCCGACAGGGTGCAGGAGCAGTCCTGTGAGATG
                         *  * *     * ***   *   **   *     ** * *    * 

OTU_2      AGAAGATCAGCACCACCAGCGTGT
OTU_3      GTG---CCAGCAATAGATGC----
                  *****  *   **    
```




## MSA with [t-coffee](http://www.tcoffee.org)

Consistency-based MSA tool that attempts to mitigate the pitfalls of progressive alignment methods. Suitable for small alignments.

#### install t-conffee
```
$ conda install -c biobuilds t-coffee 
```

#### run t-conffee
```
$ t_coffee -infile B120_test.fa -outfile B120_test_out.fa -cpu  1 -output  aln
```


output
```
CLUSTAL FORMAT for T-COFFEE 11.00.00_8cbe486 [http://www.tcoffee.org] [MODE:  ], CPU=0.00 sec, SCORE=652, Nseq=2, Len=312 

OTU_2           GTGTGGTGACCCCGATT--AGAATAG-AGAACAG-TGATGAGAGCAGGAA
OTU_3           GTGTGGTGAGT-AGATGTGACAATGCTTGGCCAGATGACGAAA-CTGAGA
                *********    ***   * ***    *  *** *** ** * * *  *

OTU_2           GTGCCCCATGGCCGTGCTGTCCCAGCGC-ATCCT-AGCCAGTTTCTGAGG
OTU_3           TTGAACCCAGACAGTCTGGCCCCAGGGCCAACCTGTGACGGCTGCATAGA
                 **  **  * * **   * ***** ** * ***  * * * * *  ** 

OTU_2           CATGACTATGGCTTGATTCTTGACTCATTAGACTACAGTGCTTCCTGGCT
OTU_3           CACAAAGCAGGCAAGTCCC----CGCATGTGACAAACGGCCAGGAGAGAC
                **  *    ***  *   *    * ***  *** *  *  *      *  

OTU_2           GATTCGA--GTCTAGTTCTTAATCCTCCCCAAATGTTTGTATCTTTTCAA
OTU_3           GCTTTGGGGGACTGGAG--GGA-GCAACGC-AGTGTGTGGAAAGGGGCGA
                * ** *   * ** *      *  *  * * * *** ** *      * *

OTU_2           AACATTCTTCTTCTGCTTAAATTAGAGTTTGGT-----TCTGTTATTTAA
OTU_3           TAGGGCCACCCTGGGCATCAGGAAGGCCTCCCTGAGGAGGCGACGTTCA-
                 *    *  * *  ** * *   **   *   *        *   ** * 

OTU_2           AACCCATAACCTTGTCTGGA---ACTTCTTATTCAGTAAGAAGATCAGCA
OTU_3           -AGCT--GAGCCCGACAGGGTGCAGGAGCAGTCCTGTGAGATGGTG-CCA
                 * *    * *  * * **    *       * * ** *** * *   **

OTU_2           CCACCAGCGTGT
OTU_3           GCAATAG-ATGC
                 **  **  ** 
```

