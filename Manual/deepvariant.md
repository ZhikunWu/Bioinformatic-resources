

## [DeepVariant quick start](https://github.com/google/deepvariant/blob/r0.8/docs/deepvariant-quick-start.md)
```
sudo docker run \
  -v "${INPUT_DIR}":"/input" \
  -v "${OUTPUT_DIR}:/output" \
  gcr.io/deepvariant-docker/deepvariant:"${BIN_VERSION}" \
  /opt/deepvariant/bin/run_deepvariant \
  --model_type=WGS \ **Replace this string with exactly one of the following [WGS,WES,PACBIO]**
  --ref=/input/ucsc.hg19.chr20.unittest.fasta \
  --reads=/input/NA12878_S1.chr20.10_10p1mb.bam \
  --regions "chr20:10,000,000-10,010,000" \
  --output_vcf=/output/output.vcf.gz \
  --output_gvcf=/output/output.g.vcf.gz \
  --num_shards=1 **How many cores the `make_examples` step uses. Change it to the number of CPU cores you have.**
```


## docker file

### [dajunluo/deepvariant](https://hub.docker.com/r/dajunluo/deepvariant/)
```
docker pull dajunluo/deepvariant
```

run demo

```
$ export OUTPUT_DIR=/path/to/output/folder/
$ docker run -v "${OUTPUT_DIR}":/opt/deepvariant/output dajunluo/deepvariant python run_deepvariant.py \
--model_type=WGS \
--ref=../../quickstart-testdata/ucsc.hg19.chr20.unittest.fasta \
--reads=../../quickstart-testdata/NA12878_S1.chr20.10_10p1mb.bam \
--regions "chr20:10,000,000-10,010,000" \
--output_vcf=../output/output.vcf.gz \
--output_gvcf=../output/output.g.vcf.gz
$ ls $OUTPUT_DIR
```


Start the container

```
$ export DATA_DIR='abosulute/path/to/your/bam/and/fasta'
$ OUTPUT_DIR=/path/to/output/folder/
$ docker run -td --name deepvariant -v "${DATA_DIR}":/opt/data -v "${OUTPUT_DIR}":/opt/deepvariant/output dajunluo/deepvariant
```


Enter the image
```
$ docker exec -it deepvariant /bin/bash
```

Inside the docker image
```
$python run_deepvariant.py --model_type=WGS \
--ref=../../data/"${REFERENCE_FILE}" \
--reads=../../data/"${BAM_FILE}" \
--regions "chr20:10,000,000-10,010,000" \
--output_vcf=../output/output.vcf.gz \
--output_gvcf=../output/output.g.vcf.gz
```