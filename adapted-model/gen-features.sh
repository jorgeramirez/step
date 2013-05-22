#!/bin/bash

. ./config
sphinx_fe -argfile $MODEL_HOME/feat.params -samprate 16000 -c step-14.fileids -di wav/ -do mfc/ -ei wav -eo mfc -mswav yes