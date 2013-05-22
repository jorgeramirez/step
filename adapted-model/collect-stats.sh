#!/bin/bash

. ./config

bw \
 -hmmdir $MODEL_HOME \
 -moddeffn $MODEL_HOME/mdef.txt \
 -ts2cbfn .cont. \
 -dictfn step-14.dic \
 -ctlfn step-14.fileids \
 -lsnfn step-14.transcription \
 -accumdir stats \
 -cepdir mfc \
 -feat 1s_c_d_dd
 #-feat s3_1x39
 #-feat 1s_c_d_dd \
 #-svspec 0-12/13-25/26-38 \
 #-cmn current \
 #-agc none
 # -feat s3_1x39