
## [SURVIVOR](https://github.com/fritzsedlazeck/SURVIVOR)

### [SURVIVOR manual](https://github.com/fritzsedlazeck/SURVIVOR/wiki)
### install SURVIVOR
```
$ conda install -c bioconda survivor 
```

### SURVIVOR parameters
```
$ SURVIVOR
Program: SURVIVOR (Tools for Structural Variations in the VCF format)
Version: 1.0.5

Usage: SURVIVOR <command> [options]

Commands:
-- Simulation/ Evaluation
    simSV   Simulates SVs and SNPs on a reference genome.
    scanreads   Obtain error profiles form mapped reads for simulation.
    simreads    Simulates long reads (Pacio or ONT).
    eval    Evaluates a VCF file after SV calling over simulated data.

-- Comparison/filtering
    merge   Compare or merge VCF files to generate a consensus or multi sample VCF files.
    genComp Generates a pairwise comparison matrix based on any multi sample VCF file
    filter  Filter a vcf file based on size and/or regions to ignore
    stats   Report multipe stats over a VCF file
    compMUMMer  Annotates a VCF file with the breakpoints found with MUMMer (Show-diff).

-- Conversion
    bincov  Bins coverage vector to a bed file to filter SVs in low MQ regions
    vcftobed    Converts a VCF file to a bed file
    bedtovcf    Converts a bed file to a VCF file 
    smaptovcf   Converts the smap file to a VCF file (beta version)
    bedpetovcf  Converts a bedpe file ot a VCF file (beta version)
    hapcuttovcf Converts the Hapcut2 final file to a VCF file using the original SNP file provided to Hapcut2
    convertAssemblytics Converts Assemblytics to a VCF file

```
