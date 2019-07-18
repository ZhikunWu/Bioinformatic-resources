
## [peregrine docker](https://hub.docker.com/r/cschin/peregrine/dockerfile)


### install peregrine

```
$ docker pull cschin/peregrine
```


```
$ docker  run -it -v /wd:/wd  cschin/peregrine pg_run.py  asm --help
Peregrine Assembler & SHIMMER ASMKit(0+unknown)
pypeflow 2.1.1+git.d63b0e79f5a7b2d370b7de84a890f88271afa476

Peregrine
=========

Peregrine is a fast genome assembler for accurate long
reads (length > 10kb, accuraccy > 99%). It can assemble
a human genome from 30x reads within 20 cpu hours from
reads to polished consensus. It uses Sparse HIereachical
MimiMizER (SHIMMER) for fast read-to-read overlaps without
explicitly quadratic comparisions used in other OLC
assemblers.

Peregrine Assembler and SHIMMER Genome Assembly Toolkit
Copyright (c) 2019- by Jason, Chen-Shan, Chin

Peregrine Assembler and  SHIMMER Genome Assembly Toolkit
is licensed under a Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License.

You should have received a copy of the license along with
this work. If not, see
<http://creativecommons.org/licenses/by-nc-sa/4.0/>.

************************************************************
If you want to use it for any commericial purposes
(including promotion activity for a commerical product),
please contact Jason Chin for a commericial license.
************************************************************

run `pg_run.py -h` for help and other license information


using pypeflow 2.1.1+git.d63b0e79f5a7b2d370b7de84a890f88271afa476

This is a pre-release, please do not re-distribute without permission.

I agree that I am not using this software for any commericial purposes (yes/no): yes
Peregrine
===============================================================
Peregrine is a fast genome assembler for accurate long
reads (length > 10kb, accuraccy > 99%). It can assemble
a human genome from 30x reads within 20 cpu hours from
reads to polished consensus. It uses Sparse HIereachical
MimiMizER (SHIMMER) for fast read-to-read overlaps without
explicitly quadratic comparisions used in other OLC
assemblers.

Currently, the assembly graph process is more or less
identical to the approaches used in the FALCON assembler
developed by Jason Chin and others in Pacific Biosciences, Inc.

Usage:
  pg_run.py asm <reads.lst> <index_nchunk> <index_nproc>
                            <ovlp_nchunk> <ovlp_nproc>
                            <mapping_nchunk> <mapping_nproc>
                            <cns_nchunk> <cns_nproc>
                            <sort_nproc>
                            [--with-consensus]
                            [--with-L0-index]
                            [--output <output>]
                            [--shimmer-k <shimmer_k>]
                            [--shimmer-w <shimmer_w>]
                            [--shimmer-r <shimmer_r>]
                            [--shimmer-l <shimmer_l>]
                            [--best_n_ovlp <n_ovlp>]
                            [--mc_lower <mc_lower>]
                            [--mc_upper <mc_upper>]
                            [--aln_bw <aln_bw>]
                            [--ovlp_upper <ovlp_upper>]
  pg_run.py (-h | --help)
  pg_run.py --verison

Options:
  -h --help                   Show this help
  --version                   Show version
  --with-consensus            Generate consensus after getting the draft contigs
  --with-L0-index             Keep level-0 index
  --output <output>           Set output directory (will be created if not exist) [default: ./wd]
  --shimmer-k <shimmer_k>     Level 0 k-mer size [default: 16]
  --shimmer-w <shimmer_w>     Level 0 window size [default: 80]
  --shimmer-r <shimmer_r>     Reduction factore for high level SHIMMER [default: 6]
  --shimmer-l <shimmer_l>     number of level of shimmer used, the value should be 1 or 2 [default: 2]
  --best_n_ovlp <n_ovlp>      Find best n_ovlp overlap [default: 4]
  --mc_lower <mc_lower>       Does not cosider SHIMMER with count less than mc_low [default: 2]
  --mc_upper <mc_upper>       Does not cosider SHIMMER with count greater than mc_upper [default: 240]
  --aln_bw <aln_bw>           Max off-diagonal gap allow during overlap confirmation [default: 100]
  --ovlp_upper <ovlp_upper>   Ignore cluster with overlap count greater ovlp_upper [default: 120]

Licenses:

Peregrine Assembler and SHIMMER Genome Assembly Toolkit
Copyright (c) 2019- by Jason, Chen-Shan, Chin

Peregrine Assembler and  SHIMMER Genome Assembly Toolkit
is licensed under a Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License.

You should have received a copy of the license along with
this work. If not, see
<http://creativecommons.org/licenses/by-nc-sa/4.0/>.

************************************************************
If you want to use it for any commericial purposes
(including promotion activity for a commerical product),
please contact Jason Chin for a commericial license.
************************************************************

This software uses the following libraray from Heng Li's
Minimap2 codebase under MIT License:

mm_sketch.c kvec.h kseq.h khash.h kalloc.h kalloc.c

The MIT License

Copyright (c) 2018-     Dana-Farber Cancer Institute
2017-2018 Broad Institute, Inc.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


License for code from FALCON

#################################################################################$$
# Copyright (c) 2011-2015, Pacific Biosciences of California, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted (subject to the limitations in the
# disclaimer below) provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright
#  notice, this list of conditions and the following disclaimer.
#
#  * Redistributions in binary form must reproduce the above
#  copyright notice, this list of conditions and the following
#  disclaimer in the documentation and/or other materials provided
#  with the distribution.
#
#  * Neither the name of Pacific Biosciences nor the names of its
#  contributors may be used to endorse or promote products derived
#  from this software without specific prior written permission.
#
# NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE
# GRANTED BY THIS LICENSE. THIS SOFTWARE IS PROVIDED BY PACIFIC
# BIOSCIENCES AND ITS CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL PACIFIC BIOSCIENCES OR ITS
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF
# USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#################################################################################$$

```


