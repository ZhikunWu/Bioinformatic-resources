
## [SecretSanta](https://gogleva.github.io/SecretSanta/vignettes/SecretSanta-vignette.html): flexible pipelines for functional secretome prediction
## [Tatp](http://www.cbs.dtu.dk/services/TatP/): predicts the presence and location of Twin-arginine signal peptide cleavage sites in bacteria.
## [TMHMM](http://www.cbs.dtu.dk/services/TMHMM/): Prediction of transmembrane helices in proteins
## [Phobius](http://phobius.sbc.su.se): A combined transmembrane topology and signal peptide predictor
## [PECAS](https://link.springer.com/article/10.1007%2Fs00726-015-2058-2): prokaryotic and eukaryotic classical analysis of secretome
## [PECAS Prokaryotic](http://genomics.cicbiogune.es/PECAS/ProkaryoticData.php)
## [bioruby-signalp](https://github.com/wwood/bioruby-signalp): A wrapper for the signal peptide prediction algorithm SignalP


## [SignaIP](http://www.cbs.dtu.dk/services/SignalP/): predicts the presence and location of signal peptide cleavage sites in amino acid sequences from different organisms
```
I didn't see this in the installation instructions anywhere, but if you edit the signalp executable in that package, you'll see some settings that need to be customized. On line 14, you need to edit the default path to point to your signalp directory location by editing the line

$ENV{SIGNAL} = '/path/to/signalp/directory';

ln -s  /home/wzk/anaconda3/envs/qiime/bin/signalp-4.1/signalp  /home/wzk/anaconda3/envs/qiime/bin/signalp
```

### run signalp
```
$ signalp -t euk -f short MetaContig_test.faa >  MetaContig_signal.faa
```



