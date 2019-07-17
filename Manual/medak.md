
## [medaka](https://github.com/nanoporetech/medaka)

### install medaka

need **mini_align** that is in tools **pomoxis**
```
$ git clone https://github.com/nanoporetech/medaka.git
$ cp /home/wuzhikun/anaconda3/envs/NanoSV/share/pomoxis/scripts/mini_align mini_assemble /home/wuzhikun/anaconda3/envs/NanoSV/share/medaka/scripts
$ cd medaka
$ python setup.py install
```


### medaka parameters
```
$ medaka -h
usage: medaka [-h] [--version]
              {features,train,consensus,consensus_from_features,stitch,variant,tools}
              ...

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit

subcommands:
  valid commands

  {features,train,consensus,consensus_from_features,stitch,variant,tools}
                        additional help
    features            Create features for inference.
    train               Train a model from features.
    consensus           Run inference from a trained model and alignments.
    consensus_from_features
                        Run inference from a trained model on existing
                        features.
    stitch              Stitch together output from medaka consensus into
                        final output.
    variant             Decode probabilities to VCF.
    tools               tools sub-command.

```