### install based on source code
```
$ cat install_with_conda.sh

#!/bin/bash
. ~/anaconda3/bin/activate
conda create -n peregrine -y python=3.7

conda activate peregrine
conda install -c conda-forge -y pypy3.6

pushd py
rm -rf .eggs/ dist/ build/ peregrine.egg-info/ peregrine_pypy.egg-info get-pip.py
python3 setup.py install
python3 setup.py clean --all
popd
git clone -b peregrine https://github.com/cschin/pypeFLOW.git
pushd pypeFLOW
python3 setup.py install
popd
pushd py
wget -q https://bootstrap.pypa.io/get-pip.py
pypy3 get-pip.py
pypy3 setup_pypy.py install
popd

pushd src
make all
make install
popd

#python3 -m pip install cffi==1.12.2
```




```
$ make all
gcc -O3  -Wall -Wno-unused-result -Wno-unused-function -Werror    shmr_mkseqdb.c kalloc.o shmr_utils.o  -lz -o shmr_mkseqdb
gcc -O3  -Wall -Wno-unused-result -Wno-unused-function -Werror   -c -o shmr_reduce.o shmr_reduce.c
gcc -O3  -Wall -Wno-unused-result -Wno-unused-function -Werror   -c -o mm_sketch.o mm_sketch.c
gcc -O3  -Wall -Wno-unused-result -Wno-unused-function -Werror   -c -o shmr_end_filter.o shmr_end_filter.c
gcc -O3  -Wall -Wno-unused-result -Wno-unused-function -Werror    shmr_index.c kalloc.o shmr_reduce.o mm_sketch.o shmr_utils.o shmr_end_filter.o  -lz -o shmr_index
shmr_index.c: In function ‘main’:
shmr_index.c:216:2: error: ‘for’ loop initial declarations are only allowed in C99 mode
  for (size_t _i=0; _i < seq_data.n; _i++) {
  ^
shmr_index.c:216:2: note: use option -std=c99 or -std=gnu99 to compile your code
make: *** [shmr_index] Error 1

```


