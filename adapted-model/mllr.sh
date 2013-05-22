#!/bin/bash

. ./config
mllr_solve -meanfn $MODEL_HOME/means -varfn $MODEL_HOME/variances -outmllrfn mllr_matrix -accumdir stats