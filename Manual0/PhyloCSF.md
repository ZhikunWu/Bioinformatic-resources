## PhyloCSF

### install ocaml
```
$su root
Password: 
root@Dell-03:/home/wzk# apt-get install ocaml
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  camlp4 ledit libcamlp4-ocaml-dev libfindlib-ocaml libfindlib-ocaml-dev ocaml-base ocaml-base-nox
  ocaml-compiler-libs ocaml-findlib ocaml-interp ocaml-nox
Suggested packages:
  ocaml-doc tuareg-mode | ocaml-mode
The following NEW packages will be installed:
  camlp4 ledit libcamlp4-ocaml-dev libfindlib-ocaml libfindlib-ocaml-dev ocaml ocaml-base ocaml-base-nox
  ocaml-compiler-libs ocaml-findlib ocaml-interp ocaml-nox
0 upgraded, 12 newly installed, 0 to remove and 122 not upgraded.
Need to get 32.7 MB of archives.
After this operation, 220 MB of additional disk space will be used.
Do you want to continue? [Y/n]


add-apt-repository --yes ppa:avsm/ppa
apt-get update -qq
apt-get install -y opam
opam init
eval $(opam config env)
opam update
opam install batteries ocaml-twt gsl

```

or install using **conda**:
```
$ conda install -c conda-forge ocaml
```


### OPAM
```

1. To configure OPAM in the current shell session, you need to run:

      eval `opam config env`

2. To correctly configure OPAM for subsequent use, add the following
   line to your profile file (for instance ~/.profile):

      . /home/wzk/.opam/opam-init/init.sh > /dev/null 2> /dev/null || true

3. To avoid issues related to non-system installations of `ocamlfind`
   add the following lines to ~/.ocamlinit (create it if necessary):

      let () =
        try Topdirs.dir_directory (Sys.getenv "OCAML_TOPLEVEL_PATH")
        with Not_found -> ()
      ;;

```

### install gsl
```
opam install gsl

=-=- conf-gsl.1 troobleshooting -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

=> This package relies on external (system) dependencies that may be missing. `opam depext conf-gsl.1' may help you find t
   installation for your system.

```
### install the depedensy of gsl
```
opam depext conf-gsl.1
```



### install PhyloCSF
```
git clone https://github.com/mlin/PhyloCSF.git

```


### PhyloCSF parameters
[PhyloCSF wiki](https://github.com/mlin/PhyloCSF/wiki)

### run PhyloCSF
```
./PhyloCSF.Linux.x86_64 PhyloCSF_Parameters/29mammals PhyloCSF_Examples/ALDH2.exon5.fa --frames=6


./PhyloCSF 29mammals PhyloCSF_Examples/Aldh2.mRNA.fa --orf=ATGStop --frames=3 --removeRefGaps --aa


```

### PhyloCSF parameters
```
wzk@server2:/home/soft/PhyloCSF$ ./PhyloCSF
usage: PhyloCSF.Linux.x86_64 parameter_set [file1 file2 ...]
input will be read from stdin if no filenames are given.

options:

  -h, --help            show this help message and exit
  --strategy=mle|fixed|omega
                        evaluation strategy (default mle)

  input interpretation:

    --files             input list(s) of alignment filenames instead of
                        individual alignment(s)
    --removeRefGaps     automatically remove any alignment columns that are
                        gapped in the reference sequence (nucleotide columns
                        are removed individually; be careful about reading
                        frame). By default, it is an error for the reference
                        sequence to contain gaps
    --species=Species1,Species2,...
                        hint that only this subset of species will be used in
                        any of the alignments; this does not change the
                        calculation mathematically, but can speed it up

  searching mulitple reading frames and ORFs:

    -f1|3|6, --frames=1|3|6
                        how many reading frames to search (default 1)
    --orf=AsIs|ATGStop|StopStop|StopStop3|ToFirstStop|FromLastStop|ToOrFromStop
                        search for ORFs (default AsIs)
    --minCodons=INT     minimum ORF length for searching over ORFs (default 25
                        codons)
    --allScores         report scores of all regions evaluated, not just the
                        max
    -pINT               search frames/ORFs using up to p parallel subprocesses

  output control:

    --bls               include alignment branch length score (BLS) for the
                        reported region in output
    --ancComp           include ancestral sequence composition score in output
    --dna               include DNA sequence in output, the part of the
                        reference (first) sequence whose score is reported
    --aa                include amino acid translation in output
    --debug             print extra information about parameters and errors

```