#### [How do I fix “for loop initial declaration used outside C99 mode” GCC error?](https://stackoverflow.com/questions/24881/how-do-i-fix-for-loop-initial-declaration-used-outside-c99-mode-gcc-error)


try to declare **i** outside of the loop!


```
for(int i = low; i <= high; ++i)
        {
                res = runalg(i);
                if (res > highestres)
                {
                        highestres = res;
                }

        }
```

to 

```
#include <stdio.h>

int main() {

   int i;

   /* for loop execution */
   for (i = 10; i < 20; i++) {
       printf("i: %d\n", i);
   }   

   return 0;
}
```




For anyone attempting to compile code from an external source that uses an automated build utility such as Make, to avoid having to track down the explicit gcc compilation calls you can set an environment variable. Enter on command prompt or put in .bashrc (or .bash_profile on Mac):
```
export CFLAGS="-std=c99"
```

or

add **CFLAGS="-std=gnu99"** in the makefile


#### [Human genome assembly parameters](https://github.com/cschin/Peregrine/issues/11)

```
The assembler is designed for accurate long reads (~10kb length < 1% error). Do you have such reads from Nanopore. If so, it should work. If not, maybe we need to wait a bit for Nanopore comes up a protocol to generate such data.
```


### run peregrine
```
python /home/wuzhikun/anaconda3/envs/NanoSV/bin/Peregrine/py/scripts/pg_run.py asm /home/wuzhikun/Project/NanoTrio/peregrine/M628-0_list.txt 24 24 24 24 24 24 24 24 24 --with-consensus --shimmer-r 3 --best_n_ovlp 8 --output /home/wuzhikun/Project/NanoTrio/peregrine/M628-0_asm
```

