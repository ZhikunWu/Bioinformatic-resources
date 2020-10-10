
## [quast](https://github.com/ablab/quast)


### quast parameter

```
quast --no-html --no-snps -o /home/wuzhikun/Project/PanGenome/Quast/CN353_noalt -r /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa -g /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.95.gff3 -t 60 /home/wuzhikun/Project/PanGenome/Assembly/CN353_assembly_polish.fasta > /home/wuzhikun/Project/PanGenome/log/Quast_CN353.log 2>&1

```


The output file

```

$ tree /home/wuzhikun/Project/PanGenome/Quast/
/home/wuzhikun/Project/PanGenome/Quast/
└── CN353_noalt
    ├── aligned_stats
    │   ├── cumulative_plot.pdf
    │   ├── NAx_plot.pdf
    │   └── NGAx_plot.pdf
    ├── basic_stats
    │   ├── CN353_assembly_polish_GC_content_plot.pdf
    │   ├── cumulative_plot.pdf
    │   ├── GC_content_plot.pdf
    │   ├── gc.icarus.txt
    │   ├── NGx_plot.pdf
    │   └── Nx_plot.pdf
    ├── contigs_reports
    │   ├── all_alignments_CN353_assembly_polish.tsv
    │   ├── CN353_assembly_polish.mis_contigs.fa
    │   ├── contigs_report_CN353_assembly_polish.mis_contigs.info
    │   ├── contigs_report_CN353_assembly_polish.stderr
    │   ├── contigs_report_CN353_assembly_polish.stdout
    │   ├── contigs_report_CN353_assembly_polish.unaligned.info
    │   ├── minimap_output
    │   │   ├── CN353_assembly_polish.coords
    │   │   ├── CN353_assembly_polish.coords.filtered
    │   │   ├── CN353_assembly_polish.coords_tmp
    │   │   ├── CN353_assembly_polish.sf
    │   │   ├── CN353_assembly_polish.unaligned
    │   │   └── CN353_assembly_polish.used_snps.gz
    │   ├── misassemblies_frcurve_plot.pdf
    │   ├── misassemblies_plot.pdf
    │   ├── misassemblies_report.tex
    │   ├── misassemblies_report.tsv
    │   ├── misassemblies_report.txt
    │   ├── transposed_report_misassemblies.tex
    │   ├── transposed_report_misassemblies.tsv
    │   ├── transposed_report_misassemblies.txt
    │   ├── unaligned_report.tex
    │   ├── unaligned_report.tsv
    │   └── unaligned_report.txt
    ├── genome_stats
    │   ├── CN353_assembly_polish_gaps.txt
    │   ├── CN353_assembly_polish_genomic_features_any.txt
    │   ├── features_cumulative_plot.pdf
    │   ├── features_frcurve_plot.pdf
    │   └── genome_info.txt
    ├── quast.log
    ├── report.pdf
    ├── report.tex
    ├── report.tsv
    ├── report.txt
    ├── transposed_report.tex
    ├── transposed_report.tsv
    └── transposed_report.txt

6 directories, 45 files

```

