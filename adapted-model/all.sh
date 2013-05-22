#!/bin/bash

. ./config

./gen-features.sh
pocketsphinx_mdef_convert -text $MODEL_HOME/mdef $MODEL_HOME/mdef.txt
./collect-stats.sh
./mllr.sh
./adapt.sh