```
I agree that I am not using this software for any commericial purposes (yes/no): yes
Peregrine Assembler (0.1.5.3+0.gd1eeebc.dirty) has been started with the following option:
 {'--aln_bw': '100',
 '--best_n_ovlp': '8',
 '--help': False,
 '--mc_lower': '2',
 '--mc_upper': '240',
 '--output': '/home/wuzhikun/Project/NanoTrio/peregrine/M628-0_asm',
 '--ovlp_upper': '120',
 '--shimmer-k': '16',
 '--shimmer-l': '2',
 '--shimmer-r': '3',
 '--shimmer-w': '80',
 '--verison': False,
 '--with-L0-index': False,
 '--with-consensus': True,
 '<cns_nchunk>': '24',
 '<cns_nproc>': '24',
 '<index_nchunk>': '24',
 '<index_nproc>': '24',
 '<mapping_nchunk>': '24',
 '<mapping_nproc>': '24',
 '<ovlp_nchunk>': '24',
 '<ovlp_nproc>': '24',
 '<reads.lst>': '/home/wuzhikun/Project/NanoTrio/peregrine/M628-0_list.txt',
 '<sort_nproc>': '24',
 'asm': True}
INFO:pypeflow.simple_pwatcher_bridge:In simple_pwatcher_bridge, pwatcher_impl=<module 'pwatcher.blocking' from '/home/wuzhikun/anaconda3/lib/python3.7/site-packages/pypeflow-2.1.1+git.d63b0e79f5a7b2d370b7de84a890f88271afa476-py3.7.egg/pwatcher/blocking.py'>
INFO:pypeflow.simple_pwatcher_bridge:job_type='local', (default)job_defaults={'njobs': 1, 'NPROC': 1, 'MB': 24000, 'submit': 'bash -C ${CMD} >| ${STDOUT_FILE} 2>| ${STDERR_FILE}', 'job_type': 'local', 'pwatcher_type': 'blocking'}, use_tmpdir=None, squash=False, job_name_style=0
INFO:pypeflow.simple_pwatcher_bridge:Setting max_jobs to 1; was None
INFO:pypeflow.simple_pwatcher_bridge:Num unsatisfied: 1, graph: 1
INFO:pypeflow.simple_pwatcher_bridge:About to submit: Node(../../../../../../../Project/NanoTrio/peregrine/M628-0_asm/0-seqdb)
INFO:pwatcher.blocking:Popen: '/bin/bash -C /home/wuzhikun/anaconda3/lib/python3.7/site-packages/pypeflow-2.1.1+git.d63b0e79f5a7b2d370b7de84a890f88271afa476-py3.7.egg/pwatcher/mains/job_start.sh >| /home/wuzhikun/Project/NanoTrio/peregrine/M628-0_asm/0-seqdb/run-Pdf8f0614cec1fb.bash.stdout 2>| /home/wuzhikun/Project/NanoTrio/peregrine/M628-0_asm/0-seqdb/run-Pdf8f0614cec1fb.bash.stderr'
INFO:pypeflow.simple_pwatcher_bridge:(slept for another 0.0s -- another 1 loop iterations)
INFO:pypeflow.simple_pwatcher_bridge:(slept for another 0.30000000000000004s -- another 2 loop iterations)
INFO:pypeflow.simple_pwatcher_bridge:(slept for another 1.2000000000000002s -- another 3 loop iterations)
INFO:pypeflow.simple_pwatcher_bridge:(slept for another 2.9999999999999996s -- another 4 loop iterations)
INFO:pypeflow.simple_pwatcher_bridge:(slept for another 6.0s -- another 5 loop iterations)
INFO:pypeflow.simple_pwatcher_bridge:(slept for another 10.500000000000002s -- another 6 loop iterations)
INFO:pypeflow.simple_pwatcher_bridge:(slept for another 16.800000000000004s -- another 7 loop iterations)

 
ERROR:pypeflow.simple_pwatcher_bridge:Task Node(../../../../../../../Project/NanoTrio/peregrine/M628-0_asm/3-asm) failed with exit-code=1
ERROR:pypeflow.simple_pwatcher_bridge:Some tasks are recently_done but not satisfied: {Node(../../../../../../../Project/NanoTrio/peregrine/M628-0_asm/3-asm)}
ERROR:pypeflow.simple_pwatcher_bridge:ready: set()
  submitted: set()
ERROR:pwatcher.blocking:Noop. We cannot kill blocked threads. Hopefully, everything will die on SIGTERM.
Traceback (most recent call last):
  File "/home/wuzhikun/anaconda3/envs/NanoSV/bin/Peregrine/py/scripts/pg_run.py", line 651, in <module>
    main(args)
  File "/home/wuzhikun/anaconda3/envs/NanoSV/bin/Peregrine/py/scripts/pg_run.py", line 586, in main
    ovlp_out)
  File "/home/wuzhikun/anaconda3/envs/NanoSV/bin/Peregrine/py/scripts/pg_run.py", line 370, in run_ovlp_to_ctg
    wf.refreshTargets()
  File "/home/wuzhikun/anaconda3/lib/python3.7/site-packages/pypeflow-2.1.1+git.d63b0e79f5a7b2d370b7de84a890f88271afa476-py3.7.egg/pypeflow/simple_pwatcher_bridge.py", line 278, in refreshTargets
    self._refreshTargets(updateFreq, exitOnFailure)
  File "/home/wuzhikun/anaconda3/lib/python3.7/site-packages/pypeflow-2.1.1+git.d63b0e79f5a7b2d370b7de84a890f88271afa476-py3.7.egg/pypeflow/simple_pwatcher_bridge.py", line 362, in _refreshTargets
    raise Exception(msg)
Exception: Some tasks are recently_done but not satisfied: {Node(../../../../../../../Project/NanoTrio/peregrine/M628-0_asm/3-asm)}


```