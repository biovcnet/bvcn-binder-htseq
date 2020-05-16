## Installation
    git clone https://github.com/Arkadiy-Garber/KOALA-formatter.git

Put KO-convert-script.py in your $PATH

## Basic usage
    KO-convert-script.py -db KO_Orthology_ko00001.txt -ko user_ko_definition.txt -taxa user.out.top -out ghostokoala-summary.csv
    
KO_Orthology_ko00001.txt can be found in this repository. This file contains gene and pathway information for every KO number. This file is sourced from Elaina Graham GhostKoalaParser repo: https://github.com/edgraham/GhostKoalaParser

user_ko_definition.txt is the main file that us creared when you download the results from your finished GhostKOALA run.

user.out.top is the output file that is created when you download the taxonomy data. This input is optional.

ghostokoala-summary.csv is what we want to name our output file
