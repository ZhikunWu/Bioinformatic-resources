
## igv_plotter

```
$ igv_plotter -g /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa --igv-jar-path /home/wuzhikun/anaconda3/envs/NanoSV/bin/igv.jar --locus-file ../../IGV_test/target_region.bed -o ../../IGV_test/target_region_igv  M625-0_test.bam
```


```
$ cat ../../IGV_test/target_region.txt
2:95930297-95932496
14:18900837-18903124

```

```
$ igv_plotter -g /home/wuzhikun/database/genome/GRCh38/Homo_sapiens.GRCh38.dna.primary_assembly.fa --igv-jar-path /home/wuzhikun/anaconda3/envs/NanoSV/bin/igv.jar --locus-file ../../IGV_test/target_region.txt -o ../../IGV_test/target_region_igv  M625-0_test.bam
Traceback (most recent call last):
  File "/home/wuzhikun/anaconda3/envs/NanoSV/bin/igv_plotter", line 140, in <module>
    igv_robot.execute()
  File "/home/wuzhikun/anaconda3/envs/NanoSV/lib/python3.6/site-packages/igv_api.py", line 256, in execute
    self._execute_impl(self.__command_queue)
  File "/home/wuzhikun/anaconda3/envs/NanoSV/lib/python3.6/site-packages/igv_api.py", line 386, in _execute_impl
    width=self.igv_window_width, height=self.igv_window_height, colordepth=24)
  File "/home/wuzhikun/anaconda3/envs/NanoSV/lib/python3.6/site-packages/xvfbwrapper.py", line 41, in __init__
    raise EnvironmentError(msg)
OSError: Can not find Xvfb. Please install it and try again.

```


### install xvfb

```
cd /home/wuzhikun/anaconda3/envs/NanoSV/share && git clone https://github.com/revnode/xvfb-run.git && ln -s /home/wuzhikun/anaconda3/envs/NanoSV/share/xvfb-run/xvfb-run /home/wuzhikun/anaconda3/envs/NanoSV/bin/xvfb-run
```

or

```
conda install -c anaconda xorg-x11-server-xvfb-cos6-x86_64
```


