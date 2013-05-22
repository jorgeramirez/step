#!/bin/bash

text2wfreq < step-14.txt | wfreq2vocab > step-14.vocab

text2idngram -vocab step-14.vocab -idngram step-14.idngram < step-14.txt

idngram2lm -vocab_type 0 -idngram step-14.idngram -vocab step-14.vocab -arpa step-14.arpa

sphinx_lm_convert -i step-14.arpa -o step-14.lm.DMP