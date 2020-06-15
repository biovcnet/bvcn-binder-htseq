# Binder for BVCN Transcriptomics lesson 3

Initially forked from [here](https://github.com/binder-examples/conda). Thank you to the awesome [binder](https://mybinder.org/) team!

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/binder/v2/gh/biovcnet/bvcn-binder-htseq/master?urlpath=lab)

Part of the [Bioinformatics Virtual Coordination Network](https://biovcnet.github.io/) :)


## Walkthrough

Build bowtie2 index out of the Tremblaya genome

    bowtie2-build -f Candidatus-Tremblaya-princeps_PCIT.fa Candidatus-Tremblaya-princeps_PCIT.fa

Map sample reads to the index using bowtie2

    bowtie2 -x Candidatus-Tremblaya-princeps_PCIT.fa -U PCIT.sample.fastq -S Candidatus-Tremblaya-princeps_PCIT.sam --no-unal

Generate GFF file using Prokka

    prokka Candidatus-Tremblaya-princeps_PCIT.fa

Extract CDS rows from the GFF file

    grep -P '\tCDS' PROKKA_05192020.gff > cds_PROKKA_05192020.gff

Examine the feature type and GFF attribute to be used as feature ID.

Generate GFF file using Prodigal

    prodigal -f gff -o Candidatus-Tremblaya-princeps_PCIT.prodigal.gff -i Candidatus-Tremblaya-princeps_PCIT.fa -a Candidatus-Tremblaya-princeps_PCIT.fa-proteins.faa -d Candidatus-Tremblaya-princeps_PCIT.fa-proteins.ffn -p meta

Run htseq-count

    htseq-count Candidatus-Tremblaya-princeps_PCIT.sam PROKKA_05192020/cds_PROKKA_05192020.gff -t CDS -i ID -c Candidatus-Tremblaya-princeps_PCIT.reverse.counts --nonunique none

Run htseq-count, only counting the reads mapping to the reverse strand

    htseq-count Candidatus-Tremblaya-princeps_PCIT.sam PROKKA_05192020/cds_PROKKA_05192020.gff -t CDS -i ID -c Candidatus-Tremblaya-princeps_PCIT.reverse.counts --nonunique none -s reverse

Inspect and compare the ouputs

run counts-to-tpm script to convert read counts to normalized value: transcripts per million (TPM)




