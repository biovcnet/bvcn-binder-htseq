# Binder for BVCN Comparative Genomics lesson

Initially forked from [here](https://github.com/binder-examples/conda). Thank you to the awesome [binder](https://mybinder.org/) team!

[![Binder](https://mybinder.org/badge_logo.svg)](https://gesis.mybinder.org/binder/v2/gh/Arkadiy-Garber/bvcn-binder-prokka-htseq/master?urlpath=lab)

Part of the [Bioinformatics Virtual Coordination Network](https://biovcnet.github.io/) :)


## Walkthrough (interspecies example with two homologous sequences)

Enter the first direcotry

    cd interspecies_example//

Align the FASTA amino acid file

    muscle -in MNBX01000583.1_4.faa -out MNBX01000583.1_4.fa

Make a codon alignment from the peptide alignment and nucleotide sequence

    pal2nal.pl MNBX01000583.1_4.fa MNBX01000583.1_4.ffn -output fasta > MNBX01000583.1_4.codonalign.fa

Check that the correct input/output files are in the codeml.ctl file

    less codeml.ctl

Run codeml

    codeml codeml.ctl

## Walkthrough (intraspecies example with three gene paralogs from one genome)

Enter the second directory

    cd intraspecies_example/

Align the FASTA amino acid file

    muscle -in NC_009928.1_232.faa -out NC_009928.1_232.fa

Make a codon alignment from the peptide alignment and nucleotide sequence

    pal2nal.pl NC_009928.1_232.fa NC_009928.1_232.ffn -output fasta > NC_009928.1_232.codonalign.fa

Run codeml after checking out the input/output codeml.ctl file

    codeml codeml.ctl

## Walkthrough (PseudoHunter)

Print the PseudoHunter help menu

    PseudoHunter.py -h

Run program on the test dataset
    
    cd PseudoHunter/
    cd mycobacterium/
    PseudoHunter4.py -q Mycobacterium_leprae-subset.fna -r Mycobacterium_tuberculosis_H37Rv.fna -ctl ../codeml-2.ctl -out pseudohunter_out

## Walkthrough (ParaHunter)

Print the ParaHunter help menu

    Parahunter.sh -h

Run program on the test dataset

    cd ParaHunter/
    cd cyanothece/
    ParaHunter.sh -a CyanothecePCC7425.faa -n CyanothecePCC7425.ffn -l ../codeml-2.ctl
