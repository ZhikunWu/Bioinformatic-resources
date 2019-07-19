
## [Pychopper](https://github.com/nanoporetech/pychopper)

### install pychopper
```
$ cdna_classifier.py --help
Traceback (most recent call last):
  File "/home/wuzhikun/anaconda3/envs/NanoSV/bin/cdna_classifier.py", line 4, in <module>
    __import__('pkg_resources').run_script('pychopper==0.6.1', 'cdna_classifier.py')
  File "/home/wuzhikun/anaconda3/envs/NanoSV/lib/python3.6/site-packages/pkg_resources/__init__.py", line 664, in run_script
    self.require(requires)[0].run_script(script_name, ns)
  File "/home/wuzhikun/anaconda3/envs/NanoSV/lib/python3.6/site-packages/pkg_resources/__init__.py", line 1444, in run_script
    exec(code, namespace, namespace)
  File "/home/wuzhikun/anaconda3/envs/NanoSV/lib/python3.6/site-packages/pychopper-0.6.1-py3.6.egg/EGG-INFO/scripts/cdna_classifier.py", line 9, in <module>
    from pychopper import chopper
  File "/home/wuzhikun/anaconda3/envs/NanoSV/lib/python3.6/site-packages/pychopper-0.6.1-py3.6.egg/pychopper/chopper.py", line 6, in <module>
    from pychopper import seq_detect
  File "/home/wuzhikun/anaconda3/envs/NanoSV/lib/python3.6/site-packages/pychopper-0.6.1-py3.6.egg/pychopper/seq_detect.py", line 5, in <module>
    import parasail
  File "/home/wuzhikun/anaconda3/envs/NanoSV/lib/python3.6/site-packages/parasail-1.1.17-py3.6.egg/parasail/__init__.py", line 30, in <module>
    _lib = ctypes.CDLL(_libname)
  File "/home/wuzhikun/anaconda3/envs/NanoSV/lib/python3.6/ctypes/__init__.py", line 348, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: libparasail.so: cannot open shared object file: No such file or directory

```

#### install library parasail
```
$ conda install -c bioconda parasail-python
```


### parameter of Pychopper
```
$ cdna_classifier.py --help
usage: cdna_classifier.py [-h] -b primers [-i input_format] [-g aln_params]
                          [-t target_length] [-s score_percentile]
                          [-n sample_size] [-r report_pdf] [-u unclass_output]
                          [-S stats_output] [-A scores_output] [-x]
                          [-l heu_stringency]
                          input_fastx output_fastx

Tool to identify full length cDNA reads. Primers have to be specified as they
are on the forward strand.

positional arguments:
  input_fastx          Input file.
  output_fastx         Output file.

optional arguments:
  -h, --help           show this help message and exit
  -b primers           Primers fasta.
  -i input_format      Input/output format (fastq).
  -g aln_params        Alignment parameters (match,
                       mismatch,gap_open,gap_extend).
  -t target_length     Number of bases to scan at each end (200).
  -s score_percentile  Score cutoff percentile (98).
  -n sample_size       Number of samples when calculating score cutoff
                       (100000).
  -r report_pdf        Report PDF.
  -u unclass_output    Write unclassified reads to this file.
  -S stats_output      Write statistics to this file.
  -A scores_output     Write alignment scores to this file.
  -x                   Use more sensitive (and error prone) heuristic mode
                       (False).
  -l heu_stringency    Stringency in heuristic mode (0.25).

```


