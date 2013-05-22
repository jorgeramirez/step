#!/bin/bash

. ./config

cp -r $MODEL_HOME/* $MODEL_ADAPTED_HOME

map_adapt \
    -meanfn $MODEL_HOME/means \
    -varfn $MODEL_HOME/variances \
    -mixwfn $MODEL_HOME/mixture_weights \
    -tmatfn $MODEL_HOME/transition_matrices \
    -accumdir stats \
    -mapmeanfn $MODEL_ADAPTED_HOME/means \
    -mapvarfn $MODEL_ADAPTED_HOME/variances \
    -mapmixwfn $MODEL_ADAPTED_HOME/mixture_weights \
    -maptmatfn $MODEL_ADAPTED_HOME/transition_matrices
